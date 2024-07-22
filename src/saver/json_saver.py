import os
import json

class JSONSaver:
    def __init__(self, file_path='data/vacancies.json'):
        #Инициализация класса с указанием пути к файлу
        self.file_path = file_path
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def add_vacancy(self, vacancy):
        #Загрузка текущих данных из файла
        data = self.load_data()
        #Добавление новой вакансии в данные
        data.append(vacancy.__dict__)
        #Сохранение обновленных данных обратно в файл
        self.save_data(data)

    def delete_vacancy(self, vacancy):
        #Загрузка текущих данных из файла
        data = self.load_data()
        #Фильтрация данных для удаления вакансии с указанным заголовком
        new_data = [v for v in data if v['title'] != vacancy.title]
        #Сохранение обновленных данных обратно в файл
        self.save_data(new_data)

    def load_data(self):
        #Попытка открыть и загрузить данные из файла
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
        #Если файл не нвйден, возвращаем пустой список
            return []

    def save_data(self, data):
        #Открытие файла для записи данных
        with open(self.file_path, 'w', encoding='utf-8') as file:
            #Запись данных в формате JSON в файл
            json.dump(data, file, ensure_ascii=False, indent=4)

# if __name__ == "__main__":
#
#     from src.vacancy.vacancy import Vacancy
#     json_saver = JSONSaver()
#
#     v1 = Vacancy("Python Developer", "http://example.com/1", "100 000 руб.", "Description")
#     v2 = Vacancy("Java Developer", "http://example.com/2", "150 000 руб.", "Description")
#
#     json_saver.add_vacancy(v1)
#     json_saver.add_vacancy(v2)
#
#     json_saver.delete_vacancy(v1)