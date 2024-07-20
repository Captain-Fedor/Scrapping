from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pprint import pprint
path = ChromeDriverManager().install()
browser_service = Service(executable_path=path)
browser = Chrome(service=browser_service)

def wait_element(browser, delay_seconds=1, by=By.CLASS_NAME, value=None):
    return WebDriverWait(browser, delay_seconds).until(
        expected_conditions.presence_of_element_located((by, value))
    )

browser.get('https://habr.com/ru/articles')
tm_article_list_tag = browser.find_element(By.CLASS_NAME, 'tm-articles-list')
article_tags = tm_article_list_tag.find_elements(By.TAG_NAME, 'article')

parsed_data = []
for article in article_tags:
    time_tag = wait_element(article, 1, By.TAG_NAME, 'time')
    pub_time = time_tag.get_attribute('datetime')
    parsed_data.append(
        {'date':  pub_time}
    )

pprint(parsed_data)