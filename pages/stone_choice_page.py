import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger

""" Локаторы, атрибуты и методы страницы выбора камня-талисмана """


class StoneChoice(Base):

    # Locators
    customer_name = "//input[@id='custName']"
    day_dropdown = "//select[@name='custDay']"
    month_dropdown = "//select[@name='custMonth']"
    year_dropdown = "//select[@name='custYear']"
    define_stone_button = "//input[@id='define_stones']"
    main_word = "//h1[@class='header']"

    # Getters
    def get_customer_name(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.customer_name)))

    def get_day_dropdown(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.day_dropdown)))

    def get_month_dropdown(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.month_dropdown)))

    def get_year_dropdown(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.year_dropdown)))

    def get_define_stone_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.define_stone_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions
    def input_customer_name(self, name):
        self.get_customer_name().send_keys(name + ' ')
        print("Enter Customer Name")

    # def select_day_dropdown(self, day):
    #     select = Select(self.get_day_dropdown())
    #     select.select_by_value(day)
    #     print("Enter Day in Dropdown")

    # def select_month_dropdown(self, month):
    #     select = Select(self.get_month_dropdown())
    #     select.select_by_value(month)
    #     print("Enter Month in Dropdown")

    # def select_year_dropdown(self, year):
    #     select = Select(self.get_year_dropdown())
    #     select.select_by_value(year)
    #     print("Enter Year in Dropdown")

    def click_define_stone_button(self):
        self.get_define_stone_button().click()
        print("Click Define Stone Button")

    # Methods

    """ Метод ввода имени покупателя в поле ввода """

    def enter_customer_name(self, customer_name):
        with allure.step("Enter Customer Name"):
            Logger.add_start_step(method="enter_customer_name")
            self.get_current_url()
            self.input_customer_name(customer_name)
            print("Customer Named Typed")
            Logger.add_end_step(url=self.driver.current_url, method="enter_customer_name")

    """ Метод ввода даты рождения покупателя с помощью дропдаунов """

    def enter_birthday(self, day, month, year):
        with allure.step("Enter Birthday"):
            Logger.add_start_step(method="enter_birthday")
            day = str(day)
            month = str(month)
            year = str(year)
            self.get_current_url()
            select = Select(self.get_day_dropdown())
            select.select_by_value(day)
            select = Select(self.get_month_dropdown())
            select.select_by_value(month)
            select = Select(self.get_year_dropdown())
            select.select_by_value(year)
            print("Birthday Entered")
            Logger.add_end_step(url=self.driver.current_url, method="enter_birthday")

    """ Метод подтверждения ввода данных покупателя и выбора камня-талисмана """

    def confirm_define_stone(self):
        with allure.step("Confirm Define Stone"):
            Logger.add_start_step(method="confirm_define_stone")
            self.click_define_stone_button()
            self.assert_url('https://mineralmarket.ru/rezultat-opredelenie-kamnya')
            Logger.add_end_step(url=self.driver.current_url, method="confirm_define_stone")
