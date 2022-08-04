import time
import utilities.custom_logger as cl
import logging

from base.basepage import BasePage

class LoginPageVerifyBasePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link_xpath = "//a[contains(text(),'Sign In')]"
    _email_field_id = "email"
    _password_field_id = "password"
    _login_button_xpath = "//input[@value='Login']"
    _login_success_verify_xpath = "//*[@id='dropdownMenu1']/img"
    _login_failed_verify_xpath = "//*[@id='page']/div[2]/div/div/div/div/form/div[1]/span"

    # Actions
    def clickLoginLink(self):
        self.elementClick(self._login_link_xpath, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field_id, locatorType="id")

    def enterPassword(self, password, locatorType="id"):
        self.sendKeys(password, self._password_field_id)

    def clickLoginButton(self):
        self.elementClick(self._login_button_xpath, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        # time.sleep(2)
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        # time.sleep(2)
        self.clickLoginButton()

    def clearFields(self):
        self.clearFieldsData(self._email_field_id, locatorType="id")
        self.clearFieldsData(self._password_field_id, locatorType="id")
        # emailField = self.getElement(locator=self._email_field_id, locatorType="id")
        # emailField.clear()
        # passwordField = self.getElement(locator=self._password_field_id, locatorType="id")
        # passwordField.clear()

    def verfyLoginSuccessful(self):
        login_result = self.isElementPresent(self._login_success_verify_xpath, locatorType="xpath")
        return login_result

    def verfyLoginFailed(self):
        login_result = self.isElementPresent(self._login_failed_verify_xpath, locatorType="xpath")
        return login_result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("My Courses")
