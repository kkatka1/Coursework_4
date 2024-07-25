import os
import json
from .abstract_saver import Saver

class JSONSaver:
    """Класс для сохранения вакансий в JSON файл
    Атрибуты:
    - file_path (str): Путь к файлу для сохранения вакансий
    """
    def __init__(self, file_path='data/vacancies.json'):
        self._file_path = file_path
        os.makedirs(os.path.dirname(self._file_path), exist_ok=True)

    def add_vacancy(self, vacancy):
        """Метод добавления вакансии в JSON файл"""
        data = self.load_data()
        data.append(vacancy.__dict__)
        self.save_data(data)

    def delete_vacancy(self, vacancy):
        """Метод удаления вакансий"""
        data = self.load_data()
        new_data = [v for v in data if v['title'] != vacancy.title]
        self.save_data(new_data)

    def load_data(self):
        """Метод загрузки данных из JSON файла"""
        try:
            with open(self._file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self, data):
        """Метод сохраниния данных в JSON файл"""
        with open(self._file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


#
# if __name__ == "__main__":
#
#     from src.vacancy.vacancy import Vacancy
#     json_saver = JSONSaver()
# #
#     v1 = Vacancy("Python Developer", "http://example.com/1", "100 000 руб.", "Description")
#     v2 = Vacancy("Java Developer", "http://example.com/2", "150 000 руб.", "Description")
# #
#     json_saver.add_vacancy(v1)
#     json_saver.add_vacancy(v2)
# #
#     json_saver.delete_vacancy(v1)