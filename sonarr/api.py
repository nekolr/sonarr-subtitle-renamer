import config


class SonarrApi(object):
    def __init__(self):
        cf = config.Config()
        self.base_url = cf.sonarr['base_url']
        self.api_key = cf.sonarr['api_key']

    def get_episode_file_list(self, series_id):
        pass
