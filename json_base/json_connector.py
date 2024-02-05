import json
from abc import ABC, abstractmethod


class Connector(ABC):
    """
    Абстрактный класс для работы с данными
    """

    @abstractmethod
    def __init__(self, path: str) -> None:
        """
        Абстрактный метод инициализации
        :param path: Путь к файлу
        """
        raise NotImplementedError

    @abstractmethod
    def read(self) -> list[dict]:
        """
        Абстрактный метод чтения данных
        :return: Список
        """
        raise NotImplementedError

    @abstractmethod
    def write(self, data: list[dict]) -> None:
        """
        Абстрактный метод записи данных
        :param data: Список
        :return: None
        """
        raise NotImplementedError

    @abstractmethod
    def get_vacancy_keywords(self, keywords: list[dict]) -> list[dict]:
        """
        Абстрактный метод получения данных по ключевым словам
        :param keywords: Ключевые слова
        :return: Список
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, keywords_delete: list[dict]) -> None:
        """
        Абстрактный метод удаления данных по ключевым словам
        :param keywords_delete: Ключевые слова
        :return: Список
        """
        raise NotImplementedError


class JSONConnector(Connector):
    """
    класс для работы с данными
    """

    def __init__(self, path: str) -> None:
        """
        Инициализация
        :param path: Путь к файлу
        """
        self.path = path

    def read(self) -> list[dict]:
        """
        Чтение данных из файла JSON
        :return: Список
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def write(self, data: list[dict]) -> None:
        """
        Запись данных в файл JSON
        :param data: Список
        :return:
        """
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def get_vacancy_keywords(self, filter_words: list[dict]) -> list[dict]:
        """
        Получение данных по ключевым словам из файла JSON
        :param filter_words: Ключевые слова
        :return: Список
        """
        data = self.read()
        matching_vacancies = [vacancy for vacancy in data if all(keyword in vacancy['vacancy_name']
                                                                 or (vacancy['requirement']
                                                                     and keyword in vacancy['requirement']) for keyword
                                                                 in filter_words)]

        return matching_vacancies

    def delete(self, keywords_delete: list[dict]) -> None:
        """
        Удаление данных по ключевым словам из файла JSON
        :param keywords_delete: Ключевые слова
        :return: Список
        """
        data = self.read()
        new_data = [vacancy for vacancy in data if not all(
            keyword in vacancy['name_vacancy'] or keyword in vacancy['requirement'] for keyword in keywords_delete)]
        self.write(new_data)
