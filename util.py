from dotenv import dotenv_values
from sqlalchemy import create_engine



def get_api_credentials():
    '''
    This is a function that returns the XECD API credentials from a .env file
    parameters: NULL
    Return value: A tuple of api_key and api_id
    Return type: Tuple
    '''
    config =dict(dotenv_values('.env'))
    api_key = config.get('API_KEY')
    api_id = config.get('API_ID')

    return(api_id, api_key)


def get_engine():
    '''
    This is a function that retrieves connetion credentials from
    a .env file and returns a postgres sqlalchemy engine

    parameter: None
    Return value: A sqlalchemy engine
    Return Type: A SQLalchemy engine object
    '''
    config = dict(dotenv_values('.env'))
    db_username = config.get('DB_USERNAME')
    db_password = config.get('DB_PASSWORD')
    db_host = config.get('DB_HOST')
    db_port = config.get('DB_PORT')
    db_name = config.get('DB_NAME')
    

    engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')
    
    return engine