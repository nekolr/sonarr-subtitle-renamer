import json
import requests
from peashooter.api import PeashooterApi


class PeashooterClient(PeashooterApi):

    def get_series_list(self):
        get_series_list_uri = '/api/sonarr/series'
        params = {"apiKey": self.api_key}
        resp = requests.get(self.base_url + get_series_list_uri, params)
        return json.loads(resp.text)['data'] if resp.status_code == 200 else []

    def refresh_series_list(self):
        refresh_series_list_uri = '/api/sonarr/refresh-series'
        params = {"apiKey": self.api_key}
        resp = requests.get(self.base_url + refresh_series_list_uri, params)
        return json.loads(resp.text)['data'] if resp.status_code == 200 else []
