import time
import readline
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome("/home/yayahc/Documents/CodeParrot/botAntp/chromedriver",chrome_options=chrome_options)
driver.get("https://www.antp.io/#/register?inviteCode=661435")

def bot(number, password):

    #login
    driver.get("https://www.antp.io/#/login")
    time.sleep(4)
    log_number_input_textbox = driver.find_element(By.XPATH, "//input[@placeholder='Veuillez saisir votre numéro de téléphone']")
    log_number_input_textbox.send_keys(number)
    log_password_input_textbox = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
    log_password_input_textbox.send_keys(password)
    login_button = driver.find_element("class name","login-btn")
    login_button.click()
    time.sleep(15)

    #do task ... a revoir
    driver.get("https://www.antp.io/#/minhas")  
    time.sleep(7)
    

src = []
password = 'azertyuiop'
src_file = open("do", "r")

src_number = src_file.readlines()
for item in src_number:
    src.append(item.strip('\n'))

for number_item in src:    
    bot (number_item,password)