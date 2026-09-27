import requests
from bs4 import BeautifulSoup

import time
import json

from dataclasses import dataclass 
from tqdm import tqdm

import pandas as pd
import matplotlib.pyplot as plt

import argparse


@dataclass
class Vacancy:
    vacancy_id: int | None
    title: str | None 

    company_name: str | None
    company_url: str | None
    
    salary_from: int | None
    salary_to: int | None
    currency: str | None

    work_format: str | None
    schedule: str | None
    employment: str | None
    experience: str | None

    skills: list[str]
    location: str | None
    published_at: str | None

    vacancy_url: str | None

class CaptchaError(Exception):
    pass

headers = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}




def parse_name_company(vacancy): # Функиця для парсинга наззвания компании 
    pre_name = vacancy.find("a", attrs= {"data-qa": "vacancy-company-name"})
    if pre_name is None:
        return None, None
    else:
        res1 = pre_name.text.replace("\xa0", " ")
        res2 = pre_name.get("href")
        return res1, res2

def parse_name_vacancy(vacancy): # Функиця для парсинга наззвания специальности 
    pre_name_vac = vacancy.find("h1", attrs={"data-qa": "vacancy-title"})
    if pre_name_vac is None:
        return None
    else:
        result = pre_name_vac.text
        return result

def parse_salary(salary): # Функиця для парсинга зарплаты 
    if salary is None: # зарплата не указана
        salary_from = None
        salary_to = None
        currency = None
    else: # зарплата указана
        pre = salary.find_all("data")
        target = 0 if "от" in salary.text else 1
        if len(pre) == 2 and target == 0: # указана вилка ОТ 
            salary_from = int(pre[0].get("value"))
            salary_to = None
            currency = pre[1].get("value")
        elif len(pre) == 2 and target == 1: # указана вилка ДО
            salary_from = None
            salary_to = int(pre[0].get("value"))
            currency = pre[1].get("value")         
        elif len(pre) == 3: # указана вилка ОТ и ДО
            salary_from = int(pre[0].get("value"))
            salary_to = int(pre[1].get("value"))
            currency = pre[2].get("value")
        else:
            return None, None, None
    return (salary_from, salary_to, currency) # ОТ, ДО, Валюта

def parse_work_format(vacancy): # Функция для парсинга формата работы 
    pre_work = vacancy.find("p", attrs={"data-qa": "work-formats-text"})
    if pre_work is None:
        return None
    else:
        one_step = pre_work.text.split(":")
        result = one_step[1].strip().replace("\xa0", " ")
        return result
    
def parse_schedule(vacancy):  # Функция для парсинга время работы
    pre_schedule = vacancy.find("p", attrs={"data-qa": "work-schedule-by-days-text"})
    if pre_schedule is None:
        return None
    else:
        one_step = pre_schedule.text.split(":") 
        result = one_step[1].strip().replace("\xa0", " ")
        return result
    
def parse_employment(vacancy):  # Функция для парсинга условия занятости
    pre_employment = vacancy.find("div", attrs={"data-qa": "common-employment-text"})
    if pre_employment is None:
        return None
    else:
        result = pre_employment.text
        return result

def parse_experience(vacancy): # Функция для парсинга опыта работы 
    pre_exp = vacancy.find('span', attrs ={"data-qa": 'vacancy-experience'})
    if pre_exp is None:
        return None
    else:
        result = pre_exp.text
        return result

def parse_skills(vacancy): # Функция для парсинга навыком
    skills = []
    pre_skill = vacancy.find_all("li", attrs={"data-qa": "skills-element"})
    for skill in pre_skill:
        skills.append(skill.text)
    return skills

def parse_location(vacancy): # Функция для парсинга города 
    pre_reloc = vacancy.find("div", attrs={"data-qa": "vacancy-address-with-map"})
    if pre_reloc is None:
        return None
    else:
        result = pre_reloc.text
        return result

def parse_date_and_id(vacancy): # Функция для парсинга айди вакансии и даты публикации
    pre_dt_id = vacancy.find_all("script", attrs={"type": "application/ld+json"})
    flg_json = None
    for el in pre_dt_id:
        one_step = json.loads(el.text)
        if one_step["@type"] == "JobPosting":
            flg_json = one_step
            break
    if flg_json is None:
        res_dt = None 
        res_id = None
        return res_dt, res_id
    if "datePosted" in flg_json:
        pre_dt = flg_json.get("datePosted").split("T")
        res_dt = pre_dt[0]
    else:
        res_dt = None
    if "identifier" in flg_json:
        res_id = flg_json["identifier"].get("value")
    else:
        res_id = None
        
    return res_dt, res_id



