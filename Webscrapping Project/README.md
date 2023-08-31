
# Three Scrapers For Top100 Richest People in the World

This repository contains web scraping scripts that collects the data from Top100 richest people from the world. The project is implemented in Python using various libraries and frameworks such as Scrapy, BeautifulSoup & Selenium.


## Scrapy: How to run the code

The ScrapySpider is a Scrapy spider designed to scrape information about the top richest people in the world from "https://www.therichest.com". The spider collects data such as their title, source, URL, and net worth.

To use the ScrapySpider to scrape richest people information, follow these steps:

### Prerequisites
Make sure you have the following tools installed:

1) Python
2) Scrapy

### Installation

1) Clone or download this repository to your local machine.
2) Navigate to the project directory using your terminal or command prompt.
3) Install the required dependencies using the following command:

```shell
  pip install scrapy
```

### Usage

1) Open the ScrapySpider.py file in a text editor.
2) In the start_urls list, add the starting URL(s) from which you want to start scraping.You can modify or add more URLs if needed.
3) Run the script using the following command in terminal after moving to the file's path:

```shell
  scrapy crawl yk_scraper -o scrapy_richest.csv
```
This command tells Scrapy to start crawling using the yk_scraper spider and save the scraped data to a CSV file named scrapy_richest.csv.

The spider will start scraping richest people information from the specified URL(s) and store the results in the CSV file.

*******************************************************************************************

## Beautiful Soup: How to run the code

The script bs_richest.py allows you to scrape information about the top richest people in the world from "https://www.therichest.com". It collects data such as their title, source, URL, and net worth using Python and popular libraries for web scraping.

To use the script to scrape richest people information using beautiful soup, follow these steps:

### Prerequisites
Make sure you have the following tools installed:

Python Libraries: requests, beautifulsoup4

### Installation

1) Clone or download this repository to your local machine.
2) Navigate to the project directory using your terminal or command prompt.
3) Install the required dependencies using the following command:

```shell
  pip install beautifulsoup4
  pip install requests
```

### Usage

1) Open the bs_richest.py file in a text editor.
2) Run the script using the following command in terminal after moving to the file's path:

```shell
  python .\bs_richest.py
```
This command will start the script, which will scrape richest people information from the specified URL and store the results in a CSV file named bs_richest.csv.

The script will create a CSV file containing the scraped data.

*******************************************************************************************

## Selenium: How to run the code

The script selenium_richest.py allows you to scrape information about the top richest people in the world from "https://www.therichest.com" using Selenium, a powerful browser automation tool. It collects data such as their title, source, URL, and net worth by simulating user interactions with a chrome web browser.

To use the script to scrape richest people information using selenium, follow these steps:

### Prerequisites
Make sure you have the following tools installed:

Python Libraries: chrome wedriver, link: https://chromedriver.chromium.org/
(I will be attaching chromedriver.exe file with this folder)

### Installation

1) Clone or download this repository to your local machine.
2) Navigate to the project directory using your terminal or command prompt.
3) Install the required dependencies using the following command:

```shell
  pip install selenium
```

### Usage

1) Open the selenium_richest.py file in a text editor.
2) Keep the "chromedriver.exe" at the same path where the selenium_richest.py file has been saved.
3) Run the script using the following command in terminal after moving to the file's path:

```shell
  python .\selenium_richest.py
```
This command will start the script, which will use Selenium to scrape richest people information from the specified URL and store the results in a CSV file named selenium_richest.csv.

The script will create a CSV file containing the scraped data.

