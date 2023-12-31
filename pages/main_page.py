from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage): 
    def go_to_login_page(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
        # login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        # login_link.click()
    def go_to_basket(self):
        basket_in = self.browser.find_element(By.CLASS_NAME, "btn.btn-default")
        basket_in.click()