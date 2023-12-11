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

driver.get("http://localhost:3000/dashboard?userName=testuser")

genre_dropdown = Select(driver.find_element(By.ID, "genre"))
genre_dropdown.select_by_visible_text("Mystery")

# Find the "Fetch Books" button and click it
fetch_books_button = driver.find_element(By.ID, "fetch-books-button")
fetch_books_button.click()

time.sleep(5)

# Verify that the recommended books are displayed on the page
expected_books = ["A Game of Thrones", "Crime and Punishment", "Loves Music, Loves to Dance"]

if all(book_title in driver.page_source for book_title in expected_books):
    print("Test Passed: All expected books are displayed.")
else:
    print("Test Failed: Some or all expected books are not displayed.")

# Close the browser
driver.quit()