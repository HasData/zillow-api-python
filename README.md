## What is Zillow API

Zillow is a large online real estate marketplace where you can find all properties for sale or rent. Using the Zillow API or no-code [Zillow scraper](https://scrape-it.cloud/scrapers/zillow), you can connect to this vast database and retrieve real estate listings based on specific search parameters.

Using the Zillow data API, you can collect up-to-date real estate data without worrying about blockings, rotating proxies, and other difficulties you might encounter in the development process.

It makes it easy to get data such as a full address, coordinates (longitude and latitude), price, property description, and many other data characterizing the features of the property, such as the number of bedrooms and bathrooms.

## Install

`pip install zillow_api`

## API Key

To use the Zillow API, you need an API key. You can get an API key and some credits for free by signing up on the [Scrape-It.Cloud](https://scrape-it.cloud/).

## Using

To understand how to use Zillow API, look at this Zillow API example:

```python
from zillow_api import ZillowAPI

zillow_api_client = ZillowAPI("INSERT_YOUR_API_KEY")

search_result = zillow_api_client.search(
	params={
		"keyword": "new york, ny",
		"type": "forSale",
		"price[min]": 1000000,
		"price[max]": 2000000,
		"homeTypes": ["house", "apartment"]
	}
)

print(search_result)
```

In the Zillow API, there are both required and optional request parameters that you can use to customize your search. Here's an overview of the difference between the two:

1. Required Parameters:
- `keyword` (string): This parameter is required and is used to specify the keyword used to search for listings. It represents the search query or location you want to retrieve listings for.
- `type` (enum): This parameter is required and determines the type of listing you want to retrieve. The possible values are: forSale, forRent, or sold.

2. Optional Parameters:
- `sort` (enum): This parameter allows you to specify the sorting option for the search results. It is an optional parameter, and the possible values include various sorting criteria such as verifiedSource, homesForYou, priceHighToLow, and more.  
- `price` (object): This parameter allows you to filter listings based on the price range. It is an optional parameter consisting of min and max values representing the minimum and maximum price of the listing.  
- `beds` (object): This parameter enables you to filter listings based on the number of bedrooms. It is optional and includes min and max values to define the minimum and maximum number of bedrooms.  
- `baths` (object): Similar to beds, this parameter allows you to filter listings based on the number of bathrooms. It is optional and includes min and max values to define the minimum and maximum number of bathrooms.
- Several other optional parameters are available, such as yearBuilt, lotSize, squareFeet, homeTypes, etc.

You can narrow your search criteria using these additional options and get listings that meet your requirements. For example, to include or exclude certain features, set price ranges, specify the number of bedrooms or bathrooms, and more.

You can also retrieve data for a specific property using the following function:

```python
from zillow_api import ZillowAPI

zillow_api_client = ZillowAPI("INSERT_YOUR_API_KEY")

property_result = zillow_api_client.property(
	params={
		"url": "https://www.zillow.com/homedetails/301-E-79th-St-APT-23S-New-York-NY-10075/31543731_zpid/"
	}
)

print(property_result)
```

You can learn more about the additional options and response format on [the documentation page](https://docs.scrape-it.cloud/zillow-api/listing).

## Zillow API use cases

The Zillow API has many use cases for developers, businesses, and individuals in the real estate industry. For example, you can use the Zillow API to gather data on real estate trends, market values, and property information.

You can also use the Zillow API to provide location-based services, such as nearby amenities, schools, transportation options, etc. This can help people make informed decisions about the suitability of a property based on its surroundings.

Using the Zillow API to gain insights into market trends, demographics, and real estate statistics is useful for market research firms.

## Zillow Python API for Real Estate Scraping

Python is one of the most popular programming languages for web scraping and data processing. Therefore, you can create a multifunctional tool for working and processing real estate data using the Python Zillow API.

## Proxy or Zillow API

If you need to collect real estate data from Zillow and you are writing your own scraper, you have two options:

1. Research the structure of Zillow and write your own algorithm to collect data. Here, you will need to use a proxy to avoid blocking. You may also need to plug in captcha services.
    
2. Use Zillow API for Python. You don't need to use proxies here since API already uses them.

Everyone decides which option is more suitable for him based on the tasks of the project and its requirements.

If you want to know more about Zillow scraping, you can read our article about [Zillow scraping in Python](https://scrape-it.cloud/blog/scraping-zillow-using-python).
