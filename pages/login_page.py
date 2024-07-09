from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from utilities.logger import Logger
import allure

""" Локаторы, атрибуты и методы страницы авторизации на сайте """


class LoginPage(Base):

    base_url = 'https://mineralmarket.ru/'

    # Locators

    login_button = "//a[@class='top_user_info_item'][1]"
    login = "//input[@id='login']"
    password = "//input[@id='passwd']"
    enter_button = "//button[@id='submitlogin']"
    main_word = "//span[@class='top_user_info_item']"

    # Getters

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_login(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.login)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.password)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_login_button(self):
        self.get_login_button().click()
        print("Click Login button")

    def click_enter_button(self):
        self.get_enter_button().click()
        print("Click Enter button")

    def input_login(self):
        self.get_login().send_keys('rinaaritova@yandex.ru')
        print("Input Login")

    def input_password(self):
        self.get_password().send_keys('ivan555')
        print("Input Password")

    # Methods

    """ Метод авторизации покупателя на сайте """

    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.base_url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_login_button()
            self.input_login()
            self.input_password()
            self.click_enter_button()
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
