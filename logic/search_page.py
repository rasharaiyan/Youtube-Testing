from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from infra.base_page import BasePage

class SearchPage(BasePage):
    SEARCH_INPUT = (By.ID, "//*[@id='search']")
    SEARCH_RESULTS = (By.ID, "//*[@id='header-contents']")

    def perform_search(self, search_query):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(search_query + Keys.RETURN)

    def search_results_are_present(self):
        return len(self.driver.find_elements(*self.SEARCH_RESULTS)) > 0
