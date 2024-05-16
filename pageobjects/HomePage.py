from selenium.webdriver.common.by import By

from pageobjects.CheckoutPage import Checkoutpage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name = 'name'")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    successMessage = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = Checkoutpage(self.driver)
        return checkoutpage
    def Name(self):
        return self.driver.find_element(*HomePage.name)

    def Email(self):
        return self.driver.find_element(*HomePage.email)

    def Check(self):
        return self.driver.find_element(*HomePage.check)

    def Gender(self):
        return self.driver.find_element(*HomePage.gender)

    def  Submit(self):
        return self.driver.find_element(*HomePage.submit)

    def getsuccessmessage(self):
        return self.driver.find_element(*HomePage.successMessage)
