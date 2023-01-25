from playwright.sync_api import Page

from test_data.user_profile import UserProfile


class AccountDetails:
    def __init__(self, page: Page):
        self.page = page
        self.title = self.page.locator('h4.review-page--header')
        self.firstname_input = self.page.locator('input#FIRST_NAME')
        self.lastname_input = self.page.locator('input#LAST_NAME')
        self.email_input = self.page.locator('input#EMAIL')
        self.email_confirm_input = self.page.locator('input#EMAIL_CONFIRM')

    def fill_user_information(self, user: UserProfile):
        self.firstname_input.fill(user.firstname)
        self.lastname_input.fill(user.lastname)
        self.email_input.fill(user.email)
        self.email_confirm_input.fill(user.email)


class OrderPage:
    def __init__(self, page: Page):
        self.page = page
        self.model_title = self.page.locator('h1.text-loader--subtitle')
        self.continue_to_payment_button = self.page.locator('button[data-id="continue-to-payment-button"]')
        self.cash_button = self.page.locator('button#cash')
        self.creditcard_button = self.page.locator('button.btn-creditcard')

    def order_with_cash(self) -> AccountDetails:
        self.cash_button.click()
        self.creditcard_button.click()
        return AccountDetails(self.page)
