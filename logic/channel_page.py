from selenium.webdriver.common.by import By
from infra.base_page import BasePage

class ChannelPage(BasePage):
    SUBSCRIBE_BUTTON = (By.XPATH, "//*[@id='subscribe-button']/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
    SUBSCRIBED_STATUS = (By.XPATH, "//*[@id='notification-preference-button']/ytd-subscription-notification-toggle-button-renderer-next/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")

    def __init__(self, driver, channel_url):
        super().__init__(driver)
        self.driver.get(channel_url)

    def subscribe_to_channel(self):
        subscribe_button = self.find_element(*self.SUBSCRIBE_BUTTON)
        if subscribe_button:
            subscribe_button.click()
            return True
        return False

    def is_subscribed(self):
        try:
            # Waiting for the "Subscribed" status to be visible 
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.SUBSCRIBED_STATUS)
            )
            return True
        except TimeoutException:
            return False

