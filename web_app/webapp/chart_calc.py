# astro.py
# may 24, 2020
#
# input one birthday and calculate the signs of each planet
#
# this was just my first file
# figuring out parsing a date and calculating the signs
# an intro to making sure it works and everything
#
# pre-processing notes:
#
# I copied/pasted and made files containing the signs for planets
# they needed to be processed so the code could use them
# these are some linux commands I used to standardize them
#
# replace slashes with commas
# tr -s '[/]' ',' < node.csv > node2.csv
# replacece blank spaces with commas:
# tr -s '[:blank:]' ',' < node2.csv > node3.csv
# delete last column:
# awk '!($8="")' node3.csv > node4.csv
# trim trailing white spaces after deleting last column:
# awk '{$1=$1};1' node4.csv > node5.csv
#
# remove a comma:
# awk -F"," '{print $1,$2,$3,$4,$5,$8}' venus.csv > venus2.csv
# remove unwanted columns, seperate remaining columns with comma (PERFECT!):
# awk '{print $1 "," $2 "," $3 "," $4 "," $5 "," $8}' venus2.csv > venus3.csv
#
# note: moon_signs.csv is in UTC+1 time zone
# all others in UTC-5 time zone
#
# these are the date ranges that I was able to collect:
# 1940 - 2013 moon
# 1940 - 2020 venus
# 1940 - 2021 sun
# 1940 - 2023 node
# 1940 - 2060 saturn
# 1940 - 2045 jupiter
# 1940 - 2026 mars
#
# command line usage:
# python3 astro.py -y 1990 -m 8 -d 26 -f "sun_signs.py"


from . import signs
import argparse
import pandas as pd
import datetime as dt
import os


basedir = os.path.abspath(os.path.dirname(__file__))
sunfile = os.path.join(basedir, "static/tables/sun_signs.csv")
moonfile = os.path.join(basedir, "static/tables/moon_signs.csv")
venusfile = os.path.join(basedir, "static/tables/venus_signs.csv")
marsfile = os.path.join(basedir, "static/tables/mars_signs.csv")
nodefile = os.path.join(basedir, "static/tables/node_signs.csv")
jupiterfile = os.path.join(basedir, "static/tables/jupiter_signs.csv")
saturnfile = os.path.join(basedir, "static/tables/saturn_signs.csv")


def birthday_chart(bday):
    bday += " 12:00"
    date = dt.datetime.strptime(bday, "%Y-%m-%d %H:%M")

    sun_sign = signs.get_sign(date, sunfile)
    moon_sign = signs.get_moon(date, moonfile)
    venus_sign = signs.get_signs(date, venusfile)
    mars_sign = signs.get_signs(date, marsfile)
    node_sign = signs.get_sign(date, nodefile)
    jupiter_sign = signs.get_signs(date, jupiterfile)
    saturn_sign = signs.get_sign(date, saturnfile)

    day = f"{date.month}-{date.day}-{date.year}"

    d = {day:[sun_sign, moon_sign, venus_sign, mars_sign, node_sign, jupiter_sign, saturn_sign]}
    df = pd.DataFrame(data=d)
    df.index = ["sun", "moon", "venus", "mars", "north node", "jupiter", "saturn"]

    return df.to_html()



##
