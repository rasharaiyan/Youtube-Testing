import unittest
from selenium import webdriver
from logic.login_page import LoginPage
#login tests
class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.youtube.com/")
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_with_current_email_and_wrong_password(self):
        self.login_page.login_flow("rasharaiyan00@gmail.com", "wrongpassword")

    def test_login_with_wrong_email_and_current_password(self):
        self.login_page.login_flow("wrongemail@gmail.com", "rasha17/2")

    def test_login_with_current_email_and_current_password(self):
        self.login_page.login_flow("rasharaiyan00@gmail.com", "rasha17/2")
        self.assertTrue(self.login_page.profile_name_is_visible())

if __name__ == "__main__":
    unittest.main()
