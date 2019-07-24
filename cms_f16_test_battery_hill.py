import gpxpy
import gpxpy.gpx
import os
import gpxpy.geo as mod_geo

start = mod_geo.Location(44.519994, 10.856544)
stop =  mod_geo.Location(44.507362, 10.854840)

directory = "tmp"
for filename in os.listdir(directory):
	if filename.endswith(".gpx"):
		file = os.path.join(directory, filename)
		#print(file)
		gpx_file = open(file, 'r')
		gpx = gpxpy.parse(gpx_file)

		pointStart = None
		pointStop = None

		#search start
		min = 9999999
		for track in gpx.tracks:
			for segment in track.segments:
				for point in segment.points:
					#print('{3}: Point at ({0},{1}) -> {2} Dist from Start:{4} Dist from End:{5}'.format(point.latitude, point.longitude, point.elevation, point.time, point.distance_2d(start), point.distance_2d(stop)))
					if(min>point.distance_2d(start)):
						min = point.distance_2d(start)
						pointStart = point

		#search stop
		min = 9999999
		for track in gpx.tracks:
			for segment in track.segments:
				for point in segment.points:
					if(min>point.distance_2d(stop)):
						min = point.distance_2d(stop)
						pointStop = point

		if((pointStop.time_difference(pointStart) > 0) and (pointStart.time < pointStop.time)):
			#print('Start:{0} End:{1}'.format(pointStart, pointStop))
			#print('Seconds:{0} Speed:{1:.1f} km/h'.format(pointStop.time_difference(pointStart), pointStart.speed_between(pointStop)*3.6))
			print('{0};{1:.1f}'.format(pointStart.time, pointStart.speed_between(pointStop)*3.6))

