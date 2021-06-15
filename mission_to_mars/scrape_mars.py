import pandas as pd
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

    # Close the browser after scraping
    browser.quit()
 
    # Study data files
    mars_data = pd.read_html('https://galaxyfacts-mars.com')
    df0 = mars_data[0]
    mars_str = ""
    mars_str = df0.to_html(index=False, header=False)

    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit next page - astrogeology Mars hemispheres site
    burl = "https://marshemispheres.com/"
    url = "https://marshemispheres.com/cerberus.html"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Find the featured image and title
    htitle1 = soup.find("h2", class_="title").get_text()
    divdata = soup.find("div", class_="downloads")
    a_class = divdata.find_all('a')
    murl1 = a_class[0].get('href')
    
    himg_url1 = burl + murl1 

    # Close the browser after scraping
    browser.quit()

    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit next page - astrogeology Mars hemispheres site
    url = "https://marshemispheres.com/schiaparelli.html"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Find the featured image and title
    htitle2 = soup.find("h2", class_="title").get_text()
    divdata = soup.find("div", class_="downloads")
    a_class = divdata.find_all('a')
    murl2 = a_class[0].get('href')
    
    himg_url2 = burl + murl2 

    # Close the browser after scraping
    browser.quit()

    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit next page - - astrogeology Mars hemispheres site
    url = "https://marshemispheres.com/syrtis.html"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Find the featured image and title
    htitle3 = soup.find("h2", class_="title").get_text()
    divdata = soup.find("div", class_="downloads")
    a_class = divdata.find_all('a')
    murl3 = a_class[0].get('href')
    
    himg_url3 = burl + murl3 

    # Close the browser after scraping
    browser.quit()

    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit next page - - astrogeology Mars hemispheres site
    url = "https://marshemispheres.com/valles.html"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Find the featured image and title
    htitle4 = soup.find("h2", class_="title").get_text()
    divdata = soup.find("div", class_="downloads")
    a_class = divdata.find_all('a')
    murl4 = a_class[0].get('href')
    
    himg_url4 = burl + murl4 

    # Close the browser after scraping
    browser.quit()

    # Store all scraped data in a dictionary
    title_data = {
         "title_1": title1,
         "tease_1": articletease1,
         "image_1": mars_img1,
         "mars_string": mars_str,
         "title1": htitle1,
         "img_url1": himg_url1,
         "title2": htitle2,
         "img_url2": himg_url2,
         "title3": htitle3,
         "img_url3": himg_url3,
         "title4": htitle4,
         "img_url4": himg_url4
    }

    # Close the browser after scraping
    browser.quit()
   
        # Return results
    return title_data