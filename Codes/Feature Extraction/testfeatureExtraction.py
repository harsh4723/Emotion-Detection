import os
import csv
import random as rn
import math
import operator 
import numpy as np
import audioBasicIO
import audioFeatureExtraction

dire =r"G:\5th sem\ee320 DSP\project\csv\newdata\dataset\testdata\angry"
c=1
for filename in os.walk(dire):
	for x in filename[2]:
		label1=[]
		label=[]
		file=filename[0]+"\\"+str(x)
		[Fs, x] = audioBasicIO.readAudioFile(file)
		F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.50*Fs, 0.25*Fs)
		for i in range(len(F[0])):
			label1.append(3)
		label.append(label1)
		G=np.append(F,label,axis=0)
		loc=r"G:\5th sem\ee320 DSP\project\csv\newdata\dataset\testdata\angrycsv\an"+str(c)+".csv"
		c=c+1
		np.savetxt(loc, G,delimiter=",")

dire =r"G:\5th sem\ee320 DSP\project\csv\newdata\dataset\testdata\sad"
c=1

for filename in os.walk(dire):
	for x in filename[2]:
		label=[]
		label1=[]
		file=filename[0]+"\\"+str(x)
		[Fs, x] = audioBasicIO.readAudioFile(file)
		F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.50*Fs, 0.25*Fs)
		#print F
		for i in range(len(F[0])):
			label1.append(1)
		label.append(label1)
		G=np.append(F,label,axis=0)
		#print G
		loc=r"G:\5th sem\ee320 DSP\project\csv\newdata\dataset\testdata\sadcsv\sd"+str(c)+".csv"
		c=c+1
		np.savetxt(loc,G,delimiter=",")



dire =r"G:\5th sem\ee320 DSP\project\csv\newdata\dataset\testdata\happy"
c=1
for filename in os.walk(dire):
	for x in filename[2]:
		label1=[]
		label=[]
		file=filename[0]+"\\"+str(x)
		[Fs, x] = audioBasicIO.readAudioFile(file)
		F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.50*Fs, 0.25*Fs)
		for i in range(len(F[0])):
			label1.append(2)
		label.append(label1)
		#print label
		G=np.append(F,label,axis=0)
		loc=r"G:\5th sem\ee320 DSP\project\csv\newdata\dataset\testdata\happycsv\hp"+str(c)+".csv"
		c=c+1
		np.savetxt(loc,G,delimiter=",")


dire =r"G:\5th sem\ee320 DSP\project\csv\newdata\dataset\testdata\neutral"
c=1
for filename in os.walk(dire):
	for x in filename[2]:
		label1=[]
		label=[]
		file=filename[0]+"\\"+str(x)
		[Fs, x] = audioBasicIO.readAudioFile(file)
		F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.50*Fs, 0.25*Fs)
		for i in range(len(F[0])):
			label1.append(4)
		label.append(label1)
		#print label
		G=np.append(F,label,axis=0)
		loc=r"G:\5th sem\ee320 DSP\project\csv\newdata\dataset\testdata\neutralcsv\nu"+str(c)+".csv"
		c=c+1
		np.savetxt(loc,G,delimiter=",")