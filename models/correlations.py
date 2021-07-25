import pandas as pd
import os

def chl_covid_correlation():
    chl = pd.read_csv('data/chl.csv')
    covid = pd.read_csv('data/covid.csv')

    chl = chl[['Measurement Value', 'Time']]
    chl.dropna(inplace=True)
    chl.rename(columns = {'Measurement Value':'Chl Measurement'}, inplace = True)
    chl.rename(columns = {'Time':'date'}, inplace = True)

    covid = covid[['date', 'new_cases']]
    covid.dropna(inplace=True)

    chl['date'] = pd.to_datetime(chl['date'], infer_datetime_format=True)
    covid['date'] = pd.to_datetime(covid['date'], infer_datetime_format=True)

    merge = pd.merge(chl, covid, how='outer', on = 'date')
    merge.dropna(inplace=True)
    corr = merge.corr().abs().unstack().sort_values(kind="quicksort")
    return corr[0] * 100

def chl_activity_correlation():
    chl = pd.read_csv('data/chl.csv')
    activity = pd.read_csv('data/japan_activity.csv')

    chl = chl[['Measurement Value', 'Time']]
    chl.dropna(inplace=True)
    chl.rename(columns = {'Measurement Value':'Chl Measurement'}, inplace = True)
    chl.rename(columns = {'Time':'date'}, inplace = True)

    activity = activity[['time', 'measurement']]
    activity.rename(columns = {'time':'date'}, inplace = True)
    activity.dropna(inplace=True)

    chl['date'] = pd.to_datetime(chl['date'], infer_datetime_format=True, utc=True)
    activity['date'] = pd.to_datetime(activity['date'], infer_datetime_format=True, utc=True)

    merge = pd.merge(chl, activity, how='outer', on = 'date')
    merge.dropna(inplace=True)
    corr = merge.corr().abs().unstack().sort_values(kind="quicksort")
    return corr[0] * 100
