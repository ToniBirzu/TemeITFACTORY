import time

from selenium import webdriver
from selenium.webdriver.common.by import By

### Part 1
chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")

first_name_field = chrome.find_element(By.ID, "first-name")
first_name_field.send_keys("Vlad")

first_name_field = chrome.find_element(By.CSS_SELECTOR, "#first-name")
first_name_field.send_keys("Mirel")

submit = chrome.find_element(By.LINK_TEXT, "Submit")
submit.click()

key = chrome.find_element(By.PARTIAL_LINK_TEXT, "Key")
key.click()

chrome.get("https://the-internet.herokuapp.com/login")
username_field = chrome.find_element(By.NAME, "username")
username_field.send_keys("Toni")

chrome.get("https://formy-project.herokuapp.com/form")
input_field = chrome.find_element(By.TAG_NAME, "input")[1]
input_field.send_keys("Birzu")

first_name_field = chrome.find_element(By.CLASS_NAME, "form-control")
first_name_field.clear()
first_name_field.send_keys("Mihai")

first_name_field = chrome.find_element(By.CSS_SELECTOR, ".form-control")
first_name_field.send_keys("Gelucu")

first_name_field = chrome.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name'").send_keys("Alin")

time.sleep(5)

### Part 2

chrome = webdriver.Chrome()
chrome.get("https://phptravels.net/")

autocomplete_field = chrome.find_element(By.ID, "autocomplete")
autocomplete_field.send_keys("Rio")

first_name_field = chrome.find_element(By.CSS_SELECTOR, "#autocomplete")
autocomplete_field.clear()
first_name_field.send_keys("San Pedro")


chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/")
checkbox = chrome.find_element(By.LINK_TEXT, "Checkbox")
checkbox.click()

key = chrome.find_element(By.PARTIAL_LINK_TEXT, "Key")
key.click()

chrome.get("https://phptravels.net/")
from_field = chrome.find_element(By.NAME, "from")
from_field.send_keys("Dublin")


chrome.get("https://phptravels.net/hotels")
input_field = chrome.find_element(By.TAG_NAME, "input")
input_field.send_keys("Checkin")

chrome.get("https://phptravels.net/flights")
first_name_field = chrome.find_element(By.CLASS_NAME, "form-control").send_keys("Frankfurt")

flying_field = chrome.find_element(By.CSS_SELECTOR, ".form-control")
flying_field.send_keys("Dubai")

chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")

job_field = chrome.find_element(By.CSS_SELECTOR, "input[placeholder = 'Enter your job title'").send_keys("Guvernator")


### Part 3

chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")

date_field = chrome.find_element(By.ID, "datepicker")
date_field.send_keys("17 10 2023")


date_field = chrome.find_element(By.CSS_SELECTOR, "#datepicker")
date_field.clear()
date_field.send_keys("21 05 2023")


chrome.get("https://formy-project.herokuapp.com/")
dropdown = chrome.find_element(By.LINK_TEXT, "Dropdown")
dropdown.click()


chrome.get("https://the-internet.herokuapp.com/")
java_link = chrome.find_element(By.PARTIAL_LINK_TEXT, "Java")
java_link.click()

chrome.get("https://the-internet.herokuapp.com/login")
login_page = chrome.find_element(By.NAME, "password")
login_page.send_keys("123456")



chrome.get("https://the-internet.herokuapp.com/login")
input_field = chrome.find_element(By.TAG_NAME, "input")
input_field.send_keys("Toni")


chrome.get("https://formy-project.herokuapp.com/enabled")
input_here = chrome.find_element(By.CLASS_NAME, "form-control")
input_here.send_keys("alabala")




chrome.get("https://phptravels.net/login")
mail_field = chrome.find_element(By.CSS_SELECTOR, ".form-control")
mail_field.send_keys("alabala@yahoo.com")



chrome.get("https://phptravels.net/login")
password_field = chrome.find_element(By.CSS_SELECTOR, "input[placeholder = 'Password'").send_keys("mypassword")













