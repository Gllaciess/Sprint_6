import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from constants import Urls


@allure.feature('Логотипы')
class TestLogo:

    @allure.title('Переход на главную по логотипу "Самокат"')
    @allure.story('Переход на главную по логотипу')
    def test_click_logo_scooter_go_to_main(self, driver):
        main_page = MainPage(driver)
        driver.get(Urls.BASE_URL)
        main_page.accept_cookies()

        main_page.click_logo_scooter()

        assert driver.current_url == Urls.BASE_URL

    @allure.title('Клик на логотип "Яндекс"')
    @allure.story('Переход в Дзен по логотипу "Яндекс"')
    def test_click_logo_yandex_go_to_dzen(self, driver):
        main_page = MainPage(driver)
        driver.get(Urls.BASE_URL)
        main_page.accept_cookies()

        main_window = driver.current_window_handle

        main_page.click_logo_yandex()

        WebDriverWait(driver, 10).until(
            EC.number_of_windows_to_be(2)
        )

        for window_handle in driver.window_handles:
            if window_handle != main_window:
                driver.switch_to.window(window_handle)
                break

        WebDriverWait(driver, 15).until(
            EC.url_contains("dzen")
        )

        assert "dzen" in driver.current_url


