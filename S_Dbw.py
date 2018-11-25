import math
from scipy.spatial import distance
import numpy as np
import itertools
import re
import warnings
from sklearn import metrics

class validation:
        def __init__(self, data, labels):
                self.dataMatrix = data
                self.classLabel = labels
                self.validation = np.nan
                self.description = ''

        def __density(a,b,stdev):
                dis=distance.euclidean(a,b)
#               print(dis)
                if dis>stdev:
                        return 0
                else:
                        return 1

        def s_dbw(self):
                self.description = "The S_Dbw index, a measure of compactness"
                sumDens=0
                sumNormCluster=0
                sumScat=0
                list_centers=[]
        #       print(self.classLabel)
        #       print(np.max(self.classLabel))
                numCluster=np.max(self.classLabel)+1

                normSigDataset=np.linalg.norm(np.var(self.dataMatrix,0))
                for i in range(numCluster):
                        indices=[t for t, x in enumerate(self.classLabel) if x == i]
                        clusterMember=self.dataMatrix[indices,:]
                        clusterCenter=np.mean(clusterMember,0)
                        list_centers.append(clusterCenter)
                        normSigCluster=np.linalg.norm(np.var(clusterMember,0))
                        sumScat=sumScat+normSigCluster/normSigDataset
                        sumNormCluster=sumNormCluster+normSigCluster
                stdev=math.sqrt(sumNormCluster)/numCluster
#               print(stdev)

                for i in range(numCluster):
                        sumDensity1=0
                        sumTemp=0

                        indices1=[t for t, x in enumerate(self.classLabel) if x == i]
                        clusterMember1=self.dataMatrix[indices1,:]
                        for member in clusterMember1:
                                sumDensity1=sumDensity1+validation.__density(member,list_centers[i],stdev)
                        for j in range(numCluster):
                                if j!=i:
                                        sumDensity2=0
                                        sumDensityCombine=0
                                        indices2=[t for t, x in enumerate(self.classLabel) if x == j]
                                        clusterMember2=self.dataMatrix[indices2,:]
                                        for member in clusterMember2:
                                                sumDensity2=sumDensity2+validation.__density(member,list_centers[j],stdev)
                                        midPoint=[]
                                        for member in combined:
                                                #print('member:',member)

                                                sumDensityCombine=sumDensityCombine+validation.__density(member,midPoint,stdev)
        #                               print(sumDensity1)
        #                               print(sumDensity2)
                                        if(sumDensity1==0 and sumDensity2==0):
                                                return float('inf')
                                        sumTemp=sumTemp+sumDensityCombine/max([sumDensity1,sumDensity2])
                                sumDens=sumDens+sumTemp
                        scat=sumScat/numCluster
                        dens_bw=sumDens/(numCluster*(numCluster-1))
                        self.validation = scat+dens_bw
                        return self.validation
