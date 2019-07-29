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

for filename in os.listdir(directory):
	if filename.endswith(".gpx"):
		file = os.path.join(directory, filename)

		#print(file)
		gpx_file = open(file, 'r')
		gpx = gpxpy.parse(gpx_file)

		hr_tot = 0
		count = 0

		#search min hearth rate
		for track in gpx.tracks:
			for segment in track.segments:
				for point in segment.points:
					time = point.time
					try:
						hr = int(point.extensions[0][0].text)
						if(hr > 0):
							count +=1
							hr_tot += hr
					except:
						hr = hr
				hr_tot = hr_tot / count
				print('{0};;;;{1}'.format(time,hr_tot))

