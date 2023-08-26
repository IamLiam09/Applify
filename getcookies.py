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
    browser.get('https://secure.indeed.com/auth?hl=en_NG&co=NG&continue=https%3A%2F%2Fng.indeed.com%2F&tmpl=desktop&service=my&from=gnav-util-homepage&jsContinue=https%3A%2F%2Fng.indeed.com%2F&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess')

    # find the element and send the key
    browser.find_element(By.ID, 'ifl-InputFormField-3').send_keys(email)

    browser.find_element(
        By.XPATH, "//button[@type='submit']").click()

    time.sleep(5)

    browser.find_element(By.ID, "auth-page-google-password-fallback").click()

    time.sleep(5)

    browser.find_element(
        By.XPATH, "//input[@name='__password']").send_keys(password)

    browser.find_element(
        By.XPATH, "//button[@type='submit']").click()
    # Log into the account
    # login_button = browser.find_element(
    #     By.XPATH, "//button[@type='submit']").click()

    time.sleep(40)

    cookies = browser.get_cookies()
    print(cookies)

    pickle.dump(cookies, open("indeedcookies.pkl", "wb"))
