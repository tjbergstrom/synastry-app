# syn_calc.py
# Jan 2021
#
# Calculate birthcharts using the tables that I processed,
# And calculate synastry matches between charts.


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


def formatted(date):
	return f"{date.month}-{date.day}-{date.year}"


def birth_chart(date):
	date += " 12:00"
	date = dt.datetime.strptime(date, "%Y-%m-%d %H:%M")
	sun = signs.get_sign(date, sunfile)
	moon = signs.get_moon(date, moonfile)
	venus = signs.get_signs(date, venusfile)
	mars = signs.get_signs(date, marsfile)
	node = signs.get_sign(date, nodefile)
	jupiter = signs.get_signs(date, jupiterfile)
	saturn = signs.get_sign(date, saturnfile)
	return date, sun, moon, venus, mars, node, jupiter, saturn


def display_single_chart(date):
	date, sun, moon, venus, mars, node, jupiter, saturn = birth_chart(date)
	data = {formatted(date) : [sun, moon, venus, mars, node, jupiter, saturn]}
	df = pd.DataFrame(data=data)
	df.index = ["sun", "moon", "venus", "mars", "north node", "jupiter", "saturn"]
	return df.to_html()


def display_synastry_chart(date1, date2):
	# Calculate each birthchart
	date1, su1, mn1, v1, mr1, n1, j1, st1 = birth_chart(date1)
	date2, su2, mn2, v2, mr2, n2, j2, st2 = birth_chart(date2)

	# The combinations of planets to consider
	signs1 = [su1, su1, mn1, su1, v1, su1, mr1, su1, j1, su1, st1, su1, n1, mn1, mn1, v1, mn1, mr1, mn1, j1, mn1, st1, mn1, n1, v1, v1, mr1, v1, j1, v1, st1, v1, n1, mr1, mr1, j1, mr1, st1, mr1, n1]
	signs2 = [su2, mn2, su2, v2, su2, mr2, su2, j2, su2, st2, su2, n2, su2, mn2, v2, mn2, mr2, mn2, j2, mn2, st2, mn2, n2, mn2, v2, mr2, v2, j2, v2, st2, v2, n2, v2, mr2, j2, mr2, st2, mr2, n2, mr2]

	# Calculate the aspects between each combination of planets
	aspects = []
	for i, j in zip(signs1, signs2):
		aspects.append(signs.calc(i, j))

	# Add the birthcart combinations and aspects to a dataframe
	data = {
		formatted(date1) : signs1,
		formatted(date2) : signs2,
		"Aspect" : aspects,
	}

	df = pd.DataFrame(data=data)

	# Add the planet match names index to the dataframe
	df.index = ['sun+sun', 'sun+moon', 'moon+sun', 'sun+venus', 'venus+sun', 'sun+mars', 'mars+sun', 'sun+jupiter', 'jupiter+sun', 'sun+saturn', 'saturn+sun', 'sun+node', 'node+sun', 'moon+moon', 'moon+venus', 'venus+moon', 'moon+mars', 'mars+moon', 'moon+jupiter', 'jupiter+moon', 'moon+saturn', 'saturn+moon', 'moon+node', 'node+moon', 'venus+venus', 'venus+mars', 'mars+venus', 'venus+jupiter', 'jupiter+venus', 'venus+saturn', 'saturn+venus', 'venus+node', 'node+venus', 'mars+mars', 'mars+jupiter', 'jupiter+mars', 'mars+saturn', 'saturn+mars', 'mars+node', 'node+mars']

	return df.to_html()


def full_charts(chart1, chart2):
	planets = ["sun", "moon", "rising", "mercury", "venus", "mars", "jupiter", "saturn", "node"]
	aspects = []
	signs1 = []
	signs2 = []
	idx = []
	for i in range(0, 9):
		for j in range(i, 9):
			aspects.append(signs.calc(chart1[i], chart2[j]))
			signs1.append(chart1[i])
			signs2.append(chart2[j])
			idx.append(f"{planets[i]}+{planets[j]}")
			if i != j:
				aspects.append(signs.calc(chart1[j], chart2[i]))
				signs1.append(chart1[j])
				signs2.append(chart2[i])
				idx.append(f"{planets[j]}+{planets[i]}")
	data = {
		"chart1" : signs1,
		"chart2" : signs2,
		"Aspect" : aspects,
	}
	df = pd.DataFrame(data=data)
	df.index = idx
	df = df.loc[df["Aspect"] != ""]
	return df.to_html()



##
