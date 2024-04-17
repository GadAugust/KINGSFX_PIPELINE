import pandas as pd
from datetime import datetime



def transform_data(data):
    '''
    
    '''
    timestamp = data['timestamp']
    base = data['from']
    row =[]
    for rate in data['to']:
        curr = rate['quotecurrency']
        exchange_rate = rate['mid']

        row.append((timestamp, base, curr, exchange_rate))
    df = pd.DataFrame(row, columns=['timestamp', 'currency_from', 'currency_to','rate'])
    # cleaning the timestamp column
    df['timestamp'] = df['timestamp'].apply(lambda x: datetime.strptime(x,"%y-%m-%dT%H:%M:%SZ"))

    return df