def parse_page(base_url, session, page=0, limit=20): # Парсим одну конкретную страницу
    params = {
            "text": "Ml engineer OR Data analyst OR Data science",
            "search_field": ["name", "company_name", "description"],
            "enable_snippets": "true",
            "hhtmFrom": "main", 
            "items_on_page": limit,
            "page": page
            }

    set_vacancy = []
    
    for retry in range(3):
        try:
            response = session.get(base_url, params=params, timeout=10)
            response.raise_for_status()
            break
            
        except requests.exceptions.Timeout:
            if retry == 2:
                return None
            else:
                time.sleep(2**retry)
                
        except requests.exceptions.HTTPError as error:
            http_res = error.response.status_code
            if http_res == 404:  
                print("PAGE:", page, "STATUS:", http_res)
                return []
            elif http_res == 429:
                if retry == 2:
                    return None
                else:
                    time.sleep(2**retry)  
            elif http_res // 100 == 5:
                if retry == 2:
                    return None
                else:
                    time.sleep(2**retry)
            else:
                print(f"Ошибка - {http_res}")
                return None

        except requests.exceptions.ConnectionError:
            if retry == 2:
                return None
            else:
                time.sleep(2**retry)
        
        except requests.exceptions.RequestException: 
            return None            
    
    vac_soup = BeautifulSoup(response.text, "html.parser")

    soup = vac_soup.find_all("a", attrs={"data-qa": "serp-item__title"})
    for link in soup:
        set_vacancy.append(link.get("href"))

    return set_vacancy



def parse_search(base_url, limit, session): # Парсмим страницы
    
    all_urls = []
    failed_pages = []

    page = 0
    
    while True:
        
        urls = parse_page(base_url, session, page, 20) # Принимает 20 вакансий 
        if urls is None: 
            failed_pages.append(page)
            page += 1
            print(f"Неккоректная страница с ulr {failed_pages}")
            continue
        elif urls == []: # Проверяем что не пустой список 
            break  
        else:
            
            for url in urls:
                if url in all_urls:
                    continue
                else:
                    if limit is None:
                        all_urls.append(url)
                    else:
                       if len(all_urls) >= limit:
                            return all_urls
                       else:
                           all_urls.append(url)
                           
                    
        page += 1
        
    return all_urls



def parse_vacancy(url, session):
    
    for retry in range(3):
        try:
            response = session.get(url, timeout=10) # Параметр запроса, ограничивающий сетевое ожидание.
            response.raise_for_status()
            break
            
        except requests.exceptions.Timeout:
            if retry == 2:
                return None
            else:
                time.sleep(2**retry)
                
        except requests.exceptions.HTTPError as error: # Класс ошибок http запроса
            http_res = error.response.status_code
            if http_res == 404:
                print(f"Ошибка {http_res}")
                return None
            elif http_res == 429:
                if retry == 2:
                    return None
                else:
                    time.sleep(2**retry)
            elif http_res // 100 == 5:
                if retry == 2:
                    return None
                else:
                    time.sleep(2**retry)                
            else:
                print(f"В разработке {http_res}")
                return None   

        except requests.exceptions.ConnectionError: # Класс ошибок, когда падает соединение 
            if retry == 2:
                return None
            else:
                time.sleep(2**retry)
        
        except requests.exceptions.RequestException: # Родительский класс ошибок 
            return None

    if "captcha" in response.url.lower():
        print("Обнаружена каптча")
        raise CaptchaError
    else:
            
        vacancy_url_pre = response.url # URL самой вакансии 
        soup = BeautifulSoup(response.text, "html.parser")

        company_name_pre, company_url_pre = parse_name_company(soup) # Название компании и URL компании

        title_pre = parse_name_vacancy(soup) # Название вакансии (Специальность)

        salary_from_pre, salary_to_pre, currency_pre = parse_salary(soup) # Зарплатная вилка: ОТ, ДО, Валюта

        work_format_pre = parse_work_format(soup) # Формат работы 

        schedule_pre = parse_schedule(soup) # График работы

        parse_employment_pre = parse_employment(soup) # Тип занятости вакансии

        experience_pre = parse_experience(soup) # Опыт работы 

        skills_pre = parse_skills(soup) # Обязательные киллы для работы

        location_pre = parse_location(soup) # Локация вакансии 

        published_at_pre, vacancy_id_pre = parse_date_and_id(soup) # Дата публикации, айди вакансии 
 
        result_vacancy = Vacancy(
            vacancy_id=vacancy_id_pre,
            title=title_pre,

            company_name=company_name_pre,
            company_url=company_url_pre,
    
            salary_from=salary_from_pre,
            salary_to=salary_to_pre,
            currency=currency_pre,

            work_format=work_format_pre,
            schedule=schedule_pre,
            employment=parse_employment_pre,
            
            experience=experience_pre,

            skills=skills_pre,
            location=location_pre,
            published_at=published_at_pre,

            vacancy_url=vacancy_url_pre
        )

        return result_vacancy


def parse_vacancies(limit=None):
    
    base_url = "https://krasnodar.hh.ru/search/vacancy"
    list_vacancy = []
    with requests.Session() as session:
        session.headers.update(headers)
        list_urls = parse_search(base_url, limit, session=session)
    
        for url in tqdm(list_urls, desc="Парсинг вакансий"):

            time.sleep(2)
            
            try:
                pre_vac = parse_vacancy(url, session=session)
                if pre_vac is None:
                    continue
                else:
                    list_vacancy.append(pre_vac)
            except CaptchaError:
                break

        return list_vacancy