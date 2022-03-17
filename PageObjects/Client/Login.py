from selenium.webdriver.common.by import By

class LoginPage():

    txtusername = "CUSTOMER_CODE"
    txtpass = "PASSWORD"
    btnlogin = "login"

    def __init__(self, driver):
        self.driver = driver

    def enterusername(self, username):
        self.driver.find_element(By.ID, self.txtusername).send_keys(username)

    def enterpass(self, password):
        self.driver.find_element(By.ID, self.txtpass).send_keys(password)

    def loginbtn(self):
        self.driver.find_element(By.NAME, self.btnlogin).click()
