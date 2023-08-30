import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pickle
import pyautogui as hand
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
    browser.get('https://secure.indeed.com/auth')
    #Cookies already saved to log into linkedin
    cookies = pickle.load(open("indeedcookies.pkl", "rb"))
    for cookie in cookies:
        try:
            browser.add_cookie(cookie)
        except Exception as e:
            print(e)
    browser.get('https://ng.indeed.com/')
    
    # browser.find_element(By.XPATH, "//input[@id='text-input-what']").send_keys("Backend Engineer")
    # browser.find_element(By.XPATH, "//input[@id='text-input-where']").send_keys("Dubai")
    # browser.find_element(By.XPATH, "//button[@type='submit']").click()
        
    
    browser.switch_to.new_window('tab')
    
    browser.get("https://www.google.com")
    
    browser.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys("Backend Engineer dubai remote indeed")
    
    browser.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys(Keys.RETURN)
    
    browser.find_element(By.TAG_NAME, 'h3').click()        
