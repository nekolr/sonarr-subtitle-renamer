import configparser


class Config(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.sonarr = {
            'base_url': config['sonarr']['baseUrl'],
            'api_key': config['sonarr']['apiKey']
        }
        self.peashooter = {
            'base_url': config['peashooter']['baseUrl'],
            'api_key': config['peashooter']['apiKey']
        }
        self.basic = {
            'series_match_ratio': config['basic']['seriesMatchRatio']
        }
