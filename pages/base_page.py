from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
browser = webdriver.Chrome(options=chrome_options)


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        time.sleep(5)
    

stepik_base = BasePage(browser, 'https://stepik.org/lesson/238819/step/2?unit=211271')
stepik_base.open()
