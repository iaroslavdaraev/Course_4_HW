from config import PATH_FILE
from utils import search_vacancies, sort_vacancies, write_to_file, load_to_file, search_keywords, delete_vacancies


def user_interaction():
    """
    Взаимодействие с пользователем
    :return: None
    """
    while True:
        user_selection = input("Выберете действие:\n"
                               f"'1' - Начать поиск,\n'2' - Загрузить из файла,\n'0' - Выход\n")

        if user_selection == '1':
            search_query = input("Введите поисковый запрос: ")
            list_vacancies = search_vacancies(search_query)
            for vacancy in list_vacancies:
                print(f'{vacancy}\n')

            user_selection = input("Записать найденные вакансии в файл?\n"
                                   f"'1' - Да,\n'2' - Нет,\n'0' - Выход\n")
            if user_selection == '2' or user_selection == '0':
                break
            else:
                write_to_file(PATH_FILE, list_vacancies)

        elif user_selection == '2':
            list_vacancies = load_to_file(PATH_FILE)

            while True:
                user_selection = input(f"'1' - Вывести весь список,\n'2' - Вывести по зарплате,\n"
                                       f"'3' - Вывести по ключевым словам,\n'4' - Удалить по ключевым словам,\n"
                                       f"'0' - Выход\n")
                if user_selection == '1':
                    for vacancy in list_vacancies:
                        print(f"{vacancy}\n")

                elif user_selection == '2':
                    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
                    sort_vac = sort_vacancies(list_vacancies, top_n)
                    for vacancy in sort_vac:
                        print(f"{vacancy}\n")

                elif user_selection == '3':
                    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
                    keywords = filter_words
                    matching_vacancies = search_keywords(PATH_FILE, keywords)
                    for vacancy in matching_vacancies:
                        print(f"{vacancy}\n")

                elif user_selection == '4':
                    filter_words = input("Введите ключевые слова для удаления вакансий из файла: ").split()
                    keywords = filter_words
                    delete_vacancies(PATH_FILE, keywords)
                    print("Данные удалены")

                elif user_selection == '0':
                    exit()

                else:
                    print("Ввели не верное значение. Пожалуйста, повторите.")

        elif user_selection == '0':
            break
        else:
            print("Ввели не верное значение. Пожалуйста, повторите.")
            continue


if __name__ == '__main__':
    user_interaction()
