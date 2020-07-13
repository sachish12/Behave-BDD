from behave import *
from selenium import webdriver
import time

@given('I launch Chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome("/Users/sash/Documents/Web Development/Challenge(Intern)/Behave/features/driver/chromedriver")


@when('I open Pointz Homepage')
def openHomePage(context):
    context.driver.get("https://dashboard.pointzi.com")


@when('Enter username "{email}" and password "{pwd}"')
def enterUsernameAndPassword(context, email, pwd):
    time.sleep(5)
    context.driver.find_element_by_id('input_1').send_keys(email)
    context.driver.find_element_by_xpath("//input[@id='input_2']").send_keys(pwd)


@when('click on login button')
def clickLogin(context):
    context.driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()


@then('Uses/r must successfully login to the Dashboard page')
def verifyLogin(context):
    time.sleep(5)
    text = context.driver.find_element_by_xpath("//p[contains(text(),'Experiments')]").text
    assert text == "EXPERIMENTS"
    context.driver.close()

