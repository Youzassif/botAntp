import time
import readline
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("/home/yayahc/Documents/CodeParrot/botAntp/chromedriver")
driver.get("")

def bot(number, password):
    #sign
    number_input_textbox = driver.find_element(By.CSS_SELECTOR, 'input[type="tel"]')
    number_input_textbox.send_keys(number)
    password_input_textbox = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
    password_input_textbox.send_keys(password)
    confirm_password_input_textbox = driver.find_element(By.XPATH, "//input[@placeholder='Confirmer votre mot de passe']")
    confirm_password_input_textbox.send_keys(password)
    login_button = driver.find_element("class name","van-button__content")
    login_button.click()
    time.sleep(2)

    #do task
    

src = []
password = 'azertyuiop'
src_file = open("src_file", "r")

src_number = src_file.readlines()
for item in src_number:
    src.append(item.strip('\n'))

for number_item in src:    
    bot (number_item,password)