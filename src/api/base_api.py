import requests


class BaseApi:

    def __init__(self):
        self.host = 'https://test.mirvracha.ru'

    def post_application(self, endpoint, payload=None, exp_status_code=200):
        response = requests.post(url=f"{self.host}/{endpoint}", data=payload)
        assert response.status_code == exp_status_code
        return response.json()
