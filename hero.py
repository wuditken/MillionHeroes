import urllib.request, sys,base64,json,os,time,pyperclip,cropimage,ocr,map_

def million():
	start = time.time()
	os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png") 
	os.system("adb pull /sdcard/screenshot.png d:/million/origin/1.png")  



	image_file = '1.png'
	question_and_op = cropimage.crop(image_file)

	question_image = question_and_op[0]
	op_a = question_and_op[1]
	op_b = question_and_op[2]
	op_c = question_and_op[3]

	print ('')

	question = ocr.ocr(question_image)

	'''
	print (question)
	print (op_a)
	print (op_b)
	print (op_c)
	'''

	results = map_.map_baidu(question)
	count = 0
	for result in results:
		#print('{0} {1} {2} {3} {4}'.format(result.index, result.title, result.abstract, result.show_url, result.url))  # 此处应有格式化输出
		print('{0}'.format(result.abstract))  # 此处应有格式化输出
		count=count+1
		print ("")
		if(count == 2):
			break

	op_a = ocr.ocr(op_a)
	op_b = ocr.ocr(op_b)
	op_c = ocr.ocr(op_c)

	print ('----------------------------')
	print (op_a)
	map_.map_baidu(question+' '+op_a)
	print (op_b)
	map_.map_baidu(question+' '+op_b)
	print (op_c)
	map_.map_baidu(question+' '+op_c)

	end = time.time()
	print('程序用时：'+str(end-start)+'秒')

if __name__ == '__main__':
	million()