from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Start the Chrome browser in headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Navigate to your web application
base_url = "http://localhost:3000/my-books?userName=salehajamshed"
driver.get(base_url)

# Find the "Delete Book" button for the first book in the "To Be Read (TBR)" shelf
wait = WebDriverWait(driver, 10)
delete_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.book-shelf[data-category="tbr"] .delete-book')))

delete_button.click()

# Check if the book card is removed from the UI
try:
    driver.find_element(By.CSS_SELECTOR, '.book-shelf[data-category="tbr"] .delete-book')
    print("Test Failed: Book card still present after deletion")
except:
    print("Test Passed: Book card successfully deleted")

# Close the browser
driver.quit()
