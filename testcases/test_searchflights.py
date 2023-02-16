import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.yatra_launch_page import LaunchPage


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():
    def test_search_flights(self):


        #Launching the browser and opening the travel website
        #provide going from information
        lp = LaunchPage(self.driver , self.wait)
        lp.departfrom("New Delhi")

        #provide going to  information
        lp.goingto("New York")
        #sync issues
        #select the departure date
        lp.selectdate('15/02/2023')
        #click on button search flight
        lp.clicksearch()
        #dynamic scroll
        lp.page_scroll()



        #click on filter 1 stop
        driver.find_element(By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()='1']").click()
        time.sleep(6)
        all_stops = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[contains(text(), 'Non Stop') or contains(text(), '1 Stop') or contains(text(), '2 Stop')]")))
        print(len(all_stops))

        #TO verify that the filter is working only to 1 stop
        for stop in all_stops:
            print("The text is : "+stop.text)
            assert stop.text == "1 Stop"
            print("assert pass")


