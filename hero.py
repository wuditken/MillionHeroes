import urllib.request, sys,base64,json,os,time,pyperclip,cropimage,ocr,map_

def million():
	start = time.time()
	os.system("adb shell /system/bin/screencap -p /sdcard/million/screenshot.png") 
	os.system("adb pull /sdcard/million/screenshot.png d:/screenshot.png")  



	image_file = '11.jpg'
	question_and_op = cropimage.crop(image_file)

	question_image = question_and_op[0]
	op_a = question_and_op[1]
	op_b = question_and_op[2]
	op_c = question_and_op[3]

	print ('')

	question = ocr.ocr(question_image)
	op_a = ocr.ocr(op_a)
	op_b = ocr.ocr(op_b)
	op_c = ocr.ocr(op_c)
	
	print (question)
	print (op_a)
	print (op_b)
	print (op_c)
	
	result = map_.map_baidu(question)

	end = time.time()
	print('程序用时：'+str(end-start)+'秒')

if __name__ == '__main__':
	million()