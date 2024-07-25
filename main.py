import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.hh_api.hh_api import HeadHunterAPI
from src.vacancy.vacancy import Vacancy
from src.saver.json_saver import JSONSaver
# import json


def get_top_vacancies(vacancies, top_n):
    """Получить топ N ваканстй по зп"""
    return sorted(vacancies, key=lambda x: (x.salary or 0), reverse=True)[:top_n]

def filter_vacancies(vacancies, filter_words):
    """Фильтрация вакансий по ключевым словам в описании"""
    return [v for v in vacancies if any(word in v.description.lower() for word in filter_words)]

def user_interaction():
    """Функция взаимодействия с пользователем через консоль"""
    hh_api = HeadHunterAPI()

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filter_words = [word.strip(",. ").lower() for word in filter_words]

    vacancies_data = hh_api.get_vacancies(search_query)
    print(f"Получено {len(vacancies_data)} вакансий")

    vacancies_list = Vacancy.cast_to_object_list(vacancies_data)

    json_saver = JSONSaver()
    for vacancy in vacancies_list:
        json_saver.add_vacancy(vacancy)

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    print(f"Отфильтровано {len(filtered_vacancies)} вакансий")

    if len(filtered_vacancies) == 0:
        print("Ключевые слова для фильтрации: ", filter_words)
        for vacancy in vacancies_list:
            print("Описание: ", vacancy.description.lower())
            for word in filter_words:
                if word in vacancy.description.lower():
                    print(f"Найдено ключевое слово '{word}' в описании")

    #sorted_vacancies = sorted(filtered_vacancies, key=lambda x: (x.salary or 0), reverse=True)

    top_vacancies = get_top_vacancies( filtered_vacancies, top_n)
    print(f"Топ {top_n} вакансий готов")

    for vacancy in top_vacancies:
        print(f"Название: {vacancy.title}")
        print(f"Ссылка: {vacancy.url}")
        print(f"Зарплата: {vacancy.salary}")
        print(f"Описание: {vacancy.description}")
        print("-" * 40)



if __name__ == "__main__":
    user_interaction()

