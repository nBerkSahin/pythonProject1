from selenium.webdriver.common.by import By

class LoginPage():

    txtusername = "CUSTOMER_CODE"
    txtpass = "PASSWORD"
    btnlogin = "login"
    iconbasket = "icon-basket-loaded"
    cardapprove = "//*[@id='__next']/div/div/div[3]/div[2]/div/div[3]/a[2]"
    adressselect = "//*[@id='__next']/div/form/div/div/div[1]/div/div/div[2]/span[1]/label"
    completetradebtn = "//*[@class='btn btn-fill-out btn-block']"


    def __init__(self, driver):
        self.driver = driver

    def enterusername(self, username):
        self.driver.find_element(By.ID, self.txtusername).send_keys(username)

    def enterpass(self, password):
        self.driver.find_element(By.ID, self.txtpass).send_keys(password)

    def loginbtn(self):
        self.driver.find_element(By.NAME, self.btnlogin).click()

    def iconbasketbtn(self):
        self.driver.find_element(By.CLASS_NAME, self.iconbasket).click()

    def cartapprovebtn(self):
        self.driver.find_element(By.XPATH, self.cardapprove).click()

    def adressselectradio(self):
        self.driver.find_element(By.XPATH, self.adressselect).click()

    def completeTrade(self):
        self.driver.find_element(By.XPATH, self.completetradebtn).click()

