import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators import OrderPageLocators


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators

    @allure.step("Заполнить первую форму заказа")
    def fill_order_form_1(self, name, surname, address, metro, phone):
        self.wait.until(EC.visibility_of_element_located(self.locators.NAME_INPUT))
        self.send_keys(self.locators.NAME_INPUT, name)
        self.send_keys(self.locators.SURNAME_INPUT, surname)
        self.send_keys(self.locators.ADDRESS_INPUT, address)

        self.click_element(self.locators.METRO_INPUT)
        self.send_keys(self.locators.METRO_INPUT, metro)
        self.send_keys(self.locators.METRO_INPUT, Keys.ARROW_DOWN)
        self.send_keys(self.locators.METRO_INPUT, Keys.ENTER)

        self.click_element(self.locators.PHONE_INPUT)

        self.send_keys(self.locators.PHONE_INPUT, phone)
        self.click_element(self.locators.NEXT_BUTTON)

    @allure.step("Заполнить вторую форму заказа")
    def fill_order_form_2(self, delivery_date, rental_period, color, comment=None):

        self.send_keys(self.locators.DELIVERY_DATE, delivery_date)
        self.click_element(self.locators.DELIVERY_DATE)

        self.click_element(self.locators.FORM_HEADER)

        self.click_element(self.locators.RENTAL_PERIOD)

        rental_option = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{rental_period}']")
        self.click_element(rental_option)

        if color == "чёрный жемчуг":
            self.click_element(self.locators.COLOR_BLACK)
        elif color == "серая безысходность":
            self.click_element(self.locators.COLOR_GREY)

        if comment:
            self.send_keys(self.locators.COMMENT_INPUT, comment)

        self.click_element(self.locators.ORDER_BUTTON)
        self.click_with_js(self.locators.YES_BUTTON)

    @allure.step("Получить сообщение об успешном заказе")
    def get_success_message(self):
        return self.get_text(self.locators.SUCCESS_MESSAGE)    


