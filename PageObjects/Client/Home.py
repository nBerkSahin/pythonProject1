from selenium.webdriver.common.by import By


class HomePage():

    greetings = "greeting"
    def __init__(self, driver):
        self.driver = driver

    def isGreetingDisplayed(self):
        return self.driver.find_element(By.CLASS_NAME, self.greetings).is_displayed()