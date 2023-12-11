from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Set up the Chrome driver with the options
driver = webdriver.Chrome(options=chrome_options)

# Open the signup page
driver.get("http://localhost:3000/login")


# Fill in the signup form
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")
submit_button = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")

username_field.send_keys("testuser")
password_field.send_keys("testpassword")

# Submit the form
submit_button.click()
time.sleep(5)
dashboard_page_title = "Dashboard"
if dashboard_page_title in driver.title:
    print("Login Successful")

    # Check for the welcome message on the dashboard
    welcome_message = driver.find_element(By.XPATH,"//div[@class='welcome-message']")
    if "Welcome, testuser" in welcome_message.text:
        print("Welcome message found. Test Passed.")
    else:
        print("Welcome message not found. Test Failed.")
# Close the browser
driver.quit()