from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from infra.base_page import BasePage

class VideoPage(BasePage):
    LIKE_BUTTON =  (By.XPATH, "//*[@id='top-level-buttons-computed']/segmented-like-dislike-button-view-model/yt-smartimation/div/div/like-button-view-model/toggle-button-view-model/button-view-model/button/yt-touch-feedback-shape/div/div[2]")
    LIKED_BUTTON = (By.XPATH, "//*[@id='top-level-buttons-computed']/segmented-like-dislike-button-view-model/yt-smartimation/div/div/dislike-button-view-model/toggle-button-view-model/button-view-model/button/yt-touch-feedback-shape/div/div[2]")
    PLAY_BUTTON = (By.XPATH, "//*[@id='movie_player']/div[36]/div[2]/div[1]/button")
    PAUSE_BUTTON = (By.XPATH, "//*[@id='movie_player']/div[36]/div[2]/div[1]/button")
    VIDEO_PLAYER = (By.CLASS_NAME, "html5-main-video") # Checking if the video has loaded, By ensuring the video player element is present

    def __init__(self, driver, video_url):
        super().__init__(driver)
        self.driver.get(video_url)

    def like_video(self):
        like_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LIKE_BUTTON))
        like_button.click()

    def is_video_liked(self):
        # This method checks if the like button has transitioned to the "liked" state.
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.LIKED_BUTTON))
            return True
        except:
            return False

    def play_video(self):
        play_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.PLAY_BUTTON))
        play_button.click()

    def is_video_playing(self):
        # Check if the pause button is visible, which indicates the video is playing.
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PAUSE_BUTTON))
            return True
        except:
            return False