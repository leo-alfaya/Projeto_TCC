import requests
from bs4 import BeautifulSoup as bs4

def get_page(url):
    page = requests.get(url)

    return bs4(page.content, "html.parser")


def get_element(page, element_css):
    items = page.select(element_css)

    return [{"text":i.get_text(), "attrs":i.attrs} for i in items]

def make_search(url, search_params):
    page = get_page(url)

    return {index:get_element(page, selector) for index, selector in search_params.items()}

def make_search_by_block(url, block, search_params):
    page = get_page(url)
    blocks = page.select(block)
    result = []

    for index, block in enumerate(blocks):
        result.append({label:get_element(block, selector) for label, selector in search_params.items()})

    return result
