import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators

    # Методы
    
    @allure.step("Принять куки")
    def accept_cookies(self):
        self.click_element(self.locators.COOKIE_BUTTON)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_top(self):
        self.click_element(self.locators.ORDER_TOP_BUTTON)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_bottom(self):
        self.click_element(self.locators.ORDER_BOTTOM_BUTTON)

    @allure.step("Нажать на логотип 'Самокат'")
    def click_logo_scooter(self):
        self.click_element(self.locators.LOGO_SCOOTER)

    @allure.step("Нажать на логотип 'Яндекс'")
    def click_logo_yandex(self):
        self.click_element(self.locators.LOGO_YANDEX)

    # Методы для вопросов

    @allure.step("Кликнуть на вопрос")
    def click_question(self, question_number):
        locator = (By.ID, f"accordion__heading-{question_number}")
        self.click_element(locator)

    @allure.step("Получить текст ответа на вопрос")
    def get_answer_text(self, question_number):
        locator = (By.ID, f"accordion__panel-{question_number}")
        return self.get_text(locator)
    

