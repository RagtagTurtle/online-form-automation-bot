from config import keys
from selenium import webdriver

def order(k):
    driver = webdriver.Chrome('./chromedriver')
    driver.get(k['product_url'])

    driver.find_element_by_xpath('')

if __name__ == '__main__':
    order(keys)