from time import sleep
import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

menu_page = 'http://127.0.0.1:5500/FrontEnd/templates/menu.html'
scenarios('../features/choose_menu.feature')

@pytest.fixture
def browser():
  # webdriver_options = webdriver.ChromeOptions()
  # webdriver_options.add_argument('--headless')
  # browse = webdriver.Chrome(options=webdriver_options)
  browser = webdriver.Chrome()
  browser.implicitly_wait(50)
  yield browser
  browser.quit()

@given('that i am already on menu page')
def login(browser):
  browser.get(menu_page)

@when('i click on some dishes')
def moving_to_tables_page(browser):
#   sleep(5)
#   arr = browser.find_elements(By.CLASS_NAME, 'btn-dark')
#   for each in arr:
#     each.click()
#   sleep(5)
  browser.find_element(By.ID, '1').click()
  browser.find_element(By.ID, '2').click()
  browser.find_element(By.ID, '3').click()
  browser.find_element(By.ID, '4').click()

@then('add more quantity of dishes')
def add_money(browser):
  browser.find_element(By.ID, 'plus-2').click()
  browser.find_element(By.ID, 'plus-2').click()
  browser.find_element(By.ID, 'plus-2').click()
  browser.find_element(By.ID, 'plus-4').click()
  browser.find_element(By.ID, 'plus-4').click()
  browser.find_element(By.ID, 'plus-3').click()
  browser.find_element(By.ID, 'plus-3').click()

@then('i should be able to proceed and it should move me to checkout page')
def check_money_added(browser):
  browser.find_element(By.ID, 'proceedToCheckoutID').click()
  checkout = browser.find_element(By.XPATH, '/html/body/div/div/h1')
  assert checkout.text == "Checkout"