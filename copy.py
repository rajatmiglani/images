import glob 
import shutil
import zipfile
import os

locations = []

location = glob.iglob('pdftoimage/*/*.jpg')
for i in location:
	locations.append(i)

for i in locations:
	shutil.copy2(i, 'cheques/')