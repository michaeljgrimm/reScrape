from bs4 import BeautifulSoup
import pprint

print('Begin Evil Zillow Scrape')
data = {}

with open('zillow.html', encoding='utf8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# URL
canonical_list = soup.find_all(rel='canonical')
data['url'] = canonical_list[0].attrs['href']

# Key Details: bedrooms, bathrooms, square feet
price_list = soup.find_all('span', class_='ds-value')
data['price'] = price_list[0].contents[0]
keydetail_list = soup.find_all('span', class_='ds-bed-bath-living-area')
data['bedrooms']    = keydetail_list[0].span.contents[0]
data['bathrooms']   = keydetail_list[2].span.contents[0]
data['sqft']        = keydetail_list[3].span.contents[0]
status_list = soup.find_all('span', class_='ds-status-details')
data['status'] = status_list[0].text
zestimate_list = soup.find_all('span', class_='ds-estimate-value')
data['zestimate'] = zestimate_list[0].text
address_list = soup.find_all('h1', class_='ds-address-container')
data['address'] = address_list[0].span.contents[0]
data['address_csz'] = address_list[0].span.next_sibling.contents[0].replace(u'\xa0', '') #remove &nbsp;

# Overview
zstats_list = soup.find_all('div', class_='ds-overview-stat-value')
zstats = {}
zstats['time'] = zstats_list[0].text
zstats['views'] = zstats_list[1].text
zstats['saves'] = zstats_list[2].text
data['zillow_stats'] = zstats
overview_list = soup.find_all('div', class_='ds-overview-section')
data['description'] = overview_list[1].contents[0].text

# Facts and features
homefacts_list = soup.find_all('ul', class_='ds-home-fact-list')
homefacts = {}
homefacts['type']       = homefacts_list[0].contents[0].contents[2].text
homefacts['year_built'] = homefacts_list[0].contents[1].contents[2].text
homefacts['heating']    = homefacts_list[0].contents[2].contents[2].text
homefacts['cooling']    = homefacts_list[0].contents[3].contents[2].text
homefacts['parking']    = homefacts_list[0].contents[4].contents[2].text
homefacts['lot']        = homefacts_list[0].contents[5].contents[2].text
homefacts['price_sqft'] = homefacts_list[0].contents[6].contents[2].text
data['facts_features'] = homefacts

# Rental value
rental_list = soup.find_all(id='ds-rental-home-values')
data['zestimate_rent'] = rental_list[0].text.replace('Rental valueRent Zestimate®','')

# finish

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data)
pass