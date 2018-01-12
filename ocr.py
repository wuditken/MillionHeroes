import urllib.request, sys, base64, json, os
from aip import AipOcr

def ocr(path, image):
	""" （百度ocr）你的 APPID AK SK """
	APP_ID = '10675766'
	API_KEY = '3LXbCnaZ5TUx9T5hpzyP7pw2'
	SECRET_KEY = 'TfKCxzZxjyTxHhOm1k2o2C5RCHiW52tl'
	client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

	def get_file_content(filePath):
		with open(filePath, 'rb') as fp:
			return fp.read()
	image = get_file_content(path+image)
	respon = client.basicGeneral(image)
	titles = respon['words_result']          #获取问题
	question = ''
	option = ['','','','','','']
	countone = 0
	count = 0
	for title in titles:
	      countone+=1
	      if(countone >=len(titles)-2):
	        option[count] = title['words']
	        count+=1
	      else:
	        question = question +title['words']

	return [question, option]