import unittest
from selenium import webdriver
from logic.login_page import LoginPage
from logic.video_page import VideoPage

class LikeVideoTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.driver.get("https://www.youtube.com/")
        self.login_page.login_flow("rasharaiyan00@gmail.com", "rasha17/2")

    def tearDown(self):
        self.driver.quit()

    def test_like_video(self):
        video_url = "https://www.youtube.com/watch?v=WMn_2ItCNJI"
        video_page = VideoPage(self.driver, video_url)

        video_page.like_video()
        self.assertTrue(video_page.is_video_liked(), "The video was not liked successfully.")

if __name__ == "__main__":
    unittest.main()
