from selenium import webdriver
from POMDocuments.LoginPageObject import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import pyperclip
from time import sleep


class CommentPage:
    # Locatorlar
    post_xpath = "//article[@role='article']"
    a_comment_xpath = "//a[@class='comment-link']"
    frame_for_button_xpath = "//iframe[@id='comment-editor']"
    button_sign_in_with_google_xpath = "//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div[1]"
    txtbox_comment_xpath = "//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/div[2]/div[2]/div[1]/div[2]/textarea"
    button_publish_comment_xpath = "//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/div[2]/div[3]/div[1]/div"
    check_comments_xpath = "//li[@class='comment']"

    #variabla values

    example_comment = "basarılı"

    #methods

    def __init__(self, driver):
        self.driver = driver

    def check_post(self):
        return self.driver.find_element(By.XPATH, self.post_xpath).is_displayed()

    def add_comment(self):
        self.driver.find_element(By.XPATH, self.a_comment_xpath).click()
        self.switch_iframe()
        self.driver.find_element(By.XPATH, self.button_sign_in_with_google_xpath).click()

    def switch_iframe(self):
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, self.frame_for_button_xpath)))

    def enter_comment(self, example_comment):
        comment_box = self.driver.find_element(By.XPATH, self.txtbox_comment_xpath)
        comment_box.send_keys(example_comment)

    def publish(self):
        self.driver.find_element(By.XPATH, self.button_publish_comment_xpath).click()