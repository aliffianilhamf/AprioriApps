import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import association_rules, apriori

# load dataset
data = pd.read_csv("data_penjualan_new.csv") 
data['order time'] = pd.to_datetime(data['order time'], format="%d-%m-%Y %H:%M")

data['month'] = data['order time'].dt.month
data['day'] = data['order time'].dt.weekday

data['month'].replace([i for i in range (1, 12 + 1)], ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "september", "Oktober", "November", "desember"], inplace=True)
data['day'].replace([i for i in range (6+1)], ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"], inplace=True)

# ambli data
def get_data(period_day = '', weekday_weekend = '', month = '', day = ''):
    ds = data.copy()
    filtered = [
        (ds['period_day'].str.contains(period_day))&
        (ds['weekday_weekend'].str.contains(weekday_weekend))&
        (ds['month'].str.contains(month.title()))&
        (ds['day'].str.contains(day.title))
    ]
    
    return filtered if filtered.shape[0] else "NO RESULT!" 
