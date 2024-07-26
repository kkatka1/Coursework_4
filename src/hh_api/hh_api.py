import requests
from .abstract_api import JobAPI

class HeadHunterAPI(JobAPI):
    """Класс для работы с API HeadHunter"""
    def __init__(self):
        self._url = 'https://api.hh.ru/vacancies'
        self._params = {'area': '1', 'per_page': "100"}

    def get_vacancies(self, search_query: str):
        self._params['text'] = search_query
        response = requests.get(self._url, params=self._params)
        response.raise_for_status()
        return response.json()['items']

