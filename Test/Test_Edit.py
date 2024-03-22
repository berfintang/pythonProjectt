from POMDocuments.HomePageObject import HomePage
from POMDocuments.LoginPageObject import LoginPage
from POMDocuments.PostPageObject import PostPage

class Test_EditPost:

    def test_EditPost(self, setup):

        self.driver = setup
        self.driver.get("https://www.blogger.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.npp = PostPage(self.driver)

        #----Login Process-----
        self.lp.clickSignIn()
        self.lp.setUserMail(self.lp.user_Mail)
        self.lp.clickMailNext()
        self.lp.setPassword(self.lp.user_Password)
        self.lp.clickPassNext()

        self.hp = HomePage(self.driver)
        self.hp.clickLatestPost()


        self.pp = PostPage(self.driver)

        self.pp.SwitchFrame_to_TextArea()


        self.pp.setText_to_TextArea("post editted ")
        self.pp.SwitchDefaultFrame()


        self.pp.clickUpdateButton()


