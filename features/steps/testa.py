import time
import pytest

from behave import *
from utilities import configReader
from PageObjects.Client import Login
from PageObjects.Client import Home
from selenium.webdriver import Chrome



@given(u'I navigate to login page')
def step_impl(context):
    context.driver = Chrome("/Users/nazmiberksahin/PycharmProjects/pythonProject1/chromedriver")
    context.driver.maximize_window()
    context.driver.get("http://35.158.94.191:3000/other/giris")


@when('I enter username as "{username}"')
def step_impl(context, username):
    home = Login.LoginPage(context.driver)
    home.enterusername(username)

@when('I enter password as "{password}"')
def step_impl(context, password):
    home = Login.LoginPage(context.driver)
    home.enterpass(password)


@when('I click login button')
def step_impl(context):
    home = Login.LoginPage(context.driver)
    home.loginbtn()
    time.sleep(4)

@then('I check my login')
def step_impl(context):
    home = Home.HomePage(context.driver)
    assert home.isGreetingDisplayed()
    time.sleep(4)