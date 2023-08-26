import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import time to load up the linkedin login verification
import time
import pickle
if __name__ == '__main__':
    email = "princewill835@gmail.com"
    password = "Colla@200"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_argument('proxy-server=106.122.8.54:3128')
    # options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')

    # using chrome because undetected_chromedriver closes immediately
    browser = webdriver.Chrome(
        options=options,
    )
    browser.get('https://www.linkedin.com/login')
    #Cookies already saved to log into linkedin
    cookies = pickle.load(open("linkedincookies.pkl", "rb"))
    for cookie in cookies:
        try:
            browser.add_cookie(cookie)
        except Exception as e:
            print(e)
    browser.get('https://www.linkedin.com/feed/')
        
    time.sleep(60)