import re


class Vacancy:
    """
    Класс вакансии
    """
    __slots__ = ('__name_vacancy', '__salary', '__url', '__requirement')

    def __init__(self, name_vacancy: str, salary: str, url: str, requirement: str) -> None:
        """
        Конструктор вакансии
        :param name_vacancy: Название вакансии
        :param salary: Зарплата
        :param url: ссылка на вакансию
        :param requirement: Требования
        """
        self.__name_vacancy = name_vacancy
        self.__salary = 0 if salary is None else int(salary)
        self.__url = url

        clean_string = re.sub(r'<.*?.', '', str(requirement))
        self.__requirement = clean_string.replace('\n', ' ')
        
    @property
    def name_vacancy(self) -> str:
        """
        Метод получения названия вакансии
        :return: Название вакансии
        """
        return self.__name_vacancy

    @property
    def salary(self) -> int:
        """
        Метод получения зарплаты
        :return: Зарплата
        """
        return self.__salary

    @property
    def url(self) -> str:
        """
        Метод получения URL-адреса
        :return: Ссылка на вакансию
        """
        return self.__url

    @property
    def requirement(self) -> str:
        """
        Метод получения требованиц к вакансии
        :return: Требования вакансии
        """
        return self.__requirement

    def __gt__(self, other) -> bool:
        return self.__salary > other.__salary

    def __lt__(self, other) -> bool:
        return self.__salary < other.__salary

    def __str__(self) -> str:
        """
        Вывод в виде строки
        :return: Строковое представление вакансии
        """
        return f'{self.__name_vacancy}, Зарплата: {self.__salary}, Требования: {self.__requirement}, URL: {self.__url}'
