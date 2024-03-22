from POMDocuments.LoginPageObject import LoginPage

class Test_Login:
    def test_login(self,setup):
        # Setting up the driver
        self.driver = setup
        # Navigating to the website
        self.driver.get("https://www.blogger.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        # Creating an instance of LoginPage class
        self.lp = LoginPage(self.driver)
        # Clicking on the Sign In button
        self.lp.clickSignIn()
        # Setting user email
        self.lp.setUserMail(self.lp.user_Mail)
        # Clicking on the Next button after entering the email
        self.lp.clickMailNext()
        # Setting user password
        self.lp.setPassword(self.lp.user_Password)
        # Clicking on the Next button after entering the password
        self.lp.clickPassNext()