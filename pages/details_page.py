import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class DetailsPage(Base):

    # Locators

    name_in_details = "//h1[@itemprop='name']"
    name_in_cart = "//p[@class='product-name']/a"
    price_in_details = "//span[@id='our_price_display']"
    price_in_cart = "//span[@id='delivery_block_total_price']"
    add_to_cart_button = "//input[@name='Submit']"
    cart_icon = "//a[@class='headrd-cart ']"

    # Getters

    def get_name_in_details(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.name_in_details)))

    def get_price_in_details(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.price_in_details)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.XPATH, self.add_to_cart_button)))

    def get_cart_icon(self):
        return WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.XPATH, self.cart_icon)))

    def get_name_in_cart(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.name_in_cart)))

    def get_price_in_cart(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.price_in_cart)))

    # Actions

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Click Add To Cart")

    def click_cart_icon(self):
        self.get_cart_icon().click()
        print("Click Cart Icon")

    # Methods

    """ Метод добавления товара в корзину и перехода на страницу корзины """

    def add_to_cart_and_move_to_cart(self):
        with allure.step("Add To Cart And Move To Order"):
            Logger.add_start_step(method="add_to_cart_and_move_to_order")
            self.click_add_to_cart_button()
            self.click_cart_icon()
            self.assert_url('https://mineralmarket.ru/order.php')
            Logger.add_end_step(url=self.driver.current_url, method="add_to_cart_and_move_to_order")

    """ Метод сравнения названия и цены продукта на детальной странице и в корзине """

    def compare_name_price_details_and_cart(self):
        with allure.step("Compare Name Price Details And Cart"):
            Logger.add_start_step(method="compare_name_price_details_and_cart")
            self.get_current_url()
            product_name_details = self.get_name_in_details().text
            print(product_name_details)
            product_price_details = self.get_price_in_details().text
            print(product_price_details)
            self.add_to_cart_and_move_to_cart()
            product_name_cart = self.get_name_in_cart().text
            print(product_name_cart)
            assert self.compare_strings(product_name_details, product_name_cart)
            print("Product Name in Details and Cart are the same")
            product_price_cart = self.get_price_in_cart().text
            print(product_price_cart)
            assert self.compare_numbers(product_price_details, product_price_cart)
            print("Product Price in Details and Cart are the same")
            Logger.add_end_step(url=self.driver.current_url, method="compare_name_price_details_and_cart")
