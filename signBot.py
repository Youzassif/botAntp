import time
import readline
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome("/home/yayahc/Documents/CodeParrot/botAntp/chromedriver",chrome_options=chrome_options)
driver.get("https://www.antp.io/#/register?inviteCode=663615")

def bot(number, password):
    #sign
    number_input_textbox = driver.find_element(By.CSS_SELECTOR, 'input[type="tel"]')
    number_input_textbox.send_keys(number)
    password_input_textbox = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
    password_input_textbox.send_keys(password)
    confirm_password_input_textbox = driver.find_element(By.XPATH, "//input[@placeholder='Confirmer votre mot de passe']")
    confirm_password_input_textbox.send_keys(password)
    sign_button = driver.find_element("class name","login-btn")
    sign_button.click()
    time.sleep(2)

    #exit
    driver.get("https://www.antp.io/#/register?inviteCode=663615")
    time.sleep(1)
    

src = []
password = 'azertyuiop'
src_file = open("src_file", "r")

src_number = src_file.readlines()
for item in src_number:
    src.append(item.strip('\n'))

for number_item in src:    
    bot (number_item,password)
    print("ok je l'ai")