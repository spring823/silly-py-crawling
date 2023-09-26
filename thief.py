#实现最简单的小说内容爬取
import codecs
import requests
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
x = requests.get('https://www.changyeyuhuo.com/book/39062/7637028_2.html')

print(x.text)

soup = BeautifulSoup(x.text,"html.parser",from_encoding="utf-8")
div = soup.find('div', class_='reader-main')
text = div.get_text("\n")
print(text)
with codecs.open("novel.txt",mode="a",encoding="utf-8") as file_txt:
    file_txt.write(text)

