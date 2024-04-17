import requests




def extract_data(api_id, api_key):
    '''
    This is a function to extract currency exchange rates of certain countries against the usd from the XECD API

    paramers:
    -api_id = API account ID
    -api_key = API account key
    Return value: a json response from the API
    Return Type: json
    '''
    currencies = ['NGH','GHS','KES','UGX','MAD','XDF','EGP']
    curr_codes = ",".join(currencies)
    url = f'https://xecdapi.xe.com/v1/convert_from.csv/?from=GBP&to={curr_codes}&amount=1'
    # API call
    response = requests.get(url, auth=(api_id,api_key))
    data = response.json()

    return data