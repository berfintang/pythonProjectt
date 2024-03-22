from POMDocuments.LoginPageObject import LoginPage
from POMDocuments.CommentPageObject import CommentPage
from POMDocuments.GuestPageObject import GuestPage
from time import sleep


class TestComment:

       def test_guestpostcomment(self, setup):
              self.driver = setup
              self.driver.get("https://testdeneme99.blogspot.com/")
              self.driver.maximize_window()
              self.driver.implicitly_wait(15)

              self.lp = LoginPage(self.driver)
              self.cp = CommentPage(self.driver)

              # Click on add comment
              self.cp.add_comment()
              sleep(3)

              # Perform Google sign-in steps
              self.lp.setUserMail(self.lp.guest_Mail)
              sleep(3)
              self.lp.clickMailNext()
              sleep(3)
              self.lp.setPassword(self.lp.guest_Password)
              sleep(3)
              self.lp.clickPassNext()

              # Switch back to iframe
              self.cp.switch_iframe()
              sleep(3)

              # Enter the comment and publish
              self.cp.enter_comment(self.cp.example_comment)
              sleep(3)
              self.cp.publish()

