import re
import requests

url = 'http://www.monmouth.edu/news/archives'

html = requests.get(url)

html_src = (str)(html.content)

tittle_pattern = re.compile('<div class="article-header">(.+?)</div>')

tittles = tittle_pattern.findall(html_src)

print(html_src)