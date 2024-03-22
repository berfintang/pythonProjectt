from time import sleep
from selenium.webdriver.common.by import By


class HomePage:
    Locator_NewPost_Xpath = "//div[@class='SpTCHb']//span[@class='MIJMVe'][normalize-space()='New Post']"
    Locator_LatestPost_Xpath = "//*[@id='yDmH0d']/c-wiz/div[2]/div/c-wiz/div[2]/c-wiz/div/div/div/div[1]/div/span/div/div/a"

    def __init__(self, driver):
        self.driver = driver

    def clickNewPost(self):
        sleep(3)
        self.driver.find_element(By.XPATH, self.Locator_NewPost_Xpath).click()


    def clickLatestPost(self):
        self.driver.find_element(By.XPATH, self.Locator_LatestPost_Xpath).click()