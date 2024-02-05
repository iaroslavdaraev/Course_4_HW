from config import PATH_FILE
from json_base.json_connector import JSONConnector
from src.api_connector import HeadHunterAPIConnector
from vacancy_prog.vacancies import Vacancy


def search_vacancies(search_query: str) -> list[Vacancy]:
    """
    Поиск вакансий
    :param search_query: Поисковый запрос
    :return: Список найденных по запросу вакансий
    """
    hh_api = HeadHunterAPIConnector(search_query)
    hh_vacancies = hh_api.get_vacancies()

    list_vacancies = []
    for item in hh_vacancies:
        list_vacancies.append(
            Vacancy(item['name'], item['salary']['from'], item['alternate_url'], item['snippet']['requirement']))
    return list_vacancies


def load_to_file(path: str) -> list[Vacancy]:
    """
    Загруза вакансий из файла
    :param path: Путь к файлу
    :return: Список вакансий из файла
    """
    json_file = JSONConnector(path)
    data = json_file.read()
    list_vacancies = []
    for item in data:
        list_vacancies.append(Vacancy(item['name_vacancy'], item['salary'], item['url'], item['requirement']))
    return list_vacancies


def write_to_file(path: str, data: list[Vacancy]) -> None:
    """
    Запись данных в файл
    :param path: Путь к файлу
    :param data: Список вакансий из файла
    :return: None
    """
    json_file = JSONConnector(path)
    list_vacancies = []
    for item in data:
        vacancy_dict = {
            'name_vacancy': item.name_vacancy,
            'salary': item.salary,
            'url': item.url,
            'requirement': item.requirement
        }
        list_vacancies.append(vacancy_dict)

    json_file.write(list_vacancies)


def sort_vacancies(data: list[Vacancy], top_n: int) -> list[Vacancy]:
    """
    Сортировка вакансий по зарпалате
    :param data:
    :param top_n:
    :return:
    """
    return sorted(data, reverse=True)[:top_n]


def search_keywords(path: str, keywords: list[str]) -> list[Vacancy]:
    """
    Поиск вакансий по ключевым словам
    :param path: Путь к файлу
    :param keywords: Ключевые слова
    :return: Список вакансий
    """
    json_file = JSONConnector(path)
    matching_vacancies = json_file.get_vacancy_keywords(keywords)
    list_vacancies = []
    for item in matching_vacancies:
        list_vacancies.append(Vacancy(item['name_vacancy'], item['salary'], item['url'], item['requirement']))
    return list_vacancies


def delete_vacancies(path: str, keywords_delete: list[str]) -> None:
    """
    Удаление акансий по ключевым словам
    :param path: Путь к файлу
    :param keywords_delete: Ключевые слова
    :return: None
    """
    json_file = JSONConnector(path)
    json_file.delete(keywords_delete)
