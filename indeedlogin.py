import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from simplifylogin import details
import time
import pickle
import pyautogui as hand
if __name__ == '__main__':
    email = "princewill835@gmail.com"
    password = "Colla@200"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    browser = webdriver.Chrome(
        options=options,
    )
    browser.get('https://secure.indeed.com/auth')
    # Cookies already saved to log into linkedin
    cookies = pickle.load(open("indeedcookies.pkl", "rb"))
    for cookie in cookies:
        try:
            browser.add_cookie(cookie)
        except Exception as e:
            print(e)
    browser.get('https://ng.indeed.com/')

    # log into simplify

    details(browser)

    # Google search for job on linked

    time.sleep(5)

    browser.switch_to.new_window('tab')

    browser.get("https://www.google.com")

    browser.find_element(
        By.XPATH, "//textarea[@id='APjFqb']").send_keys("Backend Engineer dubai remote indeed")

    browser.find_element(
        By.XPATH, "//textarea[@id='APjFqb']").send_keys(Keys.RETURN)

    browser.find_element(By.TAG_NAME, 'h3').click()
    
    browser.find_element(By.XPATH, "//div[normalize-space()='Remote']").click()

    browser.find_element(By.ID, "filter-remotejob-menu").click()

    time.sleep(3)

    hand.leftClick(x=788, y=310, duration=1)

    browser.find_element(
        By.XPATH, "//div[normalize-space()='Date posted']").click()

    hand.leftClick(x=164, y=487, duration=1)

    browser.maximize_window()
