import pandas as pd

def metrics(df):
    '''
    Gets the number of rows, columns, and number of rows with nulls for each column.  Also returns description for common values from table.
    '''
    rows = df.shape[0]
    cols = df.shape[1]
    nulls = df.isna().sum()
    print(f'There are {rows} rows and {cols} columns in this dataframe.')
    print(f'Plus the following nulls:\n{nulls}')
    print(df.dtypes)
    return df.describe().T


def get_numbers(df):
    '''
    Returns the number of instances of unique values in descending order and the number of non-nulls for every column
    '''    
    for column in df.columns:
        print(column)
        print(df[column].value_counts())
        print("-----------------")
    return df.info()

