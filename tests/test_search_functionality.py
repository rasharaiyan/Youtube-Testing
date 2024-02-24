import unittest
from selenium import webdriver
from logic.search_page import SearchPage

class SearchFunctionalityTest(unittest.TestCase):
    def setUp(self):
        # Setup: Initializes the webdriver and navigates to the YouTube homepage.
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.youtube.com/")
        self.search_page = SearchPage(self.driver)

    def tearDown(self):
        # Teardown: Closes the browser once tests are completed.
        self.driver.quit()

    def test_search_for_a_video(self):

        # Act: Perform a search on YouTube.
        self.search_page.perform_search("Selenium WebDriver")

        # Assert: Verify that search results are present.
        self.assertTrue(self.search_page.search_results_are_present())

if __name__ == "__main__":
    unittest.main()
