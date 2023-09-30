import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pickle
import pyautogui as hand
def details(browser):
    email = "williamndubuisidev@gmail.com"
    password = "Forjob@2023"

    # options = webdriver.ChromeOptions()
    # # options.add_experimental_option("detach", True)
    # browser = webdriver.Chrome(
    #     options=options,
    # )
    # get the screen to be maximazed

    browser.switch_to.new_window('tab')
    browser.get('https://simplify.jobs/auth/login')
    # Cookies already saved to log into simplify

    wait = WebDriverWait(browser, 30)

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@id='email']")))

    browser.find_element(By.XPATH, "//input[@id='email']").send_keys(email)
    browser.find_element(
        By.XPATH, "//input[@id='password']").send_keys(password)

    # simplify cookes
    cookies = pickle.load(open("simplifycookies.pkl", "rb"))
    time.sleep(3)

    hand.leftClick(x=654, y=600, duration=1)
    for cookie in cookies:
        try:
            browser.add_cookie(cookie)
        except Exception as e:
            print(e)
if __name__ == '__main__':
    details()