import requests


class BaseApi:
    @staticmethod
    def get_request(url_link, paarams=None):
        response = requests.get(url_link, params=paarams)
        return response