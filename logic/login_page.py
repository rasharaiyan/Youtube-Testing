from selenium.webdriver.common.by import By
from infra.base_page import BasePage

class LoginPage(BasePage):
    SIGNIN_BUTTON = "//*[@id='buttons']/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]"
    EMAIL_INPUT = "//input[@type='email']"
    NEXT_BUTTON = "//*[@id='identifierNext']/div/button"
    PASSWORD_INPUT = "//input[@type='password']"
    SUBMIT_BUTTON = "//*[@id='passwordNext']/div/button/div[3]"

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_sign_in_button(self):
        signin_button = self.driver.find_element(By.XPATH, self.SIGNIN_BUTTON)
        signin_button.click()

    def fill_username_input(self, email):
        email_input = self.driver.find_element(By.XPATH, self.EMAIL_INPUT)
        email_input.send_keys(email)

    def click_on_next_button(self):
        next_button = self.driver.find_element(By.XPATH, self.NEXT_BUTTON)
        next_button.click()

    def fill_password_input(self, password):
        password_input = self.driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        password_input.send_keys(password)

    def click_on_submit_button(self):
        submit_button = self.driver.find_element(By.XPATH, self.SUBMIT_BUTTON)
        submit_button.click()

    def profile_name_is_visible(self):
        profile_name = self.driver.find_element(By.XPATH, "//*[@id='account-name']")
        return profile_name.is_displayed()

    def login_flow(self, email, password):
        self.click_on_sign_in_button()
        self.fill_username_input(email)
        self.click_on_next_button()
        self.fill_password_input(password)
        self.click_on_submit_button()
