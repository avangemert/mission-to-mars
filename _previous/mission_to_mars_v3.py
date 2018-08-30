
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd


# ## Scraping

# ### NASA Mars News

# In[2]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# URL of page to be scraped
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


# In[4]:


# Retrieve page with the requests module
browser.visit(url)


# In[5]:


# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[6]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[7]:


# Retrieve the parent divs for all articles
news_p = soup.find(class_='rollover_description_inner').text


# In[8]:


print(news_p)


# In[9]:


news_title = soup.find(class_='content_title').text


# In[10]:


print(news_title)


# ### JPL Mars Space Images - Featured Image

# ### Mac user

# In[23]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[24]:


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=featured'
browser.visit(url)


# In[25]:


# HTML object
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')


# In[38]:


print(soup)


# In[44]:


# Extract image element
image_element = soup.find("li", class_="slide")


# In[46]:


# Get image url
image_url = image_element.find("a", class_="fancybox")["data-fancybox-href"]


# In[47]:


print (image_url)


# In[48]:


# Save complete URL
featured_image_url = f"https://www.jpl.nasa.gov{image_url}"


# In[49]:


print(featured_image_url)


# ### Mars Weather

# In[1]:


# URL of page to be scraped
url = 'https://twitter.com/marswxreport?lang=en'


# In[4]:


# Retrieve page with the requests module
response = requests.get(url)


# In[5]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')


# In[6]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[11]:


# Retrieve element that contains weather information
mars_weather = soup.find(class_='js-tweet-text-container').text


# In[12]:


print(mars_weather)


# ### Mars Facts

# Use Pandas to scrape the following site for facts about Mars.

# In[2]:


url = 'https://space-facts.com/mars/'


# In[4]:


# Use Panda's `read_html` to parse the url
table = pd.read_html(url)
table


# Use Pandas to convert the data to a HTML table string.

# In[8]:


mars_df = table[0]
mars_df


# In[9]:


html_mars = mars_df.to_html()
html_mars


# ### Mars Hemispheres

# Create Python dictionary to store Mars hemispheres image urls.

# In[76]:


hemisphere_image_urls = []


# In[48]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[49]:


# Visit the following URL
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)


# In[50]:


# Design an XPATH selector to grab the Cerberus Mars image
xpath = '//div[@class="item"]//a[@class="itemLink product-item"]/img'


# In[51]:


# Results shows links to four images
results = browser.find_by_xpath(xpath)
results


# In[52]:


img = results[0]
img.click()


# In[53]:


# Scrape the browser into soup and use soup to find the full resolution image of mars
# Save the image url to a variable called `img_url`
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
img_url = soup.find("img", class_="wide-image")["src"]
img_url


# In[54]:


# Save complete URL
img_url = f"https://astrogeology.usgs.gov{img_url}"


# In[55]:


print(img_url)


# In[56]:


# Find hemisphere title
title = soup.find("h2", class_="title").text
title


# In[78]:


# Adding values to dictionary and appending to list. Removing term 'Enhanced' from hemisphere name.
hemisphere_image_urls.append({"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg"})


# In[79]:


hemisphere_image_urls


# In[58]:


# Get info for second image
browser.visit(url)
xpath = '//div[@class="item"]//a[@class="itemLink product-item"]/img'
results = browser.find_by_xpath(xpath)
img = results[1]
img.click()


# In[59]:


html = browser.html


# In[60]:


soup = BeautifulSoup(html, 'html.parser')
img_url = soup.find("img", class_="wide-image")["src"]
img_url


# In[61]:


# Save complete URL
img_url = f"https://astrogeology.usgs.gov{img_url}"


# In[62]:


print(img_url)


# In[63]:


# Find hemisphere title
title = soup.find("h2", class_="title").text
title


# In[81]:


# Adding values to dictionary and appending to list. Removing term 'Enhanced' from hemisphere name.
hemisphere_image_urls.append({"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg"})


# In[65]:


# Get info for third image
browser.visit(url)
xpath = '//div[@class="item"]//a[@class="itemLink product-item"]/img'
results = browser.find_by_xpath(xpath)
img = results[2]
img.click()


# In[66]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')
img_url = soup.find("img", class_="wide-image")["src"]
img_url


# In[67]:


# Save complete URL
img_url = f"https://astrogeology.usgs.gov{img_url}"
print(img_url)


# In[68]:


# Find hemisphere title
title = soup.find("h2", class_="title").text
title


# In[82]:


# Adding values to dictionary and appending to list. Removing term 'Enhanced' from hemisphere name.
hemisphere_image_urls.append({"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg"})


# In[70]:


# Get info for fourth image
browser.visit(url)
xpath = '//div[@class="item"]//a[@class="itemLink product-item"]/img'
results = browser.find_by_xpath(xpath)
img = results[3]
img.click()


# In[71]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')
img_url = soup.find("img", class_="wide-image")["src"]
img_url


# In[72]:


# Save complete URL
img_url = f"https://astrogeology.usgs.gov{img_url}"
print(img_url)


# In[73]:


# Find hemisphere title
title = soup.find("h2", class_="title").text
title


# In[84]:


# Adding values to dictionary and appending to list. Removing term 'Enhanced' from hemisphere name.
hemisphere_image_urls.append({"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg"})


# In[85]:


hemisphere_image_urls

