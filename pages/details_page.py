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

    main_stone_string = "//h1[@class='category-name']"
    filter_by_earrings = "//a[contains(text(),'Серьги')]"
    sort_by = "//select[@id='sort-select']"
    product_labels = "//span[@class='grid-name']"
    next_page_button = "//a[@class='next_page page']"
    add_to_cart_buttons = "//a[contains(@id, 'AddToCartButton')]"
    images_list = "//ul[@id='product_list ']/li/div"
    prices_list = "//ul[@id='product_list ']/li/div/div/div/div/div/span/span"

    # Getters
    def get_filter_by_earrings(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.filter_by_earrings)))

    def get_sort_by(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.sort_by)))

    def get_next_page_button(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.next_page_button)))

    def get_add_to_cart(self):
        elements_add_to_cart = self.driver.find_elements(By.XPATH, self.add_to_cart_buttons)
        return elements_add_to_cart[1]

    def get_image_from_list(self):
        elements_images_list = self.driver.find_elements(By.XPATH, self.images_list)
        return elements_images_list[4]

    def get_elements_products_labels(self):
        return self.driver.find_elements(By.XPATH, self.product_labels)

    def get_product_label(self):
        elements_product_labels = self.driver.find_elements(By.XPATH, self.product_labels)
        return elements_product_labels[4]

    def get_product_price(self):
        elements_prices_list = self.driver.find_elements(By.XPATH, self.prices_list)
        return elements_prices_list[9]

    # Actions
    def click_filter_by_earrings(self):
        self.get_filter_by_earrings().click()
        print("Click Filter By Earrings")

    def click_sort_by(self):
        self.get_sort_by().click()
        print("Click Sort By")

    def sort_by_price_asc(self):
        select = Select(self.get_sort_by())
        select.select_by_index(1)

    def click_next_page_button(self):
        self.get_next_page_button().click()
        print("Click Next Page Button")

    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print("Click Add to Cart")

    def click_image_from_list(self):
        self.get_image_from_list().click()
        print("Click Image From Products")

    # Methods

    """ Метод проверки соответствия выбранного фильтра по типу украшения 'Серьги' списку товаров по всем выданным страницам """