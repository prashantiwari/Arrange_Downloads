import os
import shutil
import sys
from datetime import datetime
from time import sleep
todaystring = str(datetime.now())
todaystring = todaystring[:10]
lis=[]
i=1
destinationDir='C:\Users\Prashant Tiwari\Downloads\Temp\DownloadedOn'
destinationDir = destinationDir + todaystring

while os.path.exists(destinationDir):
	destinationDir=destinationDir+str(i)
	i+=1
os.makedirs(destinationDir)
lis=os.listdir('C:\Users\Prashant Tiwari\Downloads\Temp')
print lis
for x in lis:
	if x==__file__:
		continue
	shutil.move(x, destinationDir)

destinationpython = destinationDir + '\ToDatedFolder.py'
print destinationpython

sleep(5)

shutil.copy('C:\Users\Prashant Tiwari\Downloads\Temp\ToDatedFolder.py','C:\Users\Prashant Tiwari\Downloads\Temp')
