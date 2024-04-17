from extract import extract_data
from util import get_api_credentials, get_engine
from transform import transform_data
from load import load_data



def main():
    '''
    Extract data, transform and load to postgres
    '''
    api_id = get_api_credentials()[0]
    api_key = get_api_credentials()[1]

    #extract
    res = extract_data(api_id = api_id, api_key=api_key)
    print('Data extracted successfully')

    #transform
    clean_df = transform_data(res)
    print('Data transformed successfully')
    #load
    load_data(df=clean_df, engine=get_engine, table='rates')
    print('Data loaded successfully')

    #call function
    if __name__=='__main__':
        main()
        print('pipeline executed successfully')




