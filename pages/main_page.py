from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_TOP_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать'][1]")
    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")

    def accept_cookies(self):
        self.click_element(self.COOKIE_BUTTON)

    def click_order_top(self):
        self.click_element(self.ORDER_TOP_BUTTON)

    def click_order_bottom(self):
        self.click_element(self.ORDER_BOTTOM_BUTTON)

    def click_logo_scooter(self):
        self.click_element(self.LOGO_SCOOTER)

    def click_logo_yandex(self):
        self.click_element(self.LOGO_YANDEX)


        