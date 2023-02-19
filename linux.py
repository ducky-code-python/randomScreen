from selenium import webdriver
import string
import random
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
photos = 0
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def stworzLink():
    string.ascii_letters1 = '12345'
    string.ascii_letters2 = '12345'
    string.ascii_letters3 = 'abcdefghijklmnopqrstuvw'
    string.ascii_letters4 = 'abcdefghijklmnopqrstuvw'
    string.ascii_letters5 = 'abcdefghijklmnopqrstuvw'
    string.ascii_letters6 = 'abcdefghijklmnopqrstuvw'
    string.ascii_letters7 = 'abcdefghijklmnopqrstuvw'
    pierwszaLitera = random.choice(string.ascii_letters1)
    drugaLitera = random.choice(string.ascii_letters2)
    trzeciaLitera = random.choice(string.ascii_letters3)
    czwartaLitera = random.choice(string.ascii_letters4)
    piątaLitera = random.choice(string.ascii_letters5)
    szustaLitera = random.choice(string.ascii_letters6)
    siodmaLitera = random.choice(string.ascii_letters7)
    URL = "https://prnt.sc/"
    return (URL+pierwszaLitera+drugaLitera+trzeciaLitera+czwartaLitera+piątaLitera+szustaLitera+siodmaLitera)


def start():
    try:
        global photos

        s = Service('/usr/lib/chromium-browser/chromedriver')
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(service=s, options=options)
        driver.get(stworzLink())

        element = driver.find_element(By.CLASS_NAME, 'css-47sehv')
        element.click()

        element = driver.find_element(By.CLASS_NAME, 'under-image')

        element.screenshot(f"{get_random_string(6)}.png")
        driver.quit()
        photos += 1
        print(f"Number of saved photos: {photos}")
        
        start()
    except:
        print("Error")
        start()
start()