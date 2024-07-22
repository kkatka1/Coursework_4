class Vacancy:
    def __init__(self, title: str, url: str, salary: str, description: str):
        self.title = title
        self.url = url
        self.salary = self.parse_salary(salary)
        #Добавим вывод для отладки, чтобы проверить что происходит с salary
        # print(f'Обрабатываем зарплату: {salary} -> {self.salary}')
        self.description = description

    def parse_salary(self, salary) -> int:
        #Если зарплата не указана, возвращаем 0
        if salary is None:
            return 0

        #Если зп уже целое число, возвращаем ее
        if isinstance(salary, int):
            return salary

        # Если зп строка, обрабатываем ее
        if isinstance(salary, str):
            if salary.lower() in ['зарплата не указана','не указана']:
                return 0

            #Удаляем пробелы из слова "руб.","руб"
            cleaned_salary = salary.replace(' ','').replace('руб.', '').replace('руб', '')

            #Пытаемся преобразовать строку в число
            try:
                return int(cleaned_salary)
            except ValueError:
                #Если не удается,указываем 0
                return 0
        if isinstance(salary, dict):
            salary_from = salary.get('from')
            salary_to = salary.get('to')
            if salary_from and salary_to:
                return (salary_from + salary_to) // 2
            return salary_from if salary_from else salary_to if salary_to else 0
        #Если тип salary неожиданный, возвращаем 0
        return 0

    def compare_salary(self, other) -> str:
        if self.salary > other.salary:
            return f"{self.title} имеет большую зарплату, чем {other.title}"
        elif self.salary < other.salary:
            return f"{self.title} имеет меньшую зарплату, чем {other.title}"
        else:
            return f"{self.title} и {other.title} имеют одинаковые зарплаты"
    @classmethod
    def cast_to_object_list(cls, vacancies_data):
        return [
            cls(
                vac['name'],
                vac['alternate_url'],
                vac.get('salary'),
                vac['snippet']['responsibility']
            )for vac in vacancies_data['items']
        ]
#
# v1 = Vacancy("Python Developer", "http://example.com/1", "100 000 руб.", "Description")
# v2 = Vacancy("Java Developer", "http://example.com/2", "150 000 руб.", "Description")
#
# print(v1.compare_salary(v2))





