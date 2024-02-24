import unittest
from selenium import webdriver
from logic.login_page import LoginPage
from logic.channel_page import ChannelPage

class SubscribeToChannelTest(unittest.TestCase):
    def setUp(self):
        # Setup: Initializes the webdriver.
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.driver.get("https://www.youtube.com/")


    def tearDown(self):
        #Closes the browser once tests are completed
        self.driver.quit()

    def test_subscribe_to_channel(self):
        # Log in to YouTube
        self.login_page.login_flow("rasharaiyan00@gmail.com", "rasha17/2")

        #navigate to the channel
        channel_url = "https://www.youtube.com/@SimplilearnOfficial"
        self.driver.get(channel_url)
        channel_page = ChannelPage(self.driver)

        # Act: Subscribe to the channel.
        channel_page.subscribe_to_channel()

        # Assert: Verify that the subscription was successful.
        self.assertTrue(channel_page.is_subscribed(), "Subscription was not successful.")

if __name__ == "__main__":
    unittest.main()
