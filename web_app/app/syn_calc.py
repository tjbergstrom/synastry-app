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
	date1, chart1 = birth_chart(date1)[0], birth_chart(date1)[1:]
	date2, chart2 = birth_chart(date2)[0], birth_chart(date2)[1:]
	return full_charts(chart1, chart2, formatted(date1), formatted(date2), False)


def full_charts(chart1, chart2, label1='chart1', label2='chart2', full=True):
	planets = ["sun", "moon", "rising", "mercury", "venus", "mars", "jupiter", "saturn", "node"]
	if not full:
		planets = ["sun", "moon", "venus", "mars", "jupiter", "saturn", "node"]
	aspects = []
	signs1 = []
	signs2 = []
	idx = []
	for i in range(0, len(planets)):
		for j in range(i, len(planets)):
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
		label1 : signs1,
		label2 : signs2,
		"Aspect" : aspects,
	}
	df = pd.DataFrame(data=data)
	df.index = idx
	df = df.loc[df["Aspect"] != ""]
	return df.to_html()



##
