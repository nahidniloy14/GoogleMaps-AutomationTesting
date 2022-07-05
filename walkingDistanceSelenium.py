from selenium import webdriver
from selenium.webdriver.common.by import By

from WalkingDistanceAPI import response1

driver = webdriver.Chrome("C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.com/maps")


class response2:
    def webResponse(APIresponse):
        driver.find_element(By.ID, "hArJGc")
        driver.find_element(By.XPATH, "//div[@class='oya4hc selected FsvUe']/button")
        driver.find_element(By.XPATH, "//div[@id='sb_ifc50']/input").send_keys("Moakhali")
        driver.find_element(By.XPATH, "//div[@id='sb_ifc51']/input").send_keys("Banani")
        message = driver.find_element(By.XPATH, "//div[@class='Fk3sm fontHeadlineSmall'] ").text
        print(message)


assert response1 == response2
