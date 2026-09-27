import argparse

from .parser import parse_vacancies
from .storage import save_to_db


parser = argparse.ArgumentParser()

parser.add_argument(
    "--limit",
    type=int,
    default=None
)

parser.add_argument(
    "--db",
    type=str,
    default="vacancies.db"
)

args = parser.parse_args()

result = parse_vacancies(args.limit)
save_to_db(args.db, result)