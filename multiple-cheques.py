from PIL import Image
from PIL import ImageDraw
import glob 
import random
# import csv

im = Image.new("RGB", (1920,1080), "white")
draw = ImageDraw.Draw(im)

data = []

names = glob.iglob('resized/*.jpg')
for i in names:
	img = i
	data.append(img)

back = []
rand = glob.iglob('back/*.jpg')
for i in rand:
	img = i
	back.append(img)
# print(back)
for i in range(1):
	name = '3xuz' + str(i) + '.jpg'
	back_number = random.randint(0,len(back)-1)
	# print(back_number)
	icon = Image.open(back[back_number]) 
	x, y = icon.size
	im.paste(icon, (0, 0, x, y))

	cheque_number = i
	icon1 = Image.open(data[cheque_number])
	# get the correct size
	x1, y1 = icon1.size
	x_rand1 = random.randint(0, 1920 - x1)
	y_rand1 = random.randint(0, 1080 - y1)
	im.paste(icon1, (x_rand1, y_rand1, x_rand1 + x1, y_rand1 + y1))
	# name1 = data[cheque_number][9:]

	cheque_number = i+1
	icon2 = Image.open(data[cheque_number])
	# get the correct size
	x2, y2 = icon2.size
	x_rand2 = random.randint(0, 1920 - x2)
	y_rand2 = random.randint(0, 1080 - y2)
	im.paste(icon2, (x_rand2, y_rand2, x_rand2 + x2, y_rand2 + y2))
	# name2 = data[cheque_number][9:]

	cheque_number = i+2
	icon3 = Image.open(data[cheque_number])
	# get the correct size
	x3, y3 = icon3.size
	x_rand3 = random.randint(0, 1920 - x3)
	y_rand3 = random.randint(0, 1080 - y3)
	im.paste(icon3, (x_rand3, y_rand3, x_rand3 + x3, y_rand3 + y3))

	# row1 = [name,538,256,'cheques',x_rand1,y_rand1,x_rand1 + x1,y_rand1 + y1]
	# row2 = [name,538,256,'cheques',x_rand2,y_rand2,x_rand2 + x2,y_rand2 + y2]
	# row3 = [name,538,256,'cheques',x_rand3,y_rand3,x_rand3 + x3,y_rand3 + y3]

	# with open ('train3_labels.csv','a') as csvFile: 
	# 	writer = csv.writer(csvFile)
	# 	writer.writerow(row3)

	# if (x_rand2 >= x_rand3 + x3) or (y_rand2 >= y_rand3 + y3) or (x_rand3 >= x_rand2 + x2) or (y_rand3 >= y_rand2 + y2):
	# 	with open ('train3_labels.csv','a') as csvFile: 
	# 		writer = csv.writer(csvFile)
	# 		writer.writerow(row2)

	# 	if ((x_rand1 >= x_rand3 + x3) or (x_rand3 >= x_rand1 + x1) or (y_rand1 >= y_rand3 + y3) or (y_rand3 >= y_rand1 + y1)) and ((x_rand1 >= x_rand2 + x2) or (x_rand2 >= x_rand1 + x1) or (y_rand1 >= y_rand2 + y2) or (y_rand2 >= y_rand1 + y1)):
	# 		with open ('train3_labels.csv','a') as csvFile: 
	# 			writer = csv.writer(csvFile)
	# 			writer.writerow(row1)

	# else:
	# 	if (x_rand1 >= x_rand3 + x3) or (x_rand3 >= x_rand1 + x1) or (y_rand1 >= y_rand3 + y3) or (y_rand3 >= y_rand1 + y1):
	# 		with open ('train3_labels.csv','a') as csvFile: 
	# 			writer = csv.writer(csvFile)
	# 			writer.writerow(row1)

		# print(x_rand1, x_rand2, x1, y_rand1, y_rand2, y1)
		# row2 = [name,538,256,'cheques',x_rand2,y_rand2,x_rand2 + x2,y_rand2 + y2]
		# with open ('train3_labels.csv','a') as csvFile: 
			# writer = csv.writer(csvFile)
			# writer.writerow(row2)
	im.save(name, "JPEG") 