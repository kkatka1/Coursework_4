import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.hh_api.hh_api import HeadHunterAPI
from src.vacancy.vacancy import Vacancy
from src.saver.json_saver import JSONSaver
from src.utils.utils import get_top_vacancies, filter_vacancies
# import json

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

    top_vacancies = get_top_vacancies(filtered_vacancies, top_n)
    print(f"Топ {top_n} вакансий готов")

    for vacancy in top_vacancies:
        print(vacancy)
        print("-" * 40)



if __name__ == "__main__":
    user_interaction()

