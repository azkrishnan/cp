

def cluster_points(plist, f): #f (p0, p1) -> is p0 friend of p1
	clusters = [];
	while(len(plist) > 0):
		cluster = filter(lambda x: f(x,plist[0]), plist)
		plist = setol(plist, cluster, '-');
		clusters.append(cluster);
	return clusters;

def geolocgroup(plist, zoom, screen_distance):
	scale = 1183315100;#scale on google map when zoom = 0
	return cluster_points(plist, lambda x,y: latlngdist(x[0], x[1], y[0], y[1])*(2**zoom) <= screen_distance*scale);
