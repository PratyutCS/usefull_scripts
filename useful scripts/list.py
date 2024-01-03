import os
from os import listdir
from os.path import isfile, join

mypath="C:\\Users\\praty\\OneDrive\\Desktop\\naac"
ndir = [mypath+'\\'+f for f in listdir(mypath) if os.path.isdir(mypath+'\\'+f)]
print(ndir)
def dirlist(path):
	of = [f for f in listdir(path)]
	ofo= [f for f in listdir(path)]
	
	
	
	for i in range(len(of)):
		for j in range(len(of[i])):
			if(of[i][j:j+1]==' '):
				str1=of[i][0:j]
				str3=of[i][j+1:len(of[i])]
				str2="_"
				fstr=str1+str2+str3
				of[i]=fstr

	for j in range(len(ofo)):
		ostr=path+"\\"+ofo[j]
		nstr=path+"\\"+of[j]
		os.rename(ostr, nstr)
	
	
	
	ddir = [path+'\\'+f for f in listdir(path) if os.path.isdir(path+'\\'+f)]
	return ddir
i=0
while(i<len(ndir)):
	ddir=dirlist(ndir[i])
	for j in range(len(ddir)):
		ndir.append(ddir[j])
	for k in range(len(ndir)):
		print(ndir[k])
	i+=1