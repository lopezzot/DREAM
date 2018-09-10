import map

def buildcluster(fixedindex,vectorsignals,radiusstep,treshold = 0.3):
	"""Function that given a fixed fiber builds the 
	cluster around it, a cluster is given by a fixed 
	central fiber, a radius and a signal"""
	for radius in range(200,radiusstep): #find radius of cluster
		energyatdistance = energyatdistance(radius,radiusstep,fixedindex,vectorsignals)
		if energyatdistance<treshold:
			break
	for indexfiber in range(len(vectorsignals)): #find total signal in cluster
		if isinradius(radius,radiusstep,fixedindex,indexfiber):
			signalcluster = signalcluster + vectorsignals[indexfiber]
	return radius,signalcluster,fixedindex

def findmaxima(vectorsignals, treshold = 20):
	"""Function that return the valid indeces for 
	building clusters"""
	maxima = (,)
	for indexfiber in range(len(vectorsignals)):
		if vectorsignals[indexfiber]>treshold:
			if len(maxima) == 0:
				maxima.append(indexfiber)
				radius = buildcluster(indexfiber,vectorsignals,radiusstep,treshold)
	return maxima


