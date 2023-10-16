from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a WebDriver instance
driver = webdriver.Chrome()

# Open the Facebook login page
driver.get('https://www.facebook.com')

# Find the username and password input fields by name
username_field = driver.find_element(By.NAME, 'email')
password_field = driver.find_element(By.NAME, 'pass')

# Enter your Facebook username and password
username_field.send_keys('your-username')
password_field.send_keys('your-email')

# Find the login button by name
login_button = driver.find_element(By.NAME, 'login')

# Click the login button
login_button.click()

# Wait for a few seconds to ensure the login is complete
time.sleep(10)  # You can adjust the sleep duration as needed

# You are now logged in. Add any additional actions or navigate to different pages as needed.

# Finally, don't forget to close the WebDriver when you're done
driver.quit()
