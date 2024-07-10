import datetime

""" Базовые методы, используемые в классах потомках """


class Base:

    def __init__(self, driver):
        self.driver = driver

    """ Метод получения текущего url страницы """
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL " + get_url)

    """ Метод для проверки значения текста на странице """
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(f"Good main word: {value_word}")

    """ Метод взятия скриншота страницы """
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\marina.afanaseva\\PycharmProjects\\mineral_market\\screen\\' + name_screenshot)

    """ Метод взятия URL страницы """
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print(f"Good value URL {get_url}")

    """ Метод переключения на вторую вкладку """
    def move_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        print("Move to New Tab")
        self.get_current_url()

    """ Метод проверяет содержится ли подстрока в списке из строк """

    def is_substr_in_list_str(self, sub_str, list_of_str):
        # result = False
        for elem in list_of_str:
            if sub_str.casefold() in elem.casefold():
                # result = True
                assert True
            else:
                print(f"Substring {sub_str} NOT in String {elem}")
                assert False

    """ Метод создания списка строк из списка веб элементов """

    def list_str_from_list_webelements(self, list_webelements):
        list_str = []
        for elem in list_webelements:
            list_str.append(elem.text)
        print(list_str)
        return list_str

    """ Метод получения подстрок из названий фильтров """

    def get_substr_from_filter(self, filter_name):
        if filter_name == 'Браслеты':
            sub_str = filter_name[7:0]
        elif filter_name == 'Кольца':
            sub_str = filter_name[5:0]
        else:
            sub_str = filter_name
        return sub_str

    """Метод удаления 'руб.' из строки и преобразования строки в число"""

    def remove_rub_and_to_number(self, string):
        new_str = string.replace('руб.', '')
        new_str_2 = new_str.replace(' ', '')
        price = int(new_str_2)
        return price

    """ Метод сравнения двух строк """

    def compare_strings(self, string_1, string_2):
        if string_1 == string_2:
            return True
        else:
            return False

    """ Метод сравнения двух чисел """

    def compare_numbers(self, number_1, number_2):
        if number_1 == number_2:
            return True
        else:
            return False

    """ Метод разделения url до и после знака вопроса """
    def url_parse(self):
        full_url = self.driver.current_url
        parsed_url = full_url.split('?', 1)
        print(parsed_url)
        return parsed_url
