{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Splinter and BeautifulSoup\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as bs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set the executable path and initialize the chrome browser in splinter\n",
    "executable_path = {'executable_path': 'chromedriver'}\n",
    "browser = Browser('chrome', **executable_path)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Visit the NASA mars news site"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visit Nasa news url through splinter module\n",
    "url = \"https://mars.nasa.gov/news/\"\n",
    "\n",
    "browser.visit(url)\n",
    "\n",
    "# Optional delay for loading the page\n",
    "\n",
    "browser.is_element_present_by_css(\"ul.item_list li.slide\", wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The MarCO Mission Comes to an End\n",
      "The pair of briefcase-sized satellites made history when they sailed past Mars in 2019.\n"
     ]
    }
   ],
   "source": [
    "#collect the latest News Title and Paragraph Text\n",
    "\n",
    "html = browser.html\n",
    "\n",
    "soup = bs(html, 'html.parser')\n",
    "\n",
    "\n",
    "# Retrieve the latest element that contains news title and news_paragraph\n",
    "news_title = soup.find('div', class_='content_title').find('a').text\n",
    "news_p = soup.find('div', class_='article_teaser_body').text\n",
    "\n",
    "# Display New Title and Paragraph Text\n",
    "print(news_title)\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## JPL Space Images Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit URL\n",
    "url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA16192-1920x1200.jpg'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.\n",
    "\n",
    "html_image = browser.html\n",
    "soup = bs(html_image, 'html.parser')\n",
    "\n",
    "image_url = soup.find('div',class_='carousel_items')('article')[0]['style'].\\\n",
    "    replace('background-image: url(','').replace(');','')[1:-1]\n",
    "\n",
    "\n",
    "web_url = 'https://www.jpl.nasa.gov'\n",
    "\n",
    "#feature image url\n",
    "featured_image_url = web_url + image_url\n",
    "featured_image_url"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Mars Weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://twitter.com/marswxreport?lang=en'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "weather_soup = bs(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# the latest Mars weather tweet from the page.Save the tweet text for the weather report as a variable called mars_weather.\n",
    "\n",
    "# find the tweet text\n",
    "\n",
    "mars_weather = weather_soup.find('p', class_='TweetTextSize').text\n",
    "\n",
    "mars_weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url)\n",
    "\n",
    "html_hemispheres = browser.html\n",
    "\n",
    "soup = bs(html_hemispheres, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres\n",
    "items = soup.find_all('div', class_='item')\n",
    "\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "main_url = 'https://astrogeology.usgs.gov'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg'}]"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Append the dictionary with the image url string and the hemisphere title to a list. \n",
    "#This list will contain one dictionary for each hemisphere.\n",
    "\n",
    "\n",
    "for i in items: \n",
    "    title = i.find('h3').text\n",
    "    images_url = i.find('a', class_='itemLink product-item')['href']\n",
    "    browser.visit(main_url + images_url)\n",
    "    img_html = browser.html\n",
    "    soup = bs( img_html, 'html.parser')\n",
    "    img_url = main_url + soup.find('img', class_='wide-image')['src']\n",
    "    hemisphere_image_urls.append({\"title\" : title, \"img_url\" : img_url})\n",
    "    \n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Description</th>\n",
       "      <th>Value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5</td>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>6</td>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>7</td>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>8</td>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Description                          Value\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                   -87 to -5 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.\n",
    "\n",
    "url = \"https://space-facts.com/mars/\"\n",
    "tables = pd.read_html(url)\n",
    "\n",
    "facts_df = tables[0]\n",
    "facts_df.columns = [\"Description\", \"Value\"]\n",
    "\n",
    "facts_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  }
 ],
 "metadata": {
  "kernel_info": {
   "name": "python3"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  },
  "nteract": {
   "version": "0.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
