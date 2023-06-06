import requests
from urllib.parse import urlencode

ZILLOW_LISTING_API = 'https://api.scrape-it.cloud/zillow/listing'
ZILLOW_PROPERTY_API = 'https://api.scrape-it.cloud/zillow/property'

class ZillowAPI:
    def __init__(self, apiKey=None):
        if apiKey is None:
            raise ValueError('API Key is not provided')
        
        self.apiKey = apiKey
    
    def handleErrors(self, result, statusCode):
        if "status" in result and result['status'] and result['status'] == 'error' and 'message' in result:
            raise ValueError(result['message'])
        
        if statusCode == 403:
            raise ValueError("You don't have enough API credits to perform this request")
        
        if statusCode == 401:
            raise ValueError('Invalid API Key')
        
        if statusCode == 429:
            raise ValueError('You reached concurrency limit')
        
        if 'errors' in result and len(result['errors']) > 0:
            error = ValueError('Validation error')
            error.validation_errors = result['errors']
            raise error
        
        if 'requestMetadata' not in result:
            raise ValueError('Invalid response')
        
        if "status" in result['requestMetadata'] and result['requestMetadata']['status'] == 'error':
            raise ValueError('Invalid response')
    
    def search(self, params):
        url = f"{ZILLOW_LISTING_API}?{urlencode(params, doseq=True)}"

        headers = {
            'x-api-key': self.apiKey,
        }
        
        requestParams = {
            'source': 'python_sdk'
        }
        
        response = requests.get(url, headers=headers, params=requestParams)
        result = response.json()

        self.handleErrors(result, response.status_code)
        
        if result['requestMetadata']['status'] == 'ok':
            return result
        
        return result
    
    def property(self, params):
        url = f"{ZILLOW_PROPERTY_API}?{urlencode(params)}"
        
        headers = {
            'x-api-key': self.apiKey,
        }
        
        requestParams = {
            'source': 'python_sdk'
        }
        
        response = requests.get(url, headers=headers, params=requestParams)
        result = response.json()

        self.handleErrors(result, response.status_code)
        
        if result['requestMetadata']['status'] == 'ok':
            return result
        
        return result