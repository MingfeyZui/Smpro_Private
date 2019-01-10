#!/usr/local/bin/python3

import urllib.request
from bs4 import BeautifulSoup

url = urllib.request.urlopen("https://elpais.com/tecnologia/2016/10/27/actualidad/1477578212_336319.html")
html = url.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")
# for link in soup.find_all("a"):
#     print(link.get("href"))
paragraphs = list(soup.find_all("p"))
texts = [paragraph.get_text() for paragraph in paragraphs]
print("\n".join(texts))
