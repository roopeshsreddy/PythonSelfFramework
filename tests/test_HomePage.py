import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageobjects.HomePage import HomePage
from tests.HomePageData import Homepagedata
from utilites.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self,getdata):

       homepage = HomePage(self.driver)
       homepage.Name().send_keys(getdata[0])
       homepage.Email().send_keys(getdata[1])
       homepage.Check().click()
       self.selectoptionBytext(homepage.Gender(),getdata[2])
       homepage.Submit().click()
       alertText = homepage.getsuccessmessage().text

       assert ("Success" in alertText)
       self.driver.refresh()

    @pytest.fixture(params=Homepagedata.test_Homepage_data)
    def getdata(self,request):
        return request.param
