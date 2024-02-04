from src.api_connector import HeadHunterAPIConnector


def user_interaction():
    """
    Взаимодействие с пользователем
    :return: None
    """
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    hh_api = HeadHunterAPIConnector(search_query)
    hh_vacancies = hh_api.get_vacancies()

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = filter_vacancies(hh_vacancies, filter_words)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == '__main__':
    user_interaction()
