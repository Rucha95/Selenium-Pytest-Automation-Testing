from selenium import webdriver
import time
import os

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Northeastern Behrakis Health Sciences Center page
driver.get("https://bouve.northeastern.edu/behrakis/")

# Click on the "Admissions" dropdown menu
admissions_menu = driver.find_element("link text", "Admissions")
admissions_menu.click()
time.sleep(2)

# Click on the "Undergraduate Admissions" option in the dropdown menu
undergrad_admissions_option = driver.find_element("link text","Undergraduate Admissions")
undergrad_admissions_option.click()
time.sleep(2)

# Click on the "Download our Program Guide" button
download_button = driver.find_element("link text","Download our Program Guide")
download_button.click()
time.sleep(2)

# Click on the "Download" link on the next page
download_link = driver.find_element("link text","Download")
download_link.click()
time.sleep(2)

download_path = "C:/Downloads"

# Wait for the guide to finish downloading
while not any(fname.endswith('.pdf') for fname in os.listdir(download_path)):
    time.sleep(1)

# Close the driver once the guide has downloaded
driver.quit()
