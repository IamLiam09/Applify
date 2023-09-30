from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.options import Options

import pyautogui

import time

# setting up cookies for login 
chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium") 
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get("www.google.com")

# Set up the webdriver

driver = webdriver.Chrome(chrome_options=chrome_options)


# Navigate to the LinkedIn login page

driver.get("https://www.linkedin.com/login")


# Wait for the page to load

wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.ID, "username")))


# Enter the username and password

username = driver.find_element(By.ID, "username")

password = driver.find_element(By.ID, "password")

username.send_keys("princewill835@gmail.com")

password.send_keys("Colla@200")


# Click the login button

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

# login_button.click()

# open a new tab for email verificaiton

driver.execute_script('''window.open("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AXo7B7UoR0a2iiqWqaIs_qIqRdx7vmBTYbcbxxjfKehdaDg394AONNhPmn2AkBhl74WRJEH3QDOM&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S419529123%3A1692414673208219","_blank");''')

wait.until(EC.presence_of_element_located((By.ID, "identifierId")))

# inputing my email

Email = driver.find_element(By.ID, "identifierId")

Email.send_keys("princewill835@gmail.com")

# next login for email

Next= driver.find_element(By.XPATH, "//button[@type='submit']")


#switch to the second window



# Wait for the page to load

# wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Apply')]")))


# Search for the job posting

# search_bar = driver.find_element_by_xpath("//input[@aria-label='Search jobs, companies, and people']")

# search_bar.send_keys("job_title")

# search_bar.send_keys(Keys.RETURN)


# Wait for the page to load

# wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Apply')]")))


# Find the apply button and click it

# apply_button = driver.find_element_by_xpath("//button[contains(text(), 'Apply')]")

# apply_button.click()//


# Wait for the page to load

# wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Submit')]")))


# Fill out the application form

# first_name = driver.find_element_by_xpath("//input[@name='firstName']")

# last_name = driver.find_element_by_xpath("//input[@name='lastName']")

# email = driver.find_element_by_xpath("//input[@name='email']")

# phone = driver.find_element_by_xpath("//input[@name='phone']")

# summary = driver.find_element_by_xpath("//textarea[@name='summary']")

# summary.send_keys("summary_of_your_application")

# first_name.send_keys("your_first_name")

# last_name.send_keys("your_last_name")

# email.send_keys("your_email")

# phone.send_keys("your_phone_number")


# Click the submit button

# submit_button = driver.find_element_by_xpath("//button[contains(text(), 'Submit')]")

# submit_button.click()


