# Import necessary libraries
import csv
import time
import requests
from bs4 import BeautifulSoup

# Function to fetch profile data using requests
def fetch_profile_data(url):
    response = requests.get(url, headers=headers, cookies=cookies)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    return None

# Function to write data to CSV file
def write_to_csv(data):
    with open('bs_richest.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['title', 'source', 'url', 'worth'])
        writer.writerows(data)

# Headers and Cookies for requests (you might need to update these)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}

cookies = {
    'viewType': 'direct',
    'AMP_TOKEN': '%24NOT_FOUND',
    '_gid': 'GA1.2.315323177.1693371734',
    '_ga': 'GA1.2.582430291.1693371733',
    '_gat': '1',
    '_ga_S2LDV82XXN': 'GS1.1.1693371732.1.1.1693372021.0.0.0',
}

# Record the start time
start_time = time.time()

# Create a list to store the data
data_to_write = []

# Base URL and initialization
base_url = "https://www.therichest.com/top-lists/top-250-richest-people-in-the-world/page/"
page_number = 1
links_fetched = 0  # Counter for fetched links

# Start scraping loop
while links_fetched < 100:  # Limit to 100 links
    url = f"{base_url}{page_number}/"

    print(url)

    # Send a GET request to the URL
    response = requests.get(url, headers=headers, cookies=cookies)

    if response.status_code == 200:
        # Parse the response using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all 'td' elements with class 'name'
        name_tds = soup.find_all('td', {'class': 'name'})
        for name_td in name_tds:
            link_elem = name_td.find('a')
            try:
                link = link_elem['href']
                full_link = "https://www.therichest.com" + link

                print(full_link)

                # Fetch individual profile page data using the fetch_profile_data function
                profile_soup = fetch_profile_data(full_link)

                if profile_soup:
                    # Extract relevant information from the profile page
                    title = profile_soup.find('h1', {'class': 'net-profile_header_title'}).text
                    worth = profile_soup.find('strong', {"class": 'net-profile_header_networth'}).text
                    source = profile_soup.find('ul', {'class': 'net-profile_stats_list'}).find('li').find('span').text

                    # Append data to the list
                    data_to_write.append([title, source, full_link, worth])
                    print(title)

                    links_fetched += 1  # Increment the counter

                    if links_fetched >= 100:
                        break  # Break the loop after fetching 100 links
            except Exception as e:
                print(e)
                pass

        # Check for the link to the next page
        next_link = soup.find('a', class_='next')
        if next_link:
            page_number += 1
        else:
            break
    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)

# Write data to CSV using the write_to_csv function
write_to_csv(data_to_write)

print("Data scraping completed.")

# Record the end time
end_time = time.time()

# Calculate and print the total time taken
total_time = end_time - start_time
print(f"Total time taken: {total_time:.2f} seconds")
