def get_top_vacancies(vacancies, top_n):
    """Получить топ N вакансий по зп"""
    return sorted(vacancies, reverse=True)[:top_n]

def filter_vacancies(vacancies, filter_words):
    """Фильтрация вакансий по ключевым словам в описании"""
    return [v for v in vacancies if v.description and any(word in v.description.lower() for word in filter_words)]
