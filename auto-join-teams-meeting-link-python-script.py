from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to ChromeDriver
chrome_driver_path = '/usr/bin/chromedriver'

# Create a service object with the path to ChromeDriver
service = Service(chrome_driver_path)

# Initialize Chrome options
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize the WebDriver with the service and options
driver = webdriver.Chrome(service=service, options=options)

try:
    # Navigate to the URL
    driver.get('https://teams.microsoft.com/l/meetup-join/19%3ameeting_YTk3NmMyZDktOGIzOS00MTVjLTllYTctMGM5ZTQ2YmI3YjEx%40thread.v2/0?context=%7b%22Tid%22%3a%225087d92e-75bc-48ff-b1f1-f7d76c855eab%22%2c%22Oid%22%3a%224aa3c958-2553-4507-acbd-e7b4499f15df%22%7d')

    # Wait for the button to be clickable
    wait = WebDriverWait(driver, 30)
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fui-Button[data-track-action-outcome="cancelJoinMeeting"]')))

    # Click the button
    # button.click()

finally:
    # Close the WebDriver after some time to observe the result
    import time
    time.sleep(10)
    driver.quit()
