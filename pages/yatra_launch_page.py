import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.base_driver import BaseDriver


class LaunchPage():
    def __init__(self, driver, wait):
        # super.__init__(driver)
        self.driver = driver
        self.wait = wait

    def departfrom(self,departlocation):
           depart_from = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
           depart_from.click()
           depart_from.send_keys(departlocation)
           depart_from.send_keys(Keys.ENTER)

    def goingto(self,destination):
        going_to = self.wait.until(EC.element_to_be_clickable((By.XPATH , "//input[@id='BE_flight_arrival_city']")))
        going_to.click()
        time.sleep(2)
        going_to.send_keys(destination)
        time.sleep(2)


        search_res = self.wait.until(EC.presence_of_all_elements_located((By.XPATH , "//div[@class='viewport']//div[1]/li")))

        for results in search_res:
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(3)
                break


    def selectdate(self,departuredate):


        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        time.sleep(3)

        all_dates = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"))).find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")

        for dates in all_dates:
            if dates.get_attribute("data-date") == departuredate:
                dates.click()
                time.sleep(3)
                break



    def clicksearch(self):
           self.driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()
           time.sleep(3)
