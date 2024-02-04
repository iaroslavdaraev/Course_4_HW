from abc import ABC, abstractmethod

import requests

from config import URL_HH


class APIConnector(ABC):
    """
    Абстрактный класс для получения вакансий через API
    """

    @abstractmethod
    def __init__(self, search_text: str):
        """
        Инициализация полей
        :param search_text:
        """
        raise NotImplementedError

    @abstractmethod
    def get_vacancies(self) -> list[dict]:
        """
        Получение списка вакансий
        :return: Список вакансий
        """
        raise NotImplementedError


class HeadHunterAPIConnector(APIConnector):
    def __init__(self, search_text: str):
        """
        Инициализация полей API
        :param search_text:
        :param area:
        """
        self.__params = {
            'page': 0,
            'per_page': 100,
            'text': search_text,
            'search_field': 'name',
            'only_with_salary': True
        }

    def get_vacancies(self) -> list[dict]:
        """
            Получение списка вакансий API HeadHunter
            :return: Список вакансий
            """
        response = requests.get(URL_HH, params=self.__params)
        data = response.json()
        return data['items']
