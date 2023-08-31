import scrapy
import time

class ScrapySpider(scrapy.Spider):
    name = "yk_scraper"
    
    # Custom settings for the spider's output
    custom_settings = {
        'Final_Output': {
            'scrapy_richest.csv': {
                'format': 'csv',
                'encoding': 'utf8',
                'overwrite': True,  # Overwrite the CSV file each time the spider is run
            },
        },
    }
   
    # Record the start time when the spider starts running
    start_time = time.time()
    
    # Initialize a counter to keep track of the number of yielded items
    counter = 0

    # Initial URL to start scraping
    start_urls = ['https://www.therichest.com/top-lists/top-250-richest-people-in-the-world/page/1/']

    # Method to parse the main page and collect links to individual profiles
    def parse(self, response):
        base_url = "https://www.therichest.com/top-lists/top-250-richest-people-in-the-world/page/"
        
        # Extract all 'td' elements with class 'name' containing links to profiles
        tds = response.css('td.name')
        for td in tds:
            # Extract the link and construct the complete URL
            link = td.css('a::attr(href)').extract_first()
            link = "https://www.therichest.com" + link
            
            # Send a request to the individual profile page
            yield scrapy.Request(link, callback=self.parse_person)
            
            # Increment the counter to keep track of the number of profiles processed
            self.counter += 1

            # Break the loop after processing 100 profiles
            if self.counter >= 100:
                break

        # Extract the link to the next page for pagination
        next_link = response.xpath('//a[@class="next"]/@href').get()
        if next_link and self.counter <= 100:  # Proceed to the next page if counter is less than 100
            yield scrapy.Request('https://www.therichest.com' + next_link, callback=self.parse)

    # Method to parse individual profile pages
    def parse_person(self, response):
        item = {}
        # Extract relevant information from the profile page
        item['title'] = response.xpath('//h1[@class="net-profile_header_title"]/text()').get()
        item['source'] = response.xpath('//span[@itemprop="memberOf"]/text()').get()
        item['url'] = response.url
        item['worth'] = response.xpath('//strong[@itemprop="netWorth"]/text()').get()
        
        # Yield the extracted item to be saved in the output
        yield item
        
    # Record the end time when the spider completes its run
    end_time = time.time()
    
    # Calculate and print the total time taken for the entire run
    total_time = end_time - start_time
    print(f"Total time taken: {total_time:.2f} seconds")
