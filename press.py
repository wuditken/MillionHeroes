import os, random

def press(recommand, size):
	os.system("adb shell getevent -p")
	# 获取坐标，得到x_max和y_max
	x = x_max/2+(random.random()-0.5)*10
	y_dict = {
		1: 
		2: 
		3: 
		4: 
	}
	try:
		os.system("adb shell input tap "+x+' '+y_dict(recommand))
		return 1
	except:
		return 0
	