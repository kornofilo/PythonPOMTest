from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path="C:/Users/r-2g-/PycharmProjects/untitled/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
driver.find_element_by_id("welcome").click()
driver.find_element_by_id("Logout").click()
time.sleep(2)
