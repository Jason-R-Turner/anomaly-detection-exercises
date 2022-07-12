import acquire
import prepare
import pandas as pd
import numpy as np
import os


def explore_question3(df):
    '''
    This function creates a dataframe tailored to explore the following:
    
    Question 3:
    Are there students who, when active, hardly access the curriculum? 
    If so, what information do you have about these students?

    The function renames columns & drops records that are not associated with 
    active students.
    '''
    df3 = df.copy()
    df3 = df3.rename(columns={'program_id': 'program', 'name': 'cohort'})
    #rename columns just for preference
    df3 = df3.dropna()
    #drops nulls, records without sufficient data about student access
    df3['program_access'] = (df3.date_time >= df3.start_date) & (df3.date_time <= df3.end_date)
    # creates boolean column to weed out everything, but active students
    df3 = df3[(df3['program_access'] == True)]
    df3 = df3[(df3['cohort'] != 'staff')] 
    #creates df of active students that are not staff

    return df3


def get_q6_eda_df():
    df = prepare.prepare_logs()
    df.date_time = pd.to_datetime(df.date_time)
      # convert dates to DTG
    dates = ['start_date', 'end_date', 'created_at', 'updated_at']
    for col in dates:
        df[col] = pd.to_datetime(df[col])
        # drop unnecessary columns
    df = df.drop(columns=(['date', 'time']))
    return df

def get_upper_bound_and_difference(series, multiplier = 1.5):
    '''
    Gets the upper bound and its difference from the max of a series based on the InterQuartile Range and a multiplier. Default multiplier is 1.5
    '''
    q1, q3 = series.quantile([.25, .75])
    iqr = q3 - q1
    
    upper = q3 + (multiplier * iqr)
    difference = series.max() - upper
    
    print(f'{series.name}\'s Upper bound is {round(upper, 2)}, and difference from max is {round(difference, 2)}')
    return upper, difference