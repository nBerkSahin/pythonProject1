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

@when('I click add to cart button')
def step_impl(context):
    home = Login.LoginPage(context.driver)
    home.iconbasketbtn()
    time.sleep(4)

@when('I go to cart page')
def step_impl(context):
    context.driver.get("http://35.158.94.191:3000/other/sepet")
    time.sleep(4)

@when('I click cartapprove button')
def step_impl(context):
    home = Login.LoginPage(context.driver)
    home.cartapprovebtn()
    time.sleep(4)

@when('I click adresselect button')
def step_impl(context):
    home = Login.LoginPage(context.driver)
    home.adressselectradio()
    time.sleep(4)

@when('I click completetrade button')
def step_impl(context):
    home = Login.LoginPage(context.driver)
    home.completeTrade()
    time.sleep(30)