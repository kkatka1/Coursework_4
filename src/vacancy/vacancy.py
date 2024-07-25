class Vacancy:
    """Класс для предоставления вакансий
    Аргументы:
    title (str): название вакансии
    url(str): ссылка на вакансию
    salary(str): зарплата
    description(str):описание вакансии
    """
    def __init__(self, title, url, salary, description):
        self.title = title
        self.url = url
        self.salary = self.parse_salary(salary)
        self.description = description

    def parse_salary(self, salary) -> int:
        """Парсинг зарплаты из строки"""
        if salary is None:
            return 0
        if isinstance(salary, int):
            return salary
        if isinstance(salary, str):
            if salary.lower() in ['зарплата не указана','не указана']:
                return 0

            cleaned_salary = salary.replace(' ','').replace('руб.', '').replace('руб', '')
            try:
                return int(cleaned_salary)
            except ValueError:
                return 0
        if isinstance(salary, dict):
            salary_from = salary.get('from')
            salary_to = salary.get('to')
            if salary_from and salary_to:
                return (salary_from + salary_to) // 2
            return salary_from if salary_from else salary_to if salary_to else 0
        return 0

    def __lt__(self, other):
        """Магисечкий метод для сравнения вакансий по зарплате"""
        return self.salary < other.salary

    def __le__(self, other):
        """Магисечкий метод для сравнения вакансий по зарплате"""
        return self.salary <= other.salary

    def __gt__(self, other):
        """Магисечкий метод для сравнения вакансий по зарплате"""
        return self.salary > other.salary

    def __ge__(self, other):
        """Магисечкий метод для сравнения вакансий по зарплате"""
        return self.salary >= other.salary

    def __eq__(self, other):
        """Магисечкий метод для сравнения вакансий по зарплате"""
        return self.salary == other.salary


    @classmethod
    def cast_to_object_list(cls, vacancies_data):
        """Преобразование данных вакансий в объекты классов Vacancy"""
        return [
            cls(
                vac['name'],
                vac['alternate_url'],
                vac.get('salary'),
                vac['snippet']['responsibility']
            )for vac in vacancies_data
        ]

    def __str__(self):
        """Строковое представление объекта Vacancy"""
        return f"Название: {self.title}\nСсылка: {self.url}\nЗарплата: {self.salary}\nОписание: {self.description}\n "
#
# v1 = Vacancy("Python Developer", "http://example.com/1", "100 000 руб.", "Description")
# v2 = Vacancy("Java Developer", "http://example.com/2", "150 000 руб.", "Description")
#
# print(v1.compare_salary(v2))





