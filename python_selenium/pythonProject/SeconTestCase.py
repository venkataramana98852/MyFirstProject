from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Define the path to the chromedriver executable
chrome_driver_path = r"C:\Brwosers_drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Create a Service object with the path to chromedriver
service = Service(executable_path=chrome_driver_path)

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=service)

# Your test code here
driver.get("https://admin-demo.nopcommerce.com")
print("Page Title:", driver.title)
# element1 = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.NAME, 'username')))
# element1.send_keys("Admin")
#
# element2 = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.NAME, 'password')))
# element2.send_keys("admin123")
#
# element3 = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
# )
# element3.click()

input("Press Enter to close the browser...")



