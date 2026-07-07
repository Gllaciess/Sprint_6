import allure
import pytest
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from constants import Urls


@allure.feature('Вопросы о важном')
class TestQuestions:

    @allure.title('Проверка ответов')
    @allure.story('Проверка текста ответов')
    @pytest.mark.parametrize(
        'question_number, expected_text',
        [
            (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
            (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
            (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
            (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
            (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
            (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
            (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
            (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
        ]
    )
    def test_question_text(self, driver, question_number, expected_text):
        main_page = MainPage(driver)
        driver.get(Urls.BASE_URL)
        main_page.accept_cookies()

        main_page.click_question(question_number)
        answer_text = main_page.get_answer_text(question_number)

        assert answer_text == expected_text


