import gpxpy
import gpxpy.gpx
import os
import gpxpy.geo as mod_geo
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from multiprocessing import Pool, Lock
import multiprocessing
import matplotlib.pyplot as plt


directory = "tmp"
min = multiprocessing.Value('i', 9999999)
max = multiprocessing.Value('i', 0)
count = multiprocessing.Value('i', 0)
min.value = 9999999
max.value = 0
count.value = 0

def parse(filename):
	if filename.endswith(".gpx"):
		file = os.path.join(directory, filename)

		#print(file)
		print(count.value)
		gpx_file = open(file, 'r')
		gpx = gpxpy.parse(gpx_file)

		#search min hearth rate
		for track in gpx.tracks:
			for segment in track.segments:
				for point in segment.points:
					try:
						if(int(point.extensions[0][0].text) < min.value):
							min.value = int(point.extensions[0][0].text)
						if(int(point.extensions[0][0].text) > max.value):
							max.value = int(point.extensions[0][0].text)
						if(int(point.extensions[0][0].text) > 0):
							count.value +=1
					except:
						min.value = min.value

def parsehr(filename):
	if filename.endswith(".gpx"):
		file = os.path.join(directory, filename)

		#print(file)
		print(count.value)
		gpx_file = open(file, 'r')
		gpx = gpxpy.parse(gpx_file)

		#search min hearth rate
		for track in gpx.tracks:
			for segment in track.segments:
				for point in segment.points:
					try:
						if(int(point.extensions[0][0].text) > 0):
							hrs[count.value] = int(point.extensions[0][0].text)
							count.value +=1
					except:
						min.value = min.value


with Pool(processes=8) as pool:
	pool.map(parse, os.listdir(directory))

hrs = multiprocessing.Array('i', count.value)
count.value = 0

with Pool(processes=8) as pool:
	pool.map(parsehr, os.listdir(directory))

print('Min Heart Rate:{0}'.format(min.value))
print('Max Heart Rate:{0}'.format(max.value))

print(hrs[0])
print(hrs[1])

import csv

with open('heart.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(hrs)

a = sns.distplot(hrs)
plt.show()
