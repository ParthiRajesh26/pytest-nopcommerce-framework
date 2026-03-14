from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_Id = "Email"
    textbox_password_Id = "Password"
    login_button = "//button[text()='Log in']"
    logout_button = "//button[text()='Logout']"


    def __init__(self,driver):
        self.driver =driver

    def setUserName(self,userName):
        self.driver.find_element(By.ID, self.textbox_username_Id).clear()
        self.driver.find_element(By.ID, self.textbox_username_Id).send_keys(userName)

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_Id).clear()
        self.driver.find_element(By.ID, self.textbox_password_Id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_button).click()