import pytest
from src.vacancy.vacancy import Vacancy

def test_parse_salary():
    #Тестируем различные форматы зарплаты
    assert Vacancy('Test', 'url', '100 000 руб.', 'desc').salary == 100000
    assert Vacancy('Test', 'url', 'зарплата не указана', 'desc').salary == 0
    assert Vacancy('Test', 'url', 'None', 'desc').salary == 0
    assert Vacancy('Test', 'url', '100000 руб.', 'desc').salary == 100000
    assert Vacancy('Test', 'url', 'не указана', 'desc').salary == 0
    assert Vacancy('Test', 'url', {"from": 100000, "to": 150000}, 'desc').salary == 125000
    assert Vacancy('Test', 'url', {"from": 100000}, 'desc').salary == 100000
    assert Vacancy('Test', 'url', {"to": 150000}, 'desc').salary == 150000
    assert Vacancy('Test', 'url', {}, 'desc').salary == 0

def test_compare_salary():
    v1 = Vacancy("Python Developer", "http://example.com/1", "100 000 руб.", "Description")
    v2 = Vacancy("Java Developer", "http://example.com/2", "150 000 руб.", "Description")

    assert v1.compare_salary(v2) == "Python Developer имеет меньшую зарплату, чем Java Developer"
    assert v2.compare_salary(v1) == "Java Developer имеет большую зарплату, чем Python Developer"
    assert v1.compare_salary(v1) == "Python Developer и Python Developer имеют одинаковые зарплаты"



