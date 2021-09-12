from behave import *
from selenium import webdriver
import OrangeHRMsteps


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element_by_css_selector("input[name='txtUsername']").send_keys(user)
    context.driver.find_element_by_css_selector("input[name='txtPassword']").send_keys(pwd)

@when('I click on login button')
def step_impl(context):
    context.driver.find_element_by_css_selector("input[name='Submit']").click()


@then('user must successfully login to the dashboard page')
def step_impl(context):
    text = context.driver.find_element_by_xpath("//b[contains(text(),'Dashboard')]").text
    assert text == "Dashboard"
    context.driver.close()



