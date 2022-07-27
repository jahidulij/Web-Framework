import pytest
import unittest
from pages.home.login_page_pom_multi_assert import LoginPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.invalid
    def test_invalidLogin(self):
        self.lp.login("jahid@email.com", "pqa1234")
        login_result = self.lp.verifyLoginFailed()
        assert login_result == True

    @pytest.mark.valid
    def test_validLogin(self):
        self.lp.login("jahid@email.com", "pqa123")
        login_result1 = self.lp.verifyLoginSuccessful()
        assert login_result1 == True
        login_result2 = self.lp.verifyTitle()
        assert login_result2 == True
