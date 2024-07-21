# div id="post-content-body">
# time datetime="2024-07-20T04:40:26.000Z" title="2024-07-20, 07:40">1 час назад</time>
# href="/ru/articles/830128/" class="tm-title__link"
# class="tm-title tm-title_h2"
# class="tm-articles-list"

# <main class="vacancy-serp-content">
class ="vacancy-search-item__card serp-item_link vacancy-card-container--OwxCdOj5QlSlCBZvSggS"

<span class="vacancy-name--c1Lay3KouCl7XasYakLk serp-item__title-link" data-qa="serp-item__title">Web - аналитик/аналитик маркетинговых данных</span>

< span


class ="vacancy-name--c1Lay3KouCl7XasYakLk serp-item__title-link" data-qa="serp-item__title" > Разработчик CRM AI (Python) (Удаленно) < /span >

< div






import requests
import bs4
from pprint import pprint
from urllib.parse import urljoin

main_response = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2')
main_html = main_response.text
main_soup = bs4.BeautifulSoup(main_html, features='lxml')
vacancy_tag = main_soup.find(name='main', class_='vacancy-serp-content')
vacancies_tags = vacancy_tag.find_all('article')
print(articles_tags)

parsed_data = []
for article_tag in articles_tags:
    time_tag = articles_tag.find('time')
    pub_time = time_tag['datetime']

    h2_tag = article_tag.find('h2', class_="tm-title")
    title = h2_tag.text.strip()

    a_tag = h2_tag.find('a')
    relative_link = a_tag['href']
    link = urljoin('https://habr.com/', relative_link)

    response_full_article = requests.get(link)
    html_full_article = response_full_article.text
    soup_full_article = bs4.BeautifulSoup(html_full_article, features='lxml')
    tag_full_article = soup_full_article.find(id="post-content-body")
    text_full_article = tag_full_article.text

    parsed_data.append({
        'pub_time': pub_time,
        'title': title,
        'link': link,
        'text': text_full_article[:30]
    })

print(parsed_data[0])
print(parsed_data[1])




