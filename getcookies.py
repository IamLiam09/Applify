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
    email = "williamndubuisidev@gmail.com"
    password = "Forjob@2023"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_argument('proxy-server=106.122.8.54:3128')
    # options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')

    # using chrome because undetected_chromedriver closes immediately
    browser = webdriver.Chrome(
        options=options,
    )
    browser.get('https://simplify.jobs/auth/login')

    wait = WebDriverWait(browser, 10)

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@id='email']")))

    # find the element and send the key
    browser.find_element(By.XPATH, "//input[@id='email']").send_keys(email)
    browser.find_element(
        By.XPATH, "//input[@id='password']").send_keys(password)

    browser.find_element(
        By.XPATH, "//button[@type='submit']").send_keys(Keys.ENTER)

    # time.sleep(5)

    # browser.find_element(By.ID, "auth-page-google-password-fallback").click()

    # time.sleep(5)

    # browser.find_element(
    #     By.XPATH, "//input[@name='__password']").send_keys(password)

    # browser.find_element(
    #     By.XPATH, "//button[@type='submit']").click()
    # Log into the account
    # login_button = browser.find_element(
    #     By.XPATH, "//button[@type='submit']").click()

    time.sleep(40)

    cookies = browser.get_cookies()
    print(cookies)

    pickle.dump(cookies, open("simplifycookies.pkl", "wb"))
