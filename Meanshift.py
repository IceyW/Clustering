import numpy as np
from sklearn.cluster import MeanShift,estimate_bandwidth
import warnings
import collections
warnings.filterwarnings("ignore")

#MeanShift algorithm
def meanshift(x,quan):
        bandwidth=estimate_bandwidth(x,quantile=quan,n_samples=7500)
        ms=MeanShift(bandwidth=bandwidth,bin_seeding=True)
        ms.fit(x)
        labels=ms.labels_
        labels = np.asarray(labels)
        cluster_centers = ms.cluster_centers_
        labels_unique=np.unique(labels)
#       print('meanshift:',labels_unique)
        return labels,cluster_centers

