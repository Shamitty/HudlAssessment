from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import urllib3
from decouple import config
from behave import given, when, then


class HudlProject():

    @given('I have navigated to Hudl')
    def SetupDriver(context):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        context.driver = webdriver.Chrome("C:\\Selenium\\chromedriver")
        context.driver.maximize_window()
        context.driver.get("https://www.hudl.com")
        context.driver.implicitly_wait(10)

    @when('I click the login button')
    def MainLandingPage(context):
        assert "Hudl" in context.driver.title
        context.driver.find_element(
            By.CSS_SELECTOR, "a[data-qa-id=login]").click()

    @when('I enter my userlogin into the username field')
    def step_impl(context):
        context.driver.find_element(By.ID, "email").clear()
        context.driver.find_element(By.ID, "email").send_keys(config('USER'))

    @when('I enter my userpassword into the password field')
    def step_impl(context):
        context.driver.find_element(By.ID, "password").clear()
        context.driver.find_element(
            By.ID, "password").send_keys(config('PASS'))

    @when('I enter the wrong userpassword "{password}" into the password field')
    def step_impl(context, password):
        context.driver.find_element(By.ID, "password").clear()
        context.driver.find_element(
            By.ID, "password").send_keys(password)

    @when('I click the sign in button')
    def step_impl(context):
        context.driver.find_element(By.ID, "logIn").click()

    @then('I will see the Hudl sign screen with "{text}" logged in')
    def step_impl(context, text):
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "hui-globaluseritem__display-name")))
        assert text in context.driver.find_element(By.CLASS_NAME,
                                                   "hui-globaluseritem__display-name").text
        ActionChains(context.driver).move_to_element(context.driver.find_element(
            By.CLASS_NAME, "hui-globaluseritem__display-name")).perform()
        context.driver.find_element(
            By.CSS_SELECTOR, "a[data-qa-id=webnav-usermenu-logout]").click()

    @then('I will see a login failure warning "{text}"')
    def step_impl(context, text):
        try:

            context.driver.find_element(
                By.CLASS_NAME, "login-error fade-in-expand")
            assert text in context.driver.find_element(
                By.CSS_SELECTOR, "div[class=login-error-container]").text
        except:
            assert not(text)

    def tearDown(self):
        self.driver.quit()
