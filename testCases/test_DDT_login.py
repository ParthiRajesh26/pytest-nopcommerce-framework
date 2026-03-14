import logging
import time

from selenium import webdriver
import pytest
from utilities import XLUtils

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_002_ddt_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"

    logger = LogGen.loggen()
    list_status = []

    def test_ddt_login(self, setUp):
        self.logger.info("************  STARTED --- test_ddt_login ************")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.row= XLUtils.get_row_count(self.path,"Sheet1")



        for r in range(2,self.row+1):
            self.username =XLUtils.read_data(self.path,"Sheet1",r,1)
            self.password = XLUtils.read_data(self.path,"Sheet1",r,2)
            self.result = XLUtils.read_data(self.path,"Sheet1",r,3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.result=="pass":
                    self.logger.info("**** Passed ****")
                    self.lp.clickLogout()
                    self.list_status.append("pass")

                elif self.result=="fail":
                    self.logger.info("**** Failed ****")
                    self.lp.clickLogout()
                    self.list_status.append("fail")

            elif  act_title!=exp_title:
                if self.result=="pass":
                    self.logger.info("**** Failed ****")
                    self.list_status.append("fail")
                elif self.result=="fail":
                    self.logger.info("**** Passed ****")
                    self.list_status.append("pass")

        if "fail" not in self.list_status:
                self.logger.info("Login DDT test passed")
                self.driver.close()
                assert True
        else:
                self.logger.info("Login DDT test failed")
                self.driver.close()
                assert False

        self.logger.info("END DDT TEST")










