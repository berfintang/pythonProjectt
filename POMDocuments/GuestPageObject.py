from selenium.webdriver.common.by import By
from time import sleep
class GuestPage:
    # Locator for the post element
    Locator_PostID="FeaturedPost1"

    def __init__(self,driver):
        self.driver=driver
    # Method to check if guest post exists
    def GuestPostCheck(self):
        sleep(3)
        # Find all elements with the specified ID
        PostList=self.driver.find_elements(By.ID,self.Locator_PostID)

        # If there are no elements with the specified ID, assert False
        if not PostList:
            assert False  # There are no posts
        else:
            assert True  # There is at least one  post



