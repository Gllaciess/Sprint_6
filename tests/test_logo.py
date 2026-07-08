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

        assert main_page.get_current_url() == Urls.BASE_URL


    @allure.title('Клик на логотип "Яндекс"')
    @allure.story('Переход в Дзен по логотипу "Яндекс"')
    def test_click_logo_yandex_go_to_dzen(self, main_page):
        main_window = main_page.get_current_window_handle()

        main_page.click_logo_yandex()

        main_page.wait_for_windows(2)

        main_page.switch_to_new_window(main_window)

        main_page.wait_for_url_contains("dzen")

        assert "dzen" in main_page.get_current_url()


