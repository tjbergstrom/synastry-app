# astro2.py
# may 25, 2020
#
# this file takes two input birthdays
# and calculates their synastry match
# it's not perfect code,
# but it's an intro to seeing the calculations work


import os
from . import signs
import pandas as pd
import datetime as dt
import urllib.request


basedir = os.path.abspath(os.path.dirname(__file__))
sunfile = os.path.join(basedir, "static/tables/sun_signs.csv")
moonfile = os.path.join(basedir, "static/tables/moon_signs.csv")
venusfile = os.path.join(basedir, "static/tables/venus_signs.csv")
marsfile = os.path.join(basedir, "static/tables/mars_signs.csv")
nodefile = os.path.join(basedir, "static/tables/node_signs.csv")
jupiterfile = os.path.join(basedir, "static/tables/jupiter_signs.csv")
saturnfile = os.path.join(basedir, "static/tables/saturn_signs.csv")

def synastry(d1, d2):
	d1 += " 12:00"
	d2 += " 12:00"

	date1 = dt.datetime.strptime(d1, "%Y-%m-%d %H:%M")
	date2 = dt.datetime.strptime(d2, "%Y-%m-%d %H:%M")

	# Calculate the sign of each planet for the first birthday
	su1 = signs.get_sign(date1, sunfile)
	mn1 = signs.get_moon(date1, moonfile)
	v1 = signs.get_signs(date1, venusfile)
	mr1 = signs.get_signs(date1, marsfile)
	n1 = signs.get_sign(date1, nodefile)
	j1 = signs.get_signs(date1, jupiterfile)
	st1 = signs.get_sign(date1, saturnfile)

	# And for the second birthday
	su2 = signs.get_sign(date2, sunfile)
	mn2 = signs.get_moon(date2, moonfile)
	v2 = signs.get_signs(date2, venusfile)
	mr2 = signs.get_signs(date2, marsfile)
	n2 = signs.get_sign(date2, nodefile)
	j2 = signs.get_signs(date2, jupiterfile)
	st2 = signs.get_sign(date2, saturnfile)

	# Calculate the aspects between the planets of the two birthdays
	sun_sun = signs.calc(su1, su2)
	sun_moon = signs.calc(su1, mn2)
	moon_sun = signs.calc(mn1, su2)
	sun_venus = signs.calc(su1, v2)
	venus_sun = signs.calc(v1, su2)
	sun_mars = signs.calc(su1, mr2)
	mars_sun = signs.calc(mr1, su2)
	sun_jupiter = signs.calc(su1, j2)
	jupiter_sun = signs.calc(j1, su2)
	sun_saturn = signs.calc(su1, st2)
	saturn_sun = signs.calc(st1, su2)
	sun_node = signs.calc(su1, n2)
	node_sun = signs.calc(n1, su2)
	moon_moon = signs.calc(mn1, mn2)
	moon_venus = signs.calc(mn1, v2)
	venus_moon = signs.calc(v1, mn2)
	moon_mars = signs.calc(mn1, mr2)
	mars_moon = signs.calc(mr1, mn2)
	moon_jupiter = signs.calc(mn1, j2)
	jupiter_moon = signs.calc(j1, mn2)
	moon_saturn = signs.calc(mn1, st2)
	saturn_moon = signs.calc(st1, mn2)
	moon_node = signs.calc(mn1, n2)
	node_moon = signs.calc(n1, mn2)
	venus_venus = signs.calc(v1, v2)
	venus_mars = signs.calc(v1, mr2)
	mars_venus = signs.calc(mr1, v2)
	venus_jupiter = signs.calc(v1, j2)
	jupiter_venus = signs.calc(j1, v2)
	venus_saturn = signs.calc(v1, st2)
	saturn_venus = signs.calc(st1, v2)
	venus_node = signs.calc(v1, n2)
	node_venus = signs.calc(n1, v2)
	mars_mars = signs.calc(mr1, mr2)
	mars_jupiter = signs.calc(mr1, j2)
	jupiter_mars = signs.calc(j1, mr2)
	mars_saturn = signs.calc(mr1, st2)
	saturn_mars = signs.calc(st1, mr2)
	mars_node = signs.calc(mr1, n2)
	node_mars = signs.calc(n1, mr2)

	# The following is kind of a brute force way of displaying everything

	d1 = f"{date1.month}-{date1.day}-{date1.year}"
	d2 = f"{date2.month}-{date2.day}-{date2.year}"

	# Add the two birthcarts and the aspects to a dataframe
	d = {d1:[su1, su1, mn1, su1, v1, su1, mr1, su1, j1, su1, st1, su1, n1, mn1, mn1, v1, mn1, mr1, mn1, j1, mn1, st1, mn1, n1, v1, v1, mr1, v1, j1, v1, st1, v1, n1, mr1, mr1, j1, mr1, st1, mr1, n1],
	d2:[su2, mn2, su2, v2, su2, mr2, su2, j2, su2, st2, su2, n2, su2, mn2, v2, mn2, mr2, mn2, j2, mn2, st2, mn2, n2, mn2, v2, mr2, v2, j2, v2, st2, v2, n2, v2, mr2, j2, mr2, st2, mr2, n2, mr2],
	'Aspect':[sun_sun, sun_moon, moon_sun, sun_venus, venus_sun, sun_mars, mars_sun, sun_jupiter, jupiter_sun, sun_saturn, saturn_sun, sun_node, node_sun, moon_moon, moon_venus, venus_moon, moon_mars, mars_moon, moon_jupiter, jupiter_moon, moon_saturn, saturn_moon, moon_node, node_moon, venus_venus, venus_mars, mars_venus, venus_jupiter, jupiter_venus, venus_saturn, saturn_venus, venus_node, node_venus, mars_mars, mars_jupiter, jupiter_mars, mars_saturn, saturn_mars, mars_node, node_mars]}

	df = pd.DataFrame(data=d)

	# Add the planet matches to the dataframe
	df.index = ['sun+sun', 'sun+moon', 'moon+sun', 'sun+venus', 'venus+sun', 'sun+mars', 'mars+sun', 'sun+jupiter', 'jupiter+sun', 'sun+saturn', 'saturn+sun', 'sun+node', 'node+sun', 'moon+moon', 'moon+venus', 'venus+moon', 'moon+mars', 'mars+moon', 'moon+jupiter', 'jupiter+moon', 'moon+saturn', 'saturn+moon', 'moon+node', 'node+moon', 'venus+venus', 'venus+mars', 'mars+venus', 'venus+jupiter', 'jupiter+venus', 'venus+saturn', 'saturn+venus', 'venus+node', 'node+venus', 'mars+mars', 'mars+jupiter', 'jupiter+mars', 'mars+saturn', 'saturn+mars', 'mars+node', 'node+mars']

	return df.to_html()



##
