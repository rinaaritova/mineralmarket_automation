import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger

""" Локаторы, атрибуты и методы страницы камня-талисмана"""


class YourStone(Base):

    # Locators

    main_stone = "//div[@id='mainStone']/h4/b/a"
    product_labels = "//span[@class='grid-name']"
    next_page_button = "//a[@class='next_page page']"

    # Getters
    def get_main_stone(self):
        return WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.XPATH, self.main_stone)))

    def get_next_page_button(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.next_page_button)))

    def get_elements_products_labels(self):
        return self.driver.find_elements(By.XPATH, self.product_labels)

    # Actions
    def click_main_stone(self):
        self.get_main_stone().click()
        print("Click Main Stone")

    def click_next_page_button(self):
        self.get_next_page_button().click()
        print("Click Next Page Button")

    # Methods

    """ Метод проверки соответствия выбранного камня списку товаров по всем выданным страницам """

    def select_main_stone(self):
        with allure.step("Select Main Stone"):
            Logger.add_start_step(method="select_main_stone")
            self.get_current_url()
            sub_str = self.get_main_stone().text
            print(sub_str)
            self.click_main_stone()
            self.move_to_new_tab()
            # webelements_products_labels = self.driver.find_elements(By.XPATH, self.product_labels)
            # str_products_labels = self.list_str_from_list_webelements(webelements_products_labels)
            elements_products_labels = self.get_elements_products_labels()
            str_products_labels = self.list_str_from_list_webelements(elements_products_labels)
            try:
                while len(str_products_labels) > 0:
                    self.is_substr_in_list_str(sub_str, str_products_labels)
                    self.click_next_page_button()
                    # webelements_products_labels = self.driver.find_elements(By.XPATH, self.product_labels)
                    # str_products_labels = self.list_str_from_list_webelements(webelements_products_labels)
                    elements_products_labels = self.get_elements_products_labels()
                    str_products_labels = self.list_str_from_list_webelements(elements_products_labels)
                    self.click_next_page_button()
                    print("The Next Page")
            except TimeoutException:
                print("The End of Products List")
            Logger.add_end_step(url=self.driver.current_url, method="select_main_stone")
