import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# Set up the Chrome WebDriver
chrome_service = ChromeService()  # Replace with ChromeDriver executable path
driver = webdriver.Chrome(service=chrome_service)

# Record the start time
start_time = time.time()

# Initialize variables
base_url = "https://www.therichest.com/top-lists/top-250-richest-people-in-the-world/page/"
page_number = 1
links_collected = 0
all_links = []  # List to store all collected links
data_to_write = []  # List to store data for writing to CSV

# Collect links to individual profiles
while links_collected <= 100:  # Collect only 100 links
    # Build the URL of the page
    url = f"{base_url}{page_number}/"
    # Open the URL in the Chrome WebDriver
    driver.get(url)

    # Find and store links on the current page
    links = driver.find_elements(By.CSS_SELECTOR, 'td.name a')
    for link in links:
        all_links.append(link.get_attribute('href'))
        links_collected += 1
        if links_collected >= 100:
            break  # Break the loop if 100 links are collected

    # Check if there's a "Next" link and increment page number
    next_link = driver.find_element(By.CSS_SELECTOR, 'a.next')
    if not next_link.is_enabled():
        break
    page_number += 1

# Visit each page and extract data
for link in all_links:
    try:
        driver.get(link)
        # Extract data from the profile page
        title = driver.find_element(By.CSS_SELECTOR, 'h1.net-profile_header_title').text
        source = driver.find_element(By.CSS_SELECTOR, 'ul.net-profile_stats_list li span').text
        worth = driver.find_element(By.CSS_SELECTOR, 'strong.net-profile_header_networth').text
        # Add extracted data to the list for writing to CSV
        data_to_write.append([title, source, link, worth])
    except:
        # If any error occurs while extracting data, skip to the next link
        pass

# Close the Chrome WebDriver
driver.quit()

# Record the end time
end_time = time.time()

# Calculate and print the overall time taken
overall_time = end_time - start_time
print(f"Data collection completed in {overall_time:.2f} seconds.")

# Write data to CSV
with open('selenium_richest.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write header row
    writer.writerow(['title', 'source', 'url', 'worth'])
    # Write data rows
    writer.writerows(data_to_write)

print("Data writing to CSV completed.")
