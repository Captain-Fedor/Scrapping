

import requests
import bs4
import re
from pprint import pprint
import json


def get_city(data, cities=['Москва', 'Санкт-Петербург']):
    city_tag = data.find(class_="info-section--N695JG77kqwzxWAnSePt")
    town = city_tag.find(class_="fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni").text
    if town in cities:
        return town
    else:
        return None

def get_job_title(data, pattern = r'[Pp]ython|[Пп]итон?[a-я]'):
    job_title_tag = data.find(class_="vacancy-title")
    job_title = job_title_tag.find('h1', class_="bloko-header-section-1").text
    result = re.findall(pattern, job_title)
    if len(result)>=1:
        return job_title
    else:
        return None

def check_job_description(data, pattern = r'[Ff]lask|[Dd]jango'):
    job_description = data.find(class_="g-user-content").text
    result = re.findall(pattern, job_description)
    if len(result) >= 1:
        return result
    else:
        return None
def create_file_data(data):
    if None not in data:
        parsed_data.append([job_title, city, company_name, salary, job_description, link])




HEADERS = {'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; _'
                     'gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru; _ym_isad=2;'
                     ' __gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
          'Accept-Language': 'ru-RU,ru;q=0.9',
          'Sec-Fetch-Dest': 'document',
          'Sec-Fetch-Mode': 'navigate',
          'Sec-Fetch-Site': 'same-origin',
          'Sec-Fetch-User': '?1',
          'Cache-Control': 'max-age=0',
          'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/96.0.4664.93 Safari/537.36',
          'sec-ch-ua-mobile': '?0'}

main_response = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2', headers=HEADERS)
main_html = main_response.text
main_soup = bs4.BeautifulSoup(main_html, features='lxml')
vacancy_tag = main_soup.find(id="a11y-main-content")
vacancies_tags = vacancy_tag.find_all(name='div', class_="vacancy-card--z_UXteNo7bRGzxWVcL7y font-inter")
parsed_data =[]
for vacancy_tag in vacancies_tags:
    h2_tag = vacancy_tag.find('h2', class_="bloko-header-section-2")
    a_tag = h2_tag.find('a')
    city = get_city(vacancy_tag)
    # city_tag = vacancy_tag.find(class_="info-section--N695JG77kqwzxWAnSePt")
    # city = city_tag.find(class_="fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni").text
    link = a_tag['href']
    '''переход к странице вакансии'''
    job_page = requests.get(link, headers=HEADERS)
    html_job_page = job_page.text
    job_soup = bs4.BeautifulSoup(html_job_page, features='lxml')
    job_contents = job_soup.find(name='div', class_="bloko-columns-row")
    job_title = get_job_title(job_contents)
    job_title_tag = job_contents.find(class_="vacancy-title")
    # job_title = job_title_tag.find('h1', class_="bloko-header-section-1").text
    salary = job_title_tag.find(class_="magritte-text___pbpft_3-0-12 magritte-text_style-primary___AQ7MW_3-0-12"
                                        " magritte-text_typography-label-1-regular___pi3R-_3-0-12").text
    company_name = job_contents.find(class_="vacancy-company-name").text
    job_description = check_job_description(job_contents)
    job_result_data = [job_title, city, company_name, salary, job_description, link]
    create_file_data(job_result_data)
    print(job_title)
    print(city)
    print(job_description)
    print(salary)
    print(company_name)
    print(link)
    print()

with open("jobs_list.json", "w", encoding='utf8') as write_file:
    json.dump(parsed_data, write_file, ensure_ascii=False)

