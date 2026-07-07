import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    # Локаторы
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_TOP_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать'][1]")
    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")

    # Вопросы
    
    def get_question_locator(self, question_number):
        return (By.ID, f"accordion__heading-{question_number}")

    def get_answer_locator(self, question_number):
        return (By.ID, f"accordion__panel-{question_number}")

    # Методы
    
    @allure.step("Принять куки")
    def accept_cookies(self):
        self.click_element(self.COOKIE_BUTTON)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_top(self):
        self.click_element(self.ORDER_TOP_BUTTON)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_bottom(self):
        self.click_element(self.ORDER_BOTTOM_BUTTON)

    @allure.step("Нажать на логотип 'Самокат'")
    def click_logo_scooter(self):
        self.click_element(self.LOGO_SCOOTER)

    @allure.step("Нажать на логотип 'Яндекс'")
    def click_logo_yandex(self):
        self.click_element(self.LOGO_YANDEX)

    # === МЕТОД ДЛЯ РАБОТЫ С ВОПРОСАМИ ===

    @allure.step("Кликнуть на вопрос")
    def click_question(self, question_number):
        locator = self.get_question_locator(question_number)
        self.click_element(locator)

    @allure.step("Получить текст ответа на вопрос")
    def get_answer_text(self, question_number):
        locator = self.get_answer_locator(question_number)
        return self.get_text(locator)
    

