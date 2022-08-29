import config


class PeashooterApi(object):
    def __init__(self):
        cf = config.Config()
        self.api_key = cf.peashooter['api_key']
        self.base_url = cf.peashooter['base_url']

    def get_series_list(self):
        pass

    def refresh_series_list(self):
        pass
