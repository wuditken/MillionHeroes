import os, random

def press(recommand, size):
	os.system("adb shell getevent -p")
	# 获取坐标，得到x_max和y_max
	x_max = 800
	y_max = 1000
	x = x_max/2+(random.random()-0.5)*10
	y_dict = {
		1: '2',
		2: '3',
		3: '4',
		4: '5'
	}
	try:
		os.system("adb shell input tap "+x+' '+y_dict(recommand))
		return 1
	except:
		return 0
	