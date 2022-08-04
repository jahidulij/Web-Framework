import pytest
import unittest
from pages.home.login_page_pom_basepage import LoginPageVerifyBasePage
from utilities.teststatus import StatusTest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPageVerifyBasePage(self.driver)
        self.ts = StatusTest(self.driver)

    @pytest.mark.invalid
    def test_invalidLogin(self):
        self.lp.login("jahid@email.com", "pqa1234")
        login_result = self.lp.verfyLoginFailed()
        assert login_result == True

    @pytest.mark.valid
    def test_validLogin(self):
        self.lp.login("jahid@email.com", "pqa123")
        login_result1 = self.lp.verifyLoginTitle()
        self.ts.mark(login_result1, "Title is incorrect")

        login_result2 = self.lp.verfyLoginSuccessful()
        self.ts.markFinal("test_validLogin", login_result2, "Login was unsuccessful")





