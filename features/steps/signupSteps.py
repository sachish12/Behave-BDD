from behave import *
from selenium import webdriver
import time

@given('Launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome("/Users/sash/Documents/Web Development/Challenge(Intern)/Behave/features/driver/chromedriver")


@when('Open Pointzi home page')
def openHomePage(context):
    context.driver.get("https://dashboard.pointzi.com")



@when('Click on register button')
def clickRegister(context):
    time.sleep(5)
    xpath = "//button[contains(text(),'Register')]"
    context.driver.find_element_by_xpath(xpath).click()


@when('Enter email "{email}", password "{pwd}" and confirm password "{cpwd}"')
def enterEmailAndPassword(context, email, pwd, cpwd):
    time.sleep(2)
    username = context.driver.find_element_by_name("username")
    username.send_keys(email)
    password = context.driver.find_element_by_name("password")
    password.send_keys(pwd)
    confirmPassword = context.driver.find_element_by_name("confirmPassword")
    confirmPassword.send_keys(cpwd)


@when('Click on next button')
def clickNext(context):
    xpath = "//button[@class='md-button md-primary md-raised md-button']"
    context.driver.find_element_by_xpath(xpath).click()


@when('Select the role and No of app users')
def selectRoleAndAppUsers(context):
    time.sleep(2)
    context.driver.find_element_by_name("role").click()
    time.sleep(2)
    xpathRole = "//div[contains(text(),'Developer')]"
    context.driver.find_element_by_xpath(xpathRole).click()
    context.driver.find_element_by_name("number_users").click()
    time.sleep(2)
    xpathUsersNumber = "//div[contains(text(),'0 - 50,000')]"
    context.driver.find_element_by_xpath(xpathUsersNumber).click()

@when('Click on next button 2')
def clickNext(context):
    xpath = "//button[contains(text(),'Next')]"
    context.driver.find_element_by_xpath(xpath).click()


@when('Enter firstname "{fName}", lastname "{lName}", companyname "{cName}", phone number "{phNo}" and tick on accept agreement policy')
def enterDetails(context, fName, lName, cName, phNo):
    time.sleep(5)
    firstName = context.driver.find_element_by_name("first_name")
    firstName.send_keys(fName)
    lastName = context.driver.find_element_by_name("last_name")
    lastName.send_keys(lName)
    companyName = context.driver.find_element_by_name("company_name")
    companyName.send_keys(cName)
    phoneNumber = context.driver.find_element_by_name("phone")
    phoneNumber.send_keys(phNo)
    xpath = "//div[@class='md-container']"
    context.driver.find_element_by_xpath(xpath).click()



@when('Click on Sign up button')
def clickSignup(context):
    time.sleep(3)
    xpath = "//button[contains(text(),'Sign up')]"
    context.driver.find_element_by_xpath(xpath).click()



@then('User must sucessfully login to the Dashboard page')
def verifyLogin(context):
    time.sleep(5)
    xpath = "//h2[@class='md-title']"
    text = context.driver.find_element_by_xpath(xpath).text
    assert text == "Welcome to Pointzi!"
    context.driver.close()


