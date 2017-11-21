import requests
from bs4 import BeautifulSoup as bs4

def get_page(url):
	page = requests.get(url)
	return bs4(page.content, "html.parser")	

def get_element(page, element_css):
	return page.select(element_css)
