import os.path
import re
import sys
from zipfile import ZipFile

import config
from peashooter.client import PeashooterClient
from sonarr.client import SonarrClient
from thefuzz import fuzz

seriesMatchRatio = int(config.Config().basic['series_match_ratio'])


def get_episode_list(series_id, season):
    sonarr_client = SonarrClient()
    file_list = sonarr_client.get_episode_file_list(series_id)
    file_list = list(filter(lambda item: item['seasonNumber'] == season, file_list))
    file_list.sort(key=lambda item: item['relativePath'])
    return file_list


def find_series(name):
    """
    模糊查询 series
    """
    peashooter_client = PeashooterClient()
    series_list = peashooter_client.get_series_list()
    return list(filter(lambda series: fuzz.partial_ratio(series['name'], name) >= seriesMatchRatio, series_list))


def get_output_dir(episode_list):
    """
    获取 series 的存储路径
    """
    output_dir = set()
    for episode in episode_list:
        # 先替换开始的 '/'
        split_parts = episode['path'].replace('/', '', 1).split('/')
        # 不包括映射目录，所以从 1 开始
        output_dir.add("/".join(split_parts[1:len(split_parts) - 1]))
    if len(output_dir) != 1:
        raise ValueError("输出路径有误，请检查")
    return output_dir.pop()


def is_tc(filename):
    """
    是繁体字幕
    """
    pattern = re.compile(r".tcjp.|.tc.|-tc.|_tc.", re.IGNORECASE)
    match = pattern.search(filename)
    return match is not None


def array_fill(two_dimension_list):
    # 系统最大值递减来填充列表
    maxsize = sys.maxsize
    len_list = [len(item) for item in two_dimension_list]
    if set(len_list) != 1:
        maximum_len = max(*len_list)
        for item in two_dimension_list:
            for _ in range(maximum_len - len(item)):
                maxsize = maxsize - 1
                item.append(str(maxsize))
    return two_dimension_list


def deduce_episode_num_solt(name_list):
    """
    推断 episode 的位置
    """
    pattern = re.compile(r'(\d+)')
    match_items = [pattern.findall(name) for name in name_list]
    # 填充列表，避免有空数据
    match_items = array_fill(match_items)
    for i, v in enumerate([set(item) for item in zip(*match_items)]):
        if len(v) == len(name_list):
            return i
    return -1


def get_filename_episode_num_map(name_list):
    """
    生成 "压缩文件内成员名 -> episode num" 的映射
    """
    result = dict()
    solt = deduce_episode_num_solt(name_list)
    pattern = re.compile(r'(\d+)')
    for name in name_list:
        it = pattern.finditer(name)
        for i, v in enumerate(it):
            if i == solt:
                result[name] = int(v.group())
    return result


def get_episode_num_filename_map(episode_list):
    """
    生成 "episode num -> 最终字幕文件名" 的映射
    """
    pattern = re.compile(r'S(\d+)E(\d+)')
    result = dict()
    for i, episode in enumerate(episode_list):
        # 最终字幕文件名称
        filename = re.sub("mkv|mp4", "zh.ass", episode['relativePath'].split("/")[1])
        match = pattern.search(filename)
        # 获取 episode 编号
        episode_num = int(match.group(2))
        if i + 1 != episode_num:
            raise ValueError('Episode 编号不匹配')
        result[episode_num] = filename
    return result


def rename(series_id, season, zip_file_path, drive):
    # 从 sonarr 获取 episode 文件列表
    episode_file_list = get_episode_list(series_id, season)
    output_dir = os.path.join(drive, get_output_dir(episode_file_list))
    # 解压缩
    with ZipFile(zip_file_path) as zip_file:
        item_file_name_list = zip_file.namelist()
        item_file_name_list = list(filter(lambda item: not is_tc(item), item_file_name_list))
        item_file_name_list.sort()
        filename_episode_num_map = get_filename_episode_num_map(item_file_name_list)
        episode_num_filename_map = get_episode_num_filename_map(episode_file_list)

        for item_file_name in item_file_name_list:
            with zip_file.open(item_file_name) as item_file:
                data = item_file.read()
                final_item_file_name = episode_num_filename_map.get(filename_episode_num_map.get(item_file_name))
                if final_item_file_name is not None:
                    with open(os.path.join(output_dir, final_item_file_name), 'w+b') as copied_file:
                        copied_file.write(data)


if __name__ == '__main__':
    pass
