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
    # Cookies already saved to log into linkedin

    
    wait = WebDriverWait(browser, 10)

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@id='email']")))
    
    browser.find_element(By.XPATH, "//input[@id='email']").send_keys(email)
    browser.find_element(
        By.XPATH, "//input[@id='password']").send_keys(password)

    cookies = pickle.load(open("simplifycookies.pkl", "rb"))
    for cookie in cookies:
        try:
            browser.add_cookie(cookie)
        except Exception as e:
            print(e)
    # browser.get('https://simplify.jobs/auth/login')

    # #simplify login
    # browser.switch_to.new_window('tab')

    # browser.get("https://chrome.google.com/webstore/detail/simplify-copilot-%E2%80%93-autofi/pbanhockgagggenencehbnadejlgchfc")

    # time.sleep(3)

    # hand.leftClick(x=929, y=305, duration=1)

    # time.sleep(3)

    # hand.leftClick(x=568, y=249, duration=1)

    # #handle process for simplify

    # #Google search for job on linked

    # time.sleep(5)

    # browser.switch_to.new_window('tab')

    # browser.get("https://www.google.com")

    # browser.find_element(
    #     By.XPATH, "//textarea[@id='APjFqb']").send_keys("Backend Engineer dubai remote indeed")

    # browser.find_element(
    #     By.XPATH, "//textarea[@id='APjFqb']").send_keys(Keys.RETURN)

    # browser.find_element(By.TAG_NAME, 'h3').click()

    # browser.find_element(By.XPATH, "//div[normalize-space()='Remote']").click()

    # browser.find_element(By.ID, "filter-remotejob-menu").click()

    # time.sleep(3)

    # hand.leftClick(x=788, y=310, duration=1)

    # browser.find_element(
    #     By.XPATH, "//div[normalize-space()='Date posted']").click()

    # hand.leftClick(x=164, y=487, duration=1)
