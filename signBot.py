from lib2to3.pgen2 import token
import time
import readline
from selenium import webdriver
from selenium.webdriver.common.by import By
from number_generator import generator

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome("/home/yayahc/Documents/CodeParrot/botAntp/chromedriver",chrome_options=chrome_options)

def bot(number, password, mytoken):
    driver.get(f"https://www.antp.io/#/register?inviteCode={mytoken}")
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
    driver.get(f"https://www.antp.io/#/register?inviteCode={mytoken}")
    time.sleep(1)
    

src = []
password = 'azertyuiop'

final_token = []
token = open("token", "r")
mytoken = token.readlines()[0]
for item in mytoken:
    final_token.append(item.strip('\n'))
    
src = generator(10)
for number_item in src:    
    bot (number_item,password, mytoken)

print("ok je l'ai")