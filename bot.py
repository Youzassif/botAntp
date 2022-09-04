import time
import readline
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("/home/yayahc/Documents/CodeParrot/botais/chromedriver")
driver.get("https://www.ais-market.net/#/")

nbr_commande = 0
nbr_rembourssement = 0

def bot(number, password, nbr_commande, nbr_rembourssement):
    number_input_textbox = driver.find_element("class name","uni-input-input")
    number_input_textbox.clear()
    time.sleep(1)
    number_input_textbox.send_keys(number)

    password_input_textbox = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
    password_input_textbox.send_keys(password)
    time.sleep(2)

    login_button = driver.find_element("class name","submit-btn")
    login_button.click()
    time.sleep(2)

    #aller directement sur "clicker pour acheter"
    driver.get("https://www.ais-market.net/#/pages/refund/refund")
    time.sleep(3)
    
    try:
        item_ramboursement_button = driver.find_element("class name","item")
        item_ramboursement_button.click()
    except:
        pass
    time.sleep(3)
    try:
        buy_button = driver.find_element("class name", "info-btn")
        buy_button.click()
    except:
        pass

    time.sleep(5)
    try:
        buy_finish_button = driver.find_element("class name", "info-btn")
        buy_finish_button.click()
        time.sleep(2)
        #print("jai remboursser")
        nbr_rembourssement = nbr_rembourssement + 1
    except:
        pass

    #aller directement sur "c'est partie"
    driver.get("https://www.ais-market.net/#/pages/grabbing_detail/grabbing_detail")
    time.sleep(2.5)
    try:
        game_button = driver.find_element("class name","game-btn")
        game_button.click()
    except:
        pass
    time.sleep(8)
    try:
        sub_button = driver.find_element(By.XPATH, '//uni-button[text()="Soumettre"]')        
        sub_button.click()
        #print("jai buy")
        nbr_commande = nbr_commande + 1
        time.sleep(1)
    except:         
        pass

    #sortir
    driver.get("https://www.ais-market.net/#/")
    time.sleep(1)

    return nbr_commande, nbr_rembourssement


final_src = []
password = 'azertyuiop'
src = open("srcFinal", "r")


def data_number_reader(final_src, counter):
    return final_src[counter]
    
src_number = src.readlines()
for item in src_number:
    final_src.append(item.strip('\n'))

for i in final_src:    
    render = bot(i,password, nbr_commande, nbr_rembourssement)
    nbr_commande = nbr_commande + render[0]
    nbr_rembourssement = nbr_rembourssement + render[1]

print("jai tout fait vieux\n\n")
print("jai buy", nbr_commande, "et jai remboursser", nbr_rembourssement)
print("il me reste donc [", len(src_number)-nbr_commande, "] commandes sur", len(src_number), "et [", len(src_number)-(nbr_rembourssement), "] rembourssements sur", len(src_number))