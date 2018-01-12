import urllib.request, sys, base64, json, os, time, pyperclip, cropimage, ocr, map_, auto_result, press
import test as ai

def million():
	start = time.time()

	# 截屏
	# TODO 参考这个代码加快截屏速度 https://github.com/baitisj/android_screen_mirror

	# path = 'd:/million/'
	path = 'D:/LDJ/misc/misc/MillionHero/MillionHeroes-master'
	file = 'screen.png'
	os.system("adb shell /system/bin/screencap -p /sdcard/million/screenshot.png") 
	os.system("adb pull /sdcard/million/screenshot.png "+path+'/origin/'+file)

	# 裁剪问题和选项
	# TODO 自适配分辨率
	crop = cropimage.crop(path, file)
	question_and_op = crop[0]
	size = crop[1]

	end = time.time()
	print('裁剪用时：'+str(end-start)+'秒')

	print ('')

	# 识别问题和选项
	all_ocr = ocr.ocr(path+'/crop/', question_and_op)
	question = all_ocr[0]
	option_a = all_ocr[1][0]
	option_b = all_ocr[1][1]
	option_c = all_ocr[1][2]
	option_d = all_ocr[1][3]

	step_1 = time.time()
	print('题目识别用时：'+str(step_1-start)+'秒')

	# 搜索问题
	results = map_.map_baidu(question, 1)

	step_2 = time.time()
	print('题目搜索用时：'+str(step_2-step_1)+'秒')

	print ('----------------------------')

	dict_op = {
		1: 'A',
		2: 'B',
		3: 'C',
		4: 'D'
	}

	# 综合问题和选项搜索结果
	result = auto_result.auto(question, [option_a, option_b, option_c, option_d])
	print (option_a+': '+str(result[0][0]))
	print (option_b+': '+str(result[0][1]))
	print (option_c+': '+str(result[0][2]))
	if option_d != '':
		print (option_d+': '+str(result[0][3]))
	recommand = result[1]
	print (dict_op[recommand])

	step_4 = time.time()
	print('选项搜索用时：'+str(step_4-step_2)+'秒')

	# 模拟按下选项
	print (press.press(recommand, size))

	end = time.time()
	print('程序用时：'+str(end-start)+'秒')

# 挂机控制
def auto_run():
	pass

if __name__ == '__main__':
	million()