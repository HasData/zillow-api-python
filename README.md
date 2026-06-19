# Real Estate Listing API for Zillow (Python)

> HasData is an independent service and is not affiliated with, endorsed by, or sponsored by Zillow Group, Inc. Zillow is a trademark of its respective owner.

## Getting real estate data from Zillow.com

Zillow.com is a large online real estate marketplace where you can find properties for sale or rent. Using our real estate listing API or the No-Code [Zillow scraper](https://scrape-it.cloud/scrapers/zillow), you can retrieve public real estate listings based on specific search parameters.

With our API, you can collect up-to-date public real estate data without managing rotating proxies, JavaScript rendering, and the other difficulties you'd otherwise handle during development.

It makes it easy to get data such as a full address, coordinates (longitude and latitude), price, property description, and many other characteristics of a property, such as the number of bedrooms and bathrooms.

## Install

`pip install zillow-api-s`

## API Key

To use the API, you need an API key. You can get an API key and some credits for free by signing up on [Scrape-It.Cloud](https://scrape-it.cloud/).

## Using

To understand how to use the API, look at this example:

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

In the API, there are both required and optional request parameters that you can use to customize your search. Here's an overview of the difference between the two:

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

## Use cases

Our real estate listing API has many use cases for developers, businesses, and individuals in the real estate industry. For example, you can gather data on real estate trends, market values, and property information.

You can also use the API to provide location-based services, such as nearby amenities, schools, transportation options, etc. This can help people make informed decisions about the suitability of a property based on its surroundings.

Using the API to gain insights into market trends, demographics, and real estate statistics is useful for market research firms.

## Real estate data extraction with Python

Python is one of the most popular programming languages for web scraping and data processing. You can build a multifunctional tool for working with and processing real estate data using our Python library.

## Build it yourself or use our API

If you need to collect public real estate data from Zillow.com and you are writing your own scraper, you have two options:

1. Research the structure of Zillow.com and write your own algorithm to collect data. Here you would manage proxies and JavaScript rendering yourself.

2. Use our real estate listing API for Python. You don't need to manage proxies here, since the API already handles them.

Everyone decides which option is more suitable based on the project's tasks and its requirements.

If you want to know more about Zillow scraping, you can read our article about [scraping Zillow in Python](https://scrape-it.cloud/blog/scraping-zillow-using-python).
