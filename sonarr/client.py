import json
import requests
from sonarr.api import SonarrApi


class SonarrClient(SonarrApi):

    def get_episode_file_list(self, series_id):
        get_episode_file_list_uri = '/api/v3/episodefile'
        params = {
            "apikey": self.api_key,
            "seriesId": series_id
        }
        resp = requests.get(self.base_url + get_episode_file_list_uri, params)
        return json.loads(resp.text) if resp.status_code == 200 else []
