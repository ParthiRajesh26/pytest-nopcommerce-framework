import logging
import time

from selenium import webdriver
import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



class Test_001_Login:
    baseURL =  ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger= LogGen.loggen()


    @pytest.mark.sanity
    def test_homePageTitle(self,setUp):
         self.logger.info("************  STARTED --- test_homePageTitle ************")
         self.driver = setUp
         self.driver.get(self.baseURL)
         act_title= self.driver.title
         if act_title=="nopCommerce demo store. Login":
             assert True
             self.driver.close()
             self.logger.info("********* FINISHED TEST CASE 1 **********")
         else:
             self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
             self.driver.close()
             assert False

    @pytest.mark.regression
    def test_login(self,setUp):
        self.logger.info("************  STARTED --- test_login ************")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        time.sleep(5)
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("********* FINISHED TEST CASE 2 **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("********* FAILED TEST CASE 2 **********")
            assert False




