import requests
from .abstract_api import JobAPI

class HeadHunterAPI(JobAPI):
    def get_vacancies(self, search_query: str):
        url = 'https://api.hh.ru/vacancies'
        params = {'text': search_query, 'area': '1'}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

