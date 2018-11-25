import numpy as np
from sklearn import mixture
import warnings
import collections
warnings.filterwarnings("ignore")

#Gaussian mixture model algorithm
def GMM(X,num):
        gmm = mixture.GMM(n_components = num,covariance_type = 'full')
        gmm.fit(X)
        labels = gmm.predict(X)
        labels_unique = np.unique(labels)
        print('gmm:',labels_unique)
        return labels
