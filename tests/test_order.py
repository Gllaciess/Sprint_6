import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from constants import Urls, Data


@allure.feature('Заказ самоката')
class TestOrder:

    @allure.title('Позитивный сценарий заказа самоката')
    @allure.story('Позитивный сценарий заказа')
    @pytest.mark.parametrize(
        'order_data, button_type',
        [
            (Data.ORDER_DATA_1, 'top'),
            (Data.ORDER_DATA_2, 'bottom')
        ]
    )
    def test_order_successful(self, driver, order_data, button_type):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        driver.get(Urls.BASE_URL)
        main_page.accept_cookies()

        if button_type == 'top':
            main_page.click_order_top()
        else:
            main_page.click_order_bottom()

        order_page.fill_order_form_1(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"]
        )

        order_page.fill_order_form_2(
            order_data["delivery_date"],
            order_data["rental_period"],
            order_data["color"],
            order_data.get("comment")
        )

        assert "Заказ оформлен" in order_page.get_success_message()


