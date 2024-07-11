import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger

""" Локаторы, атрибуты и методы страницы со списком товаров """


class ProductsPage(Base):

    # Locators

    main_stone_string = "//h1[@class='category-name']"
    filter_by_earrings = "//a[contains(text(),'Серьги')]"
    sort_by = "//select[@id='sort-select']"
    product_labels = "//span[@class='grid-name']"
    next_page_button = "//a[contains(@class,'next_page page')]"
    images_list = "//ul[@id='product_list ']/li/div"
    prices_list = "//ul[@id='product_list ']/li/div/div/div/div/div/span/span"
    name_in_details = "//h1[@itemprop='name']"
    price_in_details = "//span[@id='our_price_display']"

    # Getters
    def get_filter_by_earrings(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.filter_by_earrings)))

    def get_sort_by(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.sort_by)))

    def get_next_page_button(self):
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, self.next_page_button)))

    def get_image_from_list(self):
        elements_images_list = self.driver.find_elements(By.XPATH, self.images_list)
        return elements_images_list[0]

    def get_elements_products_labels(self):
        return self.driver.find_elements(By.XPATH, self.product_labels)

    def get_images_from_list(self):
        return self.driver.find_elements(By.XPATH, self.images_list)

    def get_product_label(self):
        elements_product_labels = self.driver.find_elements(By.XPATH, self.product_labels)
        return elements_product_labels[0]

    def get_product_price(self):
        elements_prices_list = self.driver.find_elements(By.XPATH, self.prices_list)
        return elements_prices_list[1]

    def get_name_in_details(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.name_in_details)))

    def get_price_in_details(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.price_in_details)))

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

    def click_image_from_list(self):
        self.get_image_from_list().click()
        print("Click Image From Products")

    # Methods

    """ Метод проверки соответствия выбранного фильтра по типу украшения 'Серьги' списку товаров по всем выданным страницам """

    def select_filter_by_earrings(self):
        with allure.step("Select Filter By Earrings"):
            Logger.add_start_step(method="select_filter_by_earrings")
            filter_text = self.get_filter_by_earrings().text
            sub_str = self.get_substr_from_filter(filter_text)
            self.click_filter_by_earrings()
            print("Filter By Earrings Done")
            elements_products_labels = self.get_elements_products_labels()
            str_products_labels = self.list_str_from_list_webelements(elements_products_labels)
            try:
                while len(str_products_labels) > 0:
                    self.is_substr_in_list_str(sub_str, str_products_labels)
                    self.click_next_page_button()
                    elements_products_labels = self.get_elements_products_labels()
                    str_products_labels = self.list_str_from_list_webelements(elements_products_labels)
                    self.click_next_page_button()
                    print("The Next Page")
            except TimeoutException:
                print("The End of Products List")
            url_page_1 = self.url_parse()
            self.driver.get(url_page_1[0])
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="select_filter_by_earrings")

    """ Метод перехода на детельную страницу продукта страницу из списка товаров """

    def go_to_details_product_page(self):
        with allure.step("Go To Details Product Page"):
            Logger.add_start_step(method="go_to_details_product_page")
            self.click_image_from_list()
            self.get_current_url()
            print("Details Page Displayed")
            Logger.add_end_step(url=self.driver.current_url, method="go_to_details_product_page")

    """ Метод сравнения названия и цены продукта с плитки из списка товаров с детальной страницей товара """

    def compare_name_price_tile_and_details(self):
        with allure.step("Compare Name Price Tile And Details"):
            Logger.add_start_step(method="compare_name_price_tile_and_details")
            product_name_tile = self.get_product_label().text
            print(product_name_tile)
            product_price_tile = self.get_product_price().text
            print(product_price_tile)
            self.go_to_details_product_page()
            product_name_details = self.get_name_in_details().text
            print(product_name_details)
            assert self.compare_strings(product_name_tile, product_name_details)
            print("Product Name in Products List and Details are the same")
            product_price_details = self.get_price_in_details().text
            print(product_price_details)
            assert self.compare_numbers(product_price_tile, product_price_details)
            print("Product Price in Products List and Details are the same")
            Logger.add_end_step(url=self.driver.current_url, method="compare_name_price_tile_and_details")
