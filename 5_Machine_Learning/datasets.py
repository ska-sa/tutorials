## Function to load dataset
# Arun Aniyan
# SKA SA / RATT
# arun@ska.ac.za


import numpy as np
from sklearn.metrics import precision_score, recall_score,confusion_matrix


def load_planets():
	# Train data
	dataset = np.loadtxt('planet_train.csv',delimiter=',',dtype='str')
	feature_names = dataset[0,0:-1]
	features = dataset[1:,0:-1]
	labels = dataset[1:,-1]

	# Convert to floats
	features = features.astype('float')
	labels = labels.astype('float')


	# Print success message
	print 'Successfully Loaded the data !'

	## Some useful Statistics
	n_planets  = len(np.where(labels==1)[0])
	n_rrl  = len(np.where(labels==2)[0])
	n_sn  = len(np.where(labels==3)[0])

	# Validation Data
	testdata = np.loadtxt('planet_test.csv',delimiter=',',skiprows=1)

	testfeatures = testdata[:,0:-1]

	# Print Stats
	print '\nThere are total %d samples in your dataset.'%(features.shape[0])

	print '\nThere are %d Planets, %d RRLyrae and %d Supernovaes in your data.'%(n_planets,n_rrl,n_sn)
	
	print '\nYour dataset has %d features in total.'%(features.shape[1])

	print '\nYour validation data has %d samples.'%(testfeatures.shape[0])

	return feature_names,features,labels, testfeatures




# Evaluate Results

def evaluate_my_results(inlabels):
	testdata = np.loadtxt('planet_test.csv',delimiter=',',skiprows=1)
	actual_labels = testdata[:,-1]

	print 'Number of labels ',actual_labels.shape[0]
	
	score = precision_score(actual_labels,inlabels,average='micro')
	recall = recall_score(actual_labels, inlabels)

	print 'The precision score is %f'%(score*100)
	print 'The recall is %f'%(recall*100)

	print 'You found %d Exoplanets'%(confusion_matrix(actual_labels,inlabels)[0][0])
	print 'You found %d RRLyraes'%(confusion_matrix(actual_labels,inlabels)[1][1])
	print 'You found %d Supernova'%(confusion_matrix(actual_labels,inlabels)[2][2])




# Not used
'''
def load_transients():
	dataset = loadtxt('data/transient_train.csv',delimiter=',',dtype='str')
	feature_names = dataset[0,0:-1]
	features = dataset[1:,0:-1]
	labels = dataset[1:,-1]

	return feature_names,features,labels 

'''



	