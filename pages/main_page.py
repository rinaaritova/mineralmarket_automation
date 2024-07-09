import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger

""" Локаторы, атрибуты и методы главной страницы сайты """


class MainPage(Base):

    # Locators
    filter_talisman_stone = "//div[@id='left_column']/ul/li[2]"

    # Getters
    def get_filter_talisman_stone(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.filter_talisman_stone)))

    # Actions
    def click_filter_talisman_stone(self):
        self.get_filter_talisman_stone().click()
        print("Click Filter Option Talisman Stone")

    """ Метод выбора фильта по опции 'Личный камень-талисман' """

    # Methods
    def select_filter_talisman_stone(self):
        with allure.step("Select Filter Talisman-Stone"):
            Logger.add_start_step(method="select_filter_talisman_stone")
            self.get_current_url()
            self.click_filter_talisman_stone()
            self.assert_url('https://mineralmarket.ru/opredelenie-kamnya')
            Logger.add_end_step(url=self.driver.current_url, method="select_filter_talisman_stone")
