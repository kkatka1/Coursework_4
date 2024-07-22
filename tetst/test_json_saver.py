import pytest
import os
import json
from src.saver.json_saver import JSONSaver
from src.vacancy.vacancy import Vacancy

@pytest.fixture
def json_saver(tmp_path):
    file_path = tmp_path / "vacancies.json"
    return JSONSaver(file_path=str(file_path))

def test_add_vacancy(json_saver):
    v1 = Vacancy("Python Developer", "http://example.com/1", "100 000 руб.", "Description")
    json_saver.add_vacancy(v1)
    data = json_saver.load_data()
    assert len(data) == 1
    assert data[0]['title'] == "Python Developer"

pytest
