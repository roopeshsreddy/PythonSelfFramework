from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Confirmpage:
    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.ID, "country")
    test_loc = (By.ID,"country" )
    # self.driver.find_element(By.LINK_TEXT, "India")
    country_name = (By.LINK_TEXT, "India")
    #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    check_box = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    #self.driver.find_element(By.CSS_SELECTOR,"input[class='btn btn-success btn-lg']")
    purchase_button =(By.CSS_SELECTOR,"input[class='btn btn-success btn-lg']")
    #self.driver.find_element(By.CLASS_NAME, "alert-success").text
    msg = (By.CLASS_NAME, "alert-success")


    def testloc(self):
        return self.driver.find_element(*Confirmpage.test_loc)

    def enter_country(self, text):
        self.testloc().send_keys(text)

    def countryname(self):
        #return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.country_name))
        return self.driver.find_element(*Confirmpage.country_name)
    def checkbox(self):
        return self.driver.find_element(*Confirmpage.check_box)
    def purchasebutton(self):
        return self.driver.find_element(*Confirmpage.purchase_button)
    def message(self):
        return self.driver.find_element(*Confirmpage.msg)
