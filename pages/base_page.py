import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Поиск элемента на странице")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Клик по элементу")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    @allure.step("Ввод текста")
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return element

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        return self.find_element(locator).text
    
    @allure.step("Клик по элементу")
    def click_with_js(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить текущее окно")
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Ожидать количество окон")
    def wait_for_windows(self, count):
        WebDriverWait(self.driver, 10).until(
            EC.number_of_windows_to_be(count)
        )

    @allure.step("Ожидать URL содержит текст")
    def wait_for_url_contains(self, text):
        WebDriverWait(self.driver, 15).until(
            EC.url_contains(text)
        )


        