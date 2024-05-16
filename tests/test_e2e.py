from pageobjects.CheckoutPage import Checkoutpage
from pageobjects.CofirmPage import Confirmpage
from pageobjects.HomePage import HomePage
from utilites.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("getting card titles")
       # checkoutpage = Checkoutpage(self.driver)

        cards = checkoutpage.getcardtitles()
        i = -1
        for card in cards:
           i = i + 1
           cardtext = card.text
           #log.info(cardtext)
           if cardtext == "Blackberry":
               checkoutpage.getcardfooter()[i].click()

        checkoutpage.checkoutbutton().click()

        confirmpage = checkoutpage.secondcheckout()
       # confirmpage = Confirmpage(self.driver)
        confirmpage.enter_country("ind")
        self.verifyLinkPresence("India")
        confirmpage.countryname().click()
        confirmpage.checkbox().click()
        confirmpage.purchasebutton().click()
        sucess = confirmpage.message().text
        log.info("text recived as expected")

        assert  "Success! Thank you" in sucess
        self.driver.close()



