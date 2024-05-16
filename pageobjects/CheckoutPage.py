from selenium.webdriver.common.by import By

from pageobjects.CofirmPage import Confirmpage


class Checkoutpage:
    #mobiles = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    def __init__(self, driver):
        self.driver = driver
    card_title = (By.XPATH, "//div[@class='card h-100']")
    #find_element(By.XPATH, "div/button")
    card_footer = (By.XPATH, "div/button" )
    #driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']" )
    #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
    second_checkout = (By.XPATH, "//button[@class='btn btn-success']" )



    def getcardtitles(self):
        return self.driver.find_elements(*Checkoutpage.card_title)

    def getcardfooter(self):
        return self.driver.find_element(*Checkoutpage.card_footer)

    def checkoutbutton(self):
        return self.driver.find_element(*Checkoutpage.checkout_button)

    def secondcheckout(self):
        self.driver.find_element(*Checkoutpage.second_checkout).click()
        confirmpage = Confirmpage(self.driver)
        return confirmpage
