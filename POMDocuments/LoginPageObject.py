from selenium.webdriver.common.by import By
from time import sleep

class LoginPage:

    #-----Locators-----
    Locator_SignIn_CSS = "a[class='sign-in ga-header-sign-in'] span"
    Locator_UserMail_ID = "identifierId"
    Locator_UserPassword_Name = "Passwd"
    Locator_User_Next_Button_ID = "identifierNext"
    Locator_Password_Next_Button_ID = "passwordNext"
    Locator_GuestMail = "identifier"


    #-----Variable_Values----

    user_Mail = "ototest61@gmail.com"
    user_Password = "testDeneme9."


    guest_Mail = "ototest61@gmail.com"
    guest_Password = "testDeneme9."


    #-----Methods-----
    def __init__(self,driver):
        self.driver=driver

    # Method to set user mail
    def setUserMail(self,mail):
        sleep(3)
        userMailtxt=self.driver.find_element(By.ID,self.Locator_UserMail_ID)
        userMailtxt.clear()
        userMailtxt.send_keys(mail)

    # Method to set password
    def setPassword(self,password):
        sleep(3)
        passwordtxt=self.driver.find_element(By.NAME,self.Locator_UserPassword_Name)
        passwordtxt.clear()
        passwordtxt.send_keys(password)

    # Method to click on Sign In button
    def clickSignIn(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,self.Locator_SignIn_CSS).click()

    # Method to click on Mail Next button
    def clickMailNext(self):
        sleep(3)
        self.driver.find_element(By.ID,self.Locator_User_Next_Button_ID).click()

    # Method to click on Password Next button
    def clickPassNext(self):
        sleep(3)
        self.driver.find_element(By.ID, self.Locator_Password_Next_Button_ID).click()

