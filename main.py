# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.hh_api.hh_api import HeadHunterAPI
from src.vacancy.vacancy import Vacancy
from src.saver.json_saver import JSONSaver
# import json

def user_interaction():
    #Создание экземпляра класса для работы с APIсайтов с вакансиями
    hh_api = HeadHunterAPI()

    search_query = input("Введите поисковый запрос: ")
    #Получение количества вакансийдля вывода в топ N от пользователя
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    #Получение ключевых слов для фильтрации вакансий от пользователя
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    #Очистка и нормализаци ключевых слов
    filter_words = [word.strip(",. ").lower() for word in filter_words]

    #Получение вакансий с hh.ruв формате JSON'
    vacancies_data = hh_api.get_vacancies(search_query)
    print(f"Получено {len(vacancies_data['items'])} вакансий")

    #Преобразование набора данных из JSON в список объектов'
    vacancies_list = Vacancy.cast_to_object_list(vacancies_data)
    #print(f"преобразовано в {len(vacancies_list)}объектов")

    json_saver = JSONSaver()
    #Сохранение всех вакансий в файл
    for vacancy in vacancies_list:
        json_saver.add_vacancy(vacancy)
    #print("Вакансии сохранены")

    #Описание всех вакансий
    for vacancy in vacancies_list:
        print(vacancy.description)

    #Фильтрация вакансий по ключевым словам
    #filter_words_lower = [word.lower() for word in filter_words]
    filtered_vacancies = [v for v in vacancies_list if any(word in v.description.lower() for word in filter_words)]
    print(f"Отфильтровано {len(filtered_vacancies)} вакансий")

    if len(filtered_vacancies) == 0:
        print("Ключевые слова для фильтрации: ", filter_words)
        for vacancy in vacancies_list:
            print("Описание: ", vacancy.description.lower())
            for word in filter_words:
                if word in vacancy.description.lower():
                    print(f"Найдено ключевое слово '{word}' в описании")

    #Сортирока вакансий по зп в порядке убывания'
    sorted_vacancies = sorted(filtered_vacancies, key=lambda x: (x.salary or 0), reverse=True)
    #Получение топ N вакансий
    top_vacancies = sorted_vacancies[:top_n]
    print(f"Топ {top_n} вакансий готов")

    for vacancy in top_vacancies:
        print(f"Название: {vacancy.title}")
        print(f"Ссылка: {vacancy.url}")
        print(f"Зарплата: {vacancy.salary}")
        print(f"Описание: {vacancy.description}")
        print("-" * 40)


if __name__ == "__main__":
    user_interaction()

