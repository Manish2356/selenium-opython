import time

from selenium.webdriver.common.by import By


class SearchFlightResults(Basedriver):
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait



    def filter_flights(self,):
        driver.find_element(By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()='1']").click()
        time.sleep(6)
        all_stops = wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                    "//span[contains(text(), 'Non Stop') or contains(text(), '1 Stop') or contains(text(), '2 Stop')]")))
        print(len(all_stops))