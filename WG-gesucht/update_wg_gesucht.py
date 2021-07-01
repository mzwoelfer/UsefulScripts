from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium import webdriver
import time
import json

login_data_file = "login_data.json"

with open(login_data_file, 'r') as json_file:
    login_data = json.load(json_file)


EMAIL = login_data["email"]
PASSWORD = login_data["password"]
EDIT_LINK = login_data["edit_link"]

driver = webdriver.Chrome()
driver.get('https://wg-gesucht.de')



def get_cookie_accept_button():
    return WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".cmpboxbtn.cmpboxbtnyes")))


def get_to_login_dialog():
    print("get to login dialog")
    login_button = driver.find_element_by_link_text("LOGIN")
    login_button.click()


def get_update_offer_button():
    print("get update offer button")
    return WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="update_offer"]')))

# Login Dialog
def get_login_fields():
    print("get login fields")
    email_field = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="login_email_username"]')))
    password_field = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="login_password"]')))
    return email_field, password_field


def click_login():
    print("click login")
    driver.find_element(By.XPATH, '//*[@id="login_submit"]').click()
    return


def login(email_field, password_field, email, password):
    print("login")
    email_field.send_keys(email)
    password_field.send_keys(password)
    click_login()
    return


def update_offer(edit_link):
    print("update offer")
    time.sleep(5)
    driver.get(edit_link)
    update_button = get_update_offer_button()
    update_button.click()
    print(time.strftime("Letzte Aktualisierung: %H:%M:%S"))


try:
    get_cookie_accept_button().click()
except:
    print("Error")

get_to_login_dialog()
email_field, password_field = get_login_fields()
login(email_field, password_field, EMAIL, PASSWORD)
update_offer(EDIT_LINK)

driver.quit()