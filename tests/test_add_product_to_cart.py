from pages.details_page import DetailsPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.products_page import ProductsPage
from pages.stone_choice_page import StoneChoice
from pages.your_stone_page import YourStone
import allure


@allure.description("Test Select Product By Talisman Stone And Type And Add To Cart")
def test_select_product_by_talisman_stone_and_type_and_add_to_cart(set_up):

    driver = set_up

    """ Авторизация на сайте """
    lp = LoginPage(driver)
    lp.authorization()
    lp.assert_word(lp.get_main_word(), 'Марина Афанасьева')

    """ Выбор фильтра 'Личный камень-талисман' """
    mp = MainPage(driver)
    mp.select_filter_talisman_stone()

    """ Ввод персональных данных и подтверждение подбора камня-талисмана """
    sc = StoneChoice(driver)
    sc.enter_birthday(23, 10, 1982)
    sc.enter_customer_name("Марина")
    sc.confirm_define_stone()
    sc.assert_word(sc.get_main_word(), 'Ваши личные камни талисманы')

    """ Проверка соответсвия полученного списка товаров камню-талисману """
    ys = YourStone(driver)
    ys.select_main_stone()

    """ Выбор фильтра по типу украшения и проверка соответсвия полученного списка товаров типу украшения. 
    Выбор определенного товара из списка и сравнение названия и цены продукта с плитки из списка товаров с детальной страницей товара """

    pp = ProductsPage(driver)
    pp.select_filter_by_earrings()
    pp.compare_name_price_tile_and_details()

    """ Добавление товара в корзину и переход на страницу корзины. Сравнение названия и цены продукта на детальной странице товара и в корзине """
    dp = DetailsPage(driver)
    dp.compare_name_price_details_and_cart()
