import unittest
from selenium import webdriver
from logic.video_page import VideoPage


class PlayVideoTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_play_video(self):
        # Arrange
        video_url = "https://www.youtube.com/watch?v=WMn_2ItCNJI"
        video_page = VideoPage(self.driver, video_url)

        # Act: Attempt to play the video.
        video_page.play_video()

        # Assert: Verify that the video is playing.
        self.assertTrue(video_page.is_video_playing(), "The video did not play.")


if __name__ == "__main__":
    unittest.main()
