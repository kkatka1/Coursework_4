import pytest
from src.hh_api.hh_api import HeadHunterAPI

@pytest.fixture
def hh_api():
    return HeadHunterAPI()

def test_get_vacancies(hh_api):
    vacancies = hh_api.get_vacancies("Python")
    assert 'items' in vacancies
    assert isinstance(vacancies['items'], list)
    if vacancies['items']:
        assert 'name' in vacancies['items'][0]
        assert 'alternate_url' in vacancies['items'][0]
        assert 'snippet' in vacancies['items'][0]
        assert 'responsibility' in vacancies['items'][0]['snippet']

pytest