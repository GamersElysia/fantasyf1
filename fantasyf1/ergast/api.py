import requests

default_base_url = 'http://ergast.com/api/'

class Client:
    def __init__(self):
        self.base_url = default_base_url

    def __call__(self, resource):
        r = requests.get(self.base_url + resource + '.json')
        r.raise_for_status()
        data = r.json()
        # Ergast always returns JSON data inside an MRData property which seems
        # a bit redundant.
        # At least if MRData doesn't exist we know something's up.
        return data['MRData']
