from abc import ABC, abstractmethod

class JobAPI(ABC):
    """Абстрактный класс для работы с APIсервиса с вакансиями"""
    @abstractmethod
    def get_vacancies(self, search_query: str):
        pass
