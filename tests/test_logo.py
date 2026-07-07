import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Urls


@allure.feature('Логотипы')
class TestLogo:

    @allure.title('Переход на главную по логотипу "Самокат"')
    @allure.story('Переход на главную по логотипу')
    def test_click_logo_scooter_go_to_main(self, main_page):
        main_page.click_logo_scooter()
        
        assert main_page.driver.current_url == Urls.BASE_URL


    @allure.title('Клик на логотип "Яндекс"')
    @allure.story('Переход в Дзен по логотипу "Яндекс"')
    def test_click_logo_yandex_go_to_dzen(self, main_page):
        main_window = main_page.driver.current_window_handle

        main_page.click_logo_yandex()

        WebDriverWait(main_page.driver, 10).until(
            EC.number_of_windows_to_be(2)
        )

        for window_handle in main_page.driver.window_handles:
            if window_handle != main_window:
                main_page.driver.switch_to.window(window_handle)
                break

        WebDriverWait(main_page.driver, 15).until(
            EC.url_contains("dzen")
        )

        assert "dzen" in main_page.driver.current_url


