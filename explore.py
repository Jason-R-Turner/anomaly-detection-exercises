import acquire
import prepare
import pandas as pd
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

