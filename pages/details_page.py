import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class DetailsPage(Base):

    # Locators

    name_in_details = "//h1[@itemprop='name']"
    price_in_details = "//span[@id='our_price_display']"
    add_to_cart_button = "//input[contains(@id, 'AddToCartButton')]"
    go_to_cart_link = "//p[@id='gotocart']"

    # Getters

    def get_name_in_details(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.name_in_details)))

    def get_price_in_details(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.price_in_details)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_go_to_cart_link(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.go_to_cart_link)))

    # Actions

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Click Add To Cart")

    def click_go_to_cart(self):
        self.get_go_to_cart_link().click()
        print("Click Go To Cart Link")

    # Methods

    """ Метод добавления товара в корзину и перехода на страницу заказа """

    def add_to_cart_and_move_to_order(self):
        with allure.step("Select Filter Talisman-Stone"):
            Logger.add_start_step(method="select_filter_talisman_stone")
            self.get_current_url()
            self.click_add_to_cart_button()
            self.click_go_to_cart()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="select_filter_talisman_stone")
