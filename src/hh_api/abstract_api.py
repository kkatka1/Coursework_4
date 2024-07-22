from abc import ABC, abstractmethod

class JobAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_query: str):
        pass
