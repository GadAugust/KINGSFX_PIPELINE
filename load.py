



def load_data(df, engine, table):
    '''
    '''
    df.to_sql(table, con=engine, if_exists ='append', index=False)