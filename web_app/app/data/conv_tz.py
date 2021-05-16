# conv_tz.py
# May 2021
# Convert the tables to UTC timezone
# (All the tables I found were in UTC-5)


import os
import csv
import pandas as pd
import datetime as dt
from datetime import timedelta


def conv(infile, tz=5):
    with open('tmp.csv', 'w') as outf:
        writer = csv.writer(outf)
        df = pd.read_csv(infile)
        writer.writerow(df.columns.values.tolist())
        for index, row in df.iterrows():
            y = row["start year"]
            m = row["start month"]
            d = row["start day"]
            hr = row["start hour"]
            mn = row["start minute"]
            ampm = row["ampm"]
            label = row["label"]
            if ampm == "PM" and hr != 12:
                hr += 12
            if ampm == "AM" and hr == 12:
                hr = 0
            org_date = dt.datetime(y, m, d, hr, mn)
            new_date = org_date + timedelta(hours=tz)
            y, m, d, hr, mn = new_date.year, new_date.month, new_date.day, new_date.hour, new_date.minute
            if hr > 12:
                hr -= 12
                ampm = "PM"
            elif hr == 12:
                ampm = "PM"
            elif hr == 0:
                hr = 12
                ampm = "AM"
            else:
                ampm = "AM"
            writer.writerow([m,d,y,hr,mn,ampm,label])
    os.rename('tmp.csv', infile)


conv("mars_signs.csv")
conv("jupiter_signs.csv")
conv("saturn_signs.csv")
conv("sun_signs.csv")
conv("venus_signs.csv")



##



