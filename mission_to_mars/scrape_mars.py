from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit visitcostarica.herokuapp.com
    url = "https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the average temps
    #titleline = soup.find('div', id='content_title')
    #title1 = titleline.text
    title1 = soup.find("div", class_="content_title").get_text()
    #title1 = titleline.find.text
    #title2 = soup.find_all('div', id='content title')[2].text
    #title3 = soup.find_all('div', id='content title')[3].text
    #title4 = soup.find_all('div', id='content title')[4].text
 
    # Store data in a dictionary
    title_data = {
        "title_1": title1
    #    "title_2": title2,
    #    "title_3": title3,
    #    "title_4": title4
    }

    # Close the browser after scraping
    browser.quit()
   
        # Return results
    return title_data