# <span id="ipv4">5.30.10.224</span>
# <span class="ipinfo--location ">
# Dubai, Dubayy (AE)&nbsp;&nbsp;<a href="/ip-lookup?query=2a00:f29:229:118c:8107:b08a:27c9:91af">[Details]</a>                                       </span>
import requests
import bs4

response = requests.get('https://www.iplocation.net/')
html_data = response.text
soup = bs4.BeautifulSoup(html_data, features='lxml')
tag = soup.find(name='span', class_="ipinfo--location")
ip = tag.text.strip()
print(ip)



