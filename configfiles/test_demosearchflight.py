# # import time
# # import pytest
# # from selenium import webdriver
# # from selenium.webdriver import Keys
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.wait import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
#
# #from selenium.webdriver.support.ui import WebDriverWait
#
# import ...
# import pytest
#
#
#
# @pytest.mark.usefixtures("setup")
# class TestSearchAndVerifyFilter():
#     def test_search_flights(self):
#
#         #Launching the browser and opening the travel website
#
#
#         #provide going from information
#         departfrom = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
#         departfrom.click()
#         departfrom.send_keys("New Delhi")
#         departfrom.send_keys(Keys.ENTER)
#
#         # provide going to  information
#         goingto = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
#         goingto.click()
#         time.sleep(3)
#         goingto.send_keys("New York")
#         time.sleep(3)
#         search_results = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div[1]/li")))
#         print(len(search_results))
#
#         for result in search_results:
#             if "New York (JFK)" in result.text:
#                 result.click()
#                 break
#
#
#         #sync issues
#         self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
#         time.sleep(3)
#         # driver.find_element(By.XPATH, "//td[@id='08/03/2023']").click()
#         # time.sleep(3)
#         all_dates = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")))
#
#         #select the departure date
#         for dates in all_dates:
#             if dates.get_attribute("data-date") == "08/03/2023":
#                 dates.click()
#                 time.sleep(3)
#                 break
#
#         #click on button search flight
#         driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()
#         time.sleep(3)
#
#
#         #click on filter 1 stop
#         driver.find_element(By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()='1']").click()
#         time.sleep(6)
#         all_stops = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[contains(text(), 'Non Stop') or contains(text(), '1 Stop') or contains(text(), '2 Stop')]")))
#         print(len(all_stops))
#
#         #TO verify that the filter is working only to 1 stop
#         for stop in all_stops:
#             print("The text is : "+stop.text)
#             assert stop.text == "1 Stop"
#             print("assert pass")
#
#
