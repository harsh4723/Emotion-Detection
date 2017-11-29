import os
import csv
import random as rn
import math
import operator 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn import svm

dire =r"G:\5th sem\ee320 DSP\project\csv\all2"
#print os.listdir(dire)
finaldata1=[]
finaldata=[]
for filename in os.walk(dire):
	for x in filename[2]:
		file=filename[0]+"\\"+str(x)
		with open(file,'rb') as csvfile:
			dataset=csv.reader(csvfile)
			data=list(dataset)
			data2=np.array(data).T.tolist()
			for l in data2:
				finaldata1.append(l)


			
rn.shuffle(finaldata1)
labelset=[]
for x in finaldata1:
	labelset.append(x[-1])
	del(x[-1])


for x in finaldata1:
	finaldata.append(x)

finaldata=np.array(finaldata).T.tolist()
print len(finaldata)

print "which features you want to delete?"

D={"ZCR":0,"Energy":1,"entropy of energy":2,"spectralCentroid":3,"spectralSpread":4,"spectralEntropy":5,"spectralFlux":6,"SpectarlRollOff":7,"MFCCs":"9-21","ChromaVector":"22-33","Chroma Deviation":34}
print D

a="yes"
A=[]
print "-1 to exit"
while(x!=-1):
	x=int(raw_input())
	A.append(x)

del(A[-1])

finaldata2=[]
for x in range(len(finaldata)):
	if x not in A:
		finaldata2.append(finaldata[x])

	

finaldata=np.array(finaldata2).T.tolist()

print len(finaldata[0])


X_train=np.array(finaldata)
X_scaled = preprocessing.scale(X_train)
finaldata=X_scaled.tolist()
finaldata=preprocessing.normalize(finaldata)


traindata=[]
testdata=[]
labeltrain=[]
labeltest=[]

l=len(finaldata)

ltrain=int(0.80*l)
ltest=l-ltrain


for x in range(ltrain):
	traindata.append(finaldata[x])
	labeltrain.append(labelset[x])

for x in range(ltest):
	testdata.append(finaldata[x+ltrain])
	labeltest.append(labelset[x+ltest])


'''neigh = KNeighborsClassifier(n_neighbors=2)
neigh.fit(traindata,labeltrain) 

testpred=neigh.predict(testdata)'''
clf = svm.SVC()
clf.fit(traindata, labeltrain) 
testpred=clf.predict(testdata)

#labeltest=map(int,labeltest)
#estpred=map(int,testpred)
print labeltest
print testpred

print accuracy_score(labeltest,testpred)



