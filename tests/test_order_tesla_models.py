import re

import pytest
from playwright.sync_api import expect, Page

from po.order_page import OrderPage
from po.tesla_main_page import TeslaMainPage
from test_data.test_data import TeslaModels
from test_data.user_profile import new_user


@pytest.mark.parametrize("model, url", [(TeslaModels.MODEL_S, '/models'),
                                        (TeslaModels.MODEL_3, '/model3'),
                                        (TeslaModels.MODEL_X, '/modelx'),
                                        (TeslaModels.MODEL_Y, '/modely'),
                                        ("Not exist model", '/modely')]
                         )
def test_order_tesla_model(page: Page, model, url):
    """Test check ordering the car but is not finished. It contains one always filed test"""
    page.set_default_timeout(timeout=5000)

    tesla_page = TeslaMainPage(page)
    order_page = OrderPage(page)

    tesla_page.navigate()
    tesla_page.close_location_country_dialog()

    tesla_page.open_category(model)
    expect(tesla_page.section_title).to_have_text(model, timeout=20000)
    expect(page).to_have_url(re.compile(url))

    tesla_page.order_now_button.click(timeout=10000)
    expect(order_page.model_title).to_have_text(model, timeout=10000)

    order_page.continue_to_payment_button.click()
    order_page \
        .order_with_cash() \
        .fill_user_information(new_user)
