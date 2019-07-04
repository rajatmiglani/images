from PIL import Image
from PIL import ImageDraw
import glob 
import random
import csv

im = Image.new("RGB", (1920,1080), "white")
draw = ImageDraw.Draw(im)

data = []

names = glob.iglob('tr-small/*.jpg')
for i in names:
	img = i
	data.append(img)

back = []
rand = glob.iglob('back/*.jpg')
for i in rand:
	img = i
	back.append(img)
# print(back)
for i in range(700):
	name = 'single/xuz' + str(i) + '.jpg'
	back_number = random.randint(0,len(back)-1)
	# print(back_number)
	icon2 = Image.open(back[back_number]) 
	x2, y2 = icon2.size
	im.paste(icon2, (0, 0, x2, y2))

	cheque_number = random.randint(0,len(data)-1)
	icon = Image.open(data[cheque_number])
	# get the correct size
	x, y = icon.size
	# print(x)
	x_rand = random.randint(0, 1920 - x)
	y_rand = random.randint(0, 1080 - y)
	im.paste(icon, (x_rand, y_rand, x_rand + x, y_rand + y))

	# name = data[cheque_number][9:]
	row = [name,538,256,'cheques',x_rand,y_rand,x_rand + x,y_rand + y]

	with open ('train_labels.csv','a') as csvFile: 
		writer = csv.writer(csvFile)
		writer.writerow(row)

	im.save(name, "JPEG") 