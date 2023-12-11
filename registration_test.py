from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# # Set up the Chrome driver with the options
driver = webdriver.Chrome(options=chrome_options)

# Open the signup page
driver.get("http://localhost:3000/")


# Fill in the signup form
username_field = driver.find_element(By.NAME, "username")
email_field = driver.find_element(By.NAME, "email")
password_field = driver.find_element(By.NAME, "password")

username_field.send_keys("testuser")
email_field.send_keys("testuser@example.com")
password_field.send_keys("testpassword")

# Submit the form
password_field.send_keys(Keys.RETURN)

# Wait for the signup to complete (you might need to adjust the sleep time)
time.sleep(5)
# Verify the signup success by checking if the browser is on the login page
login_page_title = "Login Page"
assert login_page_title in driver.title

if "Login Page" in driver.title:
    print("Test successful! Redirected to the login page.")
else:
    print("Test failed! Not redirected to the login page.")

# Close the browser
driver.quit()