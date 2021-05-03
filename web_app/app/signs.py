# signs.py
# may 26, 2020
#
# Parse the sign tables and calculate aspects between planets.


import csv
import pandas as pd
import datetime as dt


# Read the file with all the signs and get the sign for the birthday
def get_sign(date, input_file):
    year = date.year
    df = pd.read_csv(input_file)
    sign = "Not Found"
    for index, row in df.iterrows():
        y = row["start year"]
        m = row["start month"]
        d = row["start day"]
        new_date = dt.datetime(y, m, d)
        if new_date <= date:
            sign = row["label"]
        if new_date > date:
            break
    return sign


# Get the sign from files that have hour and minute precision
def get_signs(date, input_file):
    year = date.year
    df = pd.read_csv(input_file)
    df2 = df3 = df
    df = df[df["start year"] == year]
    df2 = df2[df2["start year"] == (year-1)]
    df3 = df3[df3["start year"] == (year+1)]
    fs = [df2, df, df3]
    df = pd.concat(fs)
    sign = "Not Found"
    for index, row in df.iterrows():
        y = row["start year"]
        m = row["start month"]
        d = row["start day"]
        hr = row["start hour"]
        mi = row["start minute"]
        ampm = row["ampm"]
        if ampm == "PM" and hr != 12:
            hr += 12
        if ampm == "AM" and hr == 12:
            hr = 0
        new_date = dt.datetime(y, m, d, hr, mi)
        if new_date <= date:
            sign = row["label"]
        if new_date > date:
            break
    return sign


# Get the moon sign, much more precise
def get_moon(date, input_file):
    year = date.year
    month = date.month
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    input_file = csv.reader(open(input_file, "r"), delimiter = ",")
    found = False
    moons = []
    prev_row = ""
    for row in input_file:
        try:
            if str(year) == row[0]:
                found = True
                moons.append(prev_prev_row)
                continue
        except:
            pass
        try:
            if str(year+1) == row[0]:
                found = False
        except:
            pass
        prev_prev_row = prev_row
        prev_row = row
        if found:
            moons.append(row)
    first = True
    m = ""
    y = ""
    sign = "Not Found"
    for moon in moons:
        if first:
            y = (year-1)
            m = 12
            first = False
        else:
            y = year
        try:
            if moon[0] in month_names:
                m = moon[0]
                continue
        except:
            pass
        try:
            d = moon[0]
            t = moon[1]
            label = moon[2]
        except:
            pass
        i = 1
        for mo in month_names:
            if mo == m:
                m = i
            i += 1
        date_and_time = f"{y}-{m}-{d} {t}"
        new_date = dt.datetime.strptime(date_and_time,"%Y-%m-%d %H:%M")
        if new_date <= date:
            sign = label.capitalize()
        if new_date > date:
            break
        try:
            if moon[3] in month_names:
                m = moon[3]
        except:
            pass
    return sign


# Calculate the synastry aspect between two planets
def calcs(p, q):
    if p == q:
        return "Conjunct ❤️"
    # opposites are six signs apart
    elif p - q == 6:
        return "Opposite 💘"
    # trines are three signs apart
    elif (p - q) % 4 == 0:
        return "Trine 💖"
    # sextiles are two signs apart
    elif (p - q) % 2 == 0:
        return "Sextile 💕"
    # squares are four signs apart
    elif (p - q) % 3 == 0:
        return "Square 💔"
    # anything else is a quincunx
    else:
        return "Quincunx 🖤"


# Make the calculation easier
def calc(s1, s2):
    signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    if s1 not in signs or s2 not in signs:
        return ""
    p1 = signs.index(s1) + 1
    p2 = signs.index(s2) + 1
    if p1 > p2:
        return calcs(p1, p2)
    else:
        return calcs(p2, p1)



##
