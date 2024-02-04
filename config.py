from pathlib import Path

URL_HH = "https://api.hh.ru/vacancies"
PROJECT: Path = Path(__file__).parent
PATH_FILE = PROJECT.joinpath("vacancies.json")
