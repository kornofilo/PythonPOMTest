from selenium import webdriver
import time
import unittest
from SampleProjects.POMProjectDemo.Pages.loginPage import LoginPage
from SampleProjects.POMProjectDemo.Pages.homePage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path="C:/Users/r-2g-/PycharmProjects/untitled/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)

        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        assert()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        assert ()
        time.sleep(2)

        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("tests completed")



