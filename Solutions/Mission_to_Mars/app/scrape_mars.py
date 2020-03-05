from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime as dt
import time 
import re 
def scrape_all():

    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store in dictionary.
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "hemispheres": hemispheres(browser),
        "weather": twitter_weather(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html

    soup = bs(html, 'html.parser')

    news_title = soup.find('div', class_='content_title').find('a').text
    news_p = soup.find('div', class_='article_teaser_body').text

    return news_title, news_p


def featured_image(browser):
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    html_image = browser.html
    soup = bs(html_image, 'html.parser')

    image_url = soup.find('div',class_='carousel_items')('article')[0]['style'].\
    replace('background-image: url(','').replace(');','')[1:-1]


    web_url = 'https://www.jpl.nasa.gov'
    return image_url


def hemispheres(browser):

    # A way to break up long strings
    url = (
        "https://astrogeology.usgs.gov/search/"
        "results?q=hemisphere+enhanced&k1=target&v1=Mars"
    )

    browser.visit(url)
    
    html_hemispheres = browser.html

    soup = bs(html_hemispheres, 'html.parser')

    items = soup.find_all('div', class_='item')

    hemisphere_image_urls = []

    main_url = 'https://astrogeology.usgs.gov'

    for i in items: 
        title = i.find('h3').text
        images_url = i.find('a', class_='itemLink product-item')['href']
        browser.visit(main_url + images_url)
        img_html = browser.html
        soup = bs( img_html, 'html.parser')
        img_url = main_url + soup.find('img', class_='wide-image')['src']
        hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
        
    return hemisphere_image_urls


def twitter_weather(browser):
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    tweet_attrs = {"class": "tweet", "data-name": "Mars Weather"}
    try: 
        mars_weather_tweet = weather_soup.find("div", attrs=tweet_attrs)
        mars_weather = mars_weather_tweet.find("p", "tweet-text").get_text()  
    
    except AttributeError:
        pattern = re.compile(r'sol')
        mars_weather = weather_soup.find('span', text=pattern).text
        
    return mars_weather




def mars_facts():
    try:
        df = pd.read_html("http://space-facts.com/mars/")[0]
    except BaseException:
        return None

    df.columns = ["description", "value"]
    df.set_index("description", inplace=True)

    # Add some bootstrap styling to <table>
    return df.to_html(classes="table table-striped")


if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())
