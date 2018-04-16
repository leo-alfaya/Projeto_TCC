import requests
from bs4 import BeautifulSoup as bs4

def get_page(url):
	page = requests.get(url)
	return bs4(page.content, "html.parser")

def get_element(page, element_css):
	result = page.select(element_css)
	return result

def teste_g1():
	page = get_page("http://www.g1.globo.com")
	result = get_element(page, ".bstn-fd-cover-picture img")

	return result
