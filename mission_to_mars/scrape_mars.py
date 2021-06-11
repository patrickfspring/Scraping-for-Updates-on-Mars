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

    # Get the headline title and teaser
    title1 = soup.find("div", class_="content_title").get_text()
    articletease1 = soup.find("div", class_="article_teaser_body").get_text()

    # Close the browser after scraping
    browser.quit()

    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit next page - JPL Mars Space Images - Featured Image
    url = "https://spaceimages-mars.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Find the featured image
    relative_image_path = soup.find("img", class_="headerimage fade-in")["src"]
    mars_img1 = url + relative_image_path
 
    # Store all scraped data in a dictionary
    title_data = {
         "title_1": title1,
         "tease_1": articletease1,
         "image_1": mars_img1
    #    "title_2": title2,
    #    "title_3": title3,
    #    "title_4": title4
    }

    # Close the browser after scraping
    browser.quit()
   
        # Return results
    return title_data