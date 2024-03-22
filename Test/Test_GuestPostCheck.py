from POMDocuments.GuestPageObject import GuestPage

class TestGuestPostCheck:
    def test_GuestPostCheck(self,setup):
        self.driver = setup
        self.driver.get("https://testdeneme99.blogspot.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

        # Instantiate GuestPage object
        self.GuestPagePost=GuestPage(self.driver)
        # Call the GuestPostCheck method to check guest post functionality
        self.GuestPagePost.GuestPostCheck()



