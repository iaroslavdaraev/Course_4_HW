import re


class Vacancy:
    """
    Класс вакансии
    """
    __slots__ = ('__vacancy_name', '__salary', '__url', '__requirement')

    def __init__(self, vacancy_name: str, salary: str, url: str, requirement: str) -> None:
        """
        Конструктор вакансии
        :param vacancy_name: Название вакансии
        :param salary: Зарплата
        :param url: ссылка на вакансию
        :param requirement: Требования
        """
        self.__vacancy_name = vacancy_name
        self.__salary = 0 if salary is None else int(salary)
        self.__url = url

        clean_string = re.sub(r'<.*?.', '', str(requirement))
        self.__requirement = clean_string.replace('\n', ' ')

    def __gt__(self, other) -> bool:
        return self.__salary > other.__salary

    def __lt__(self, other) -> bool:
        return self.__salary < other.__salary

    def __str__(self) -> str:
        """
        Вывод в виде строки
        :return: Строковое представление вакансии
        """
        return f'{self.__vacancy_name}, Зарплата: {self.__salary}, Требования: {self.__requirement}, URL: {self.__url}'
