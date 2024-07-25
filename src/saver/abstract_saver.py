from abc import ABC, abstractmethod

"""Абстрактный класс для сохранения вакансий в файл"""

class Saver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def save_data(self, data):
        pass

