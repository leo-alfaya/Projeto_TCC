import requests
from bs4 import BeautifulSoup as bs4

def get_page(url):
	page = requests.get(url)
	return bs4(page.content, "html.parser")


def get_element(page, element_css):
	items = page.select(element_css)

	return items

def make_search(url, config_search):
	page = get_page(url)

	return {index:get_element(page, selector) for index, selector in config_search.items()}


data = {
	"tema":".feed-post-header",
	"titulo":".feed-post-body-title"
}

result = make_search("http://www.g1.globo.com", data)
