from behave import when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup Selenium driver (adjust as needed for your environment)
driver = webdriver.Chrome()  # Make sure chromedriver is in PATH

# ---------------- 7a: Button Click ----------------
@when('I click the button with id "{button_id}"')
def step_click_button(context, button_id):
    button = driver.find_element(By.ID, button_id)
    button.click()


# ---------------- 7b: Verify text is present ----------------
@then('I should see the text "{expected_text}" on the page')
def step_verify_text_present(context, expected_text):
    body = driver.find_element(By.TAG_NAME, "body").text
    assert expected_text in body, f'"{expected_text}" not found on page'


# ---------------- 7c: Verify text is NOT present ----------------
@then('I should not see the text "{unexpected_text}" on the page')
def step_verify_text_not_present(context, unexpected_text):
    body = driver.find_element(By.TAG_NAME, "body").text
    assert unexpected_text not in body, f'"{unexpected_text}" should not be on page'


# ---------------- 7d: Verify a specific message is present ----------------
@then('I should see the message "{expected_message}"')
def step_verify_message(context, expected_message):
    body = driver.find_element(By.TAG_NAME, "body").text
    assert expected_message in body, f'Message "{expected_message}" not found'
