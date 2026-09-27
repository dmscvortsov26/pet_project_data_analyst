import sqlite3

import json
from parser import Vacancy

def vacancy_exists(cursor, vacancy_id):
    cursor.execute(
        """
        SELECT
            vacancy_id 
        FROM vacancies
        WHERE TRUE 
        AND vacancy_id = ?
        """,
        (
        vacancy_id,
        )
    )
    
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False

def save_vacancy(cursor, vacancy):
    if vacancy.vacancy_id is None:
        print("ID вакансии отсутсвует")
    else:
        flg_id = vacancy_exists(cursor, vacancy.vacancy_id)
        if flg_id == True:
            print("Вакансия уже существует в БД")
        else:
            cursor.execute("""
                        INSERT INTO vacancies (vacancy_id, title, company_name, 
                           company_url, salary_from, salary_to, 
                           currency, work_format, schedule, employment, 
                           experience, skills, location, published_at, vacancy_url)
                           
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, 
                        (
                        vacancy.vacancy_id, vacancy.title, vacancy.company_name, 
                        vacancy.company_url, vacancy.salary_from, vacancy.salary_to, 
                        vacancy.currency, vacancy.work_format, vacancy.schedule, vacancy.employment,
                        vacancy.experience, json.dumps(vacancy.skills, ensure_ascii=False), vacancy.location, vacancy.published_at, vacancy.vacancy_url
                        )               
                      )
            print("Вакансия добавлена")


def save_vacancies(connection, cursor, result_parse):
    with connection:
        for vacancy in result_parse:
            save_vacancy(cursor, vacancy)


def init_db(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS vacancies (
            vacancy_id INTEGER PRIMARY KEY,
            title TEXT,

            company_name TEXT,
            company_url TEXT,

            salary_from INTEGER,
            salary_to INTEGER,
            currency TEXT,
    
            work_format TEXT,
            schedule TEXT,
            employment TEXT,
            experience TEXT,
        
            skills TEXT,
            location TEXT,
            published_at TEXT,

            vacancy_url TEXT
        );
        """
              )


def save_to_db(db_path, vacancies):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    init_db(cursor)
    save_vacancies(connection, cursor, vacancies)

    print("Вакансии успешно загружены")

    connection.close()
    print("Отключение")


def load_vacancies(cursor): # Функция интерпаритриует данные из БД в объект Vacancy
    result = []
    
    cursor.execute(
        """
        SELECT * FROM vacancies
        """
    )
    pre_vac = cursor.fetchall()
    for vac in pre_vac:
        vacancy = Vacancy(
                vacancy_id = vac[0],
                title = vac[1],
                company_name = vac[2],
                company_url = vac[3],
                salary_from = vac[4],
                salary_to = vac[5],
                currency = vac[6],
                work_format = vac[7],
                schedule = vac[8],
                employment = vac[9],
                experience = vac[10],
                skills = json.loads(vac[11]),
                location = vac[12],
                published_at = vac[13],
                vacancy_url = vac[14]
                )
        result.append(vacancy)
    return result