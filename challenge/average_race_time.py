# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime
import pandas as pd
import numpy as np

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    # with open('10k_racetimes.txt', 'rt') as file:
    #     content = file.read()
    # return content
    df = pd.read_csv("10k_racetimes.csv")
    return df

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races_df = get_data()
    # TODO: grab only Rhines times by searching athlete column for her name
        # create a list of her times
    filtered_df = races_df[races_df['Athlete'].str.contains('Jennifer Rhines', case=False, na=False)]
    times_list = filtered_df['TIME'].to_list()
    
    return times_list

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    total = datetime.timedelta()

    for time in racetimes:
        try:
            mins, secs, ms = re.split(r'[:.]', time)
            total += datetime.timedelta(minutes=int(mins), seconds=int(secs), milliseconds=int(ms))
        except ValueError:
            mins, secs = re.split(r'[:.]', time)
            total += datetime.timedelta(minutes=int(mins), seconds=int(secs))

    avg_times = total / len(racetimes)
    print(avg_times)
    return f'{avg_times}'[2:-5]