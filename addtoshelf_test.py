from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Set up the Chrome driver with the options
driver = webdriver.Chrome(options=chrome_options)


driver.get("http://localhost:3000/book-details?title=The%20Plague&userName=salehajamshed")

# Click the "To Be Read (TBR)" button for the first book
tbr_button = driver.find_element(By.ID, "tbr-button")
tbr_button.click()

try:
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert_text = alert.text
    expected_alert_text = "Book added to To Be Read (TBR)"

    # Verify that the expected alert text is present in the actual alert text
    if expected_alert_text in alert_text:
        print(f"Test Passed: {expected_alert_text}")
    else:
        print(f"Test Failed: Expected alert message '{expected_alert_text}' not found in alert: '{alert_text}'")

    # Close the alert (accept)
    alert.accept()

except:
    print("Test Failed: Alert not displayed")

# Close the browser
driver.quit()