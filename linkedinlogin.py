import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from simplifylogin import details
# import time to load up the linkedin login verification
import time
import pickle
import pyautogui as hand
if __name__ == '__main__':
    email = "princewill835@gmail.com"
    password = "Colla@200"
    job = "backend engineer"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    browser = webdriver.Chrome(
        options=options,
    )
    
    # log into simplify
    
    details(browser)
    
    time.sleep(5)

    browser.switch_to.new_window('tab')
    
    browser.get('https://www.linkedin.com/login')
    # Cookies already saved to log into linkedin
    cookies = pickle.load(open("linkedincookies.pkl", "rb"))
    for cookie in cookies:
        try:
            browser.add_cookie(cookie)
        except Exception as e:
            print(e)
    browser.get('https://www.linkedin.com/feed/')

    job_search = browser.find_element(
        By.XPATH, "//input[@placeholder='Search']").send_keys("Backend Engineer")

    # click on the search bar
    hand.click(x=207, y=168, duration=1)
    hand.press("Enter")

    # click
    # on the job
    time.sleep(5)
    hand.leftClick(x=72, y=225, duration=1)

    # FILTER

    # click on remote
    time.sleep(2)
    hand.leftClick(x=621, y=219, duration=1)
    # Input click
    time.sleep(2)
    hand.leftClick(x=524, y=310, duration=1)
    # send result
    time.sleep(2)
    hand.leftClick(x=718, y=425, duration=1)

    # Date Posted
    time.sleep(2)
    hand.leftClick(x=340, y=215, duration=1)
    # Date input
    time.sleep(2)
    hand.leftClick(x=210, y=371, duration=1)
    # send result
    time.sleep(2)
    hand.leftClick(x=404, y=463, duration=1)

    # Experince
    time.sleep(2)
    hand.leftClick(x=491, y=220, duration=1)
    hand.leftClick(x=393, y=277, duration=1)
    hand.leftClick(x=350, y=323, duration=1)
    hand.leftClick(x=350, y=369, duration=1)
    hand.leftClick(x=548, y=552, duration=1)
    # time.sleep(5)
    # print(hand.position())
