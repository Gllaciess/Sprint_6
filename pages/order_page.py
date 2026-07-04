from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):

    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//div[contains(@class, 'select-search__value')]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")


    DELIVERY_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")
    RENTAL_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option')]")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")

    def fill_order_form_1(self, name, surname, address, metro, phone):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.SURNAME_INPUT, surname)
        self.send_keys(self.ADDRESS_INPUT, address)
        self.click_element(self.METRO_INPUT)
        self.send_keys(self.METRO_INPUT, metro)
        self.click_element(self.METRO_OPTION)
        self.send_keys(self.PHONE_INPUT, phone)
        self.click_element(self.NEXT_BUTTON)

    def fill_order_form_2(self, delivery_date, rental_period, color):
        self.send_keys(self.DELIVERY_DATE, delivery_date)
        self.click_element(self.DELIVERY_DATE)
        self.click_element(self.RENTAL_PERIOD)
        rental_option = (By.XPATH, f"//div[text()='{rental_period}']")
        self.click_element(rental_option)
        if color == "чёрный жемчуг":
            self.click_element(self.COLOR_BLACK)
        elif color == "серая безысходность":
            self.click_element(self.COLOR_GREY)
        self.click_element(self.ORDER_BUTTON)
        self.click_element(self.YES_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
    

    