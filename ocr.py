import urllib.request, sys, base64, json, os
from aip import AipOcr

def ocr(image):
	'''
	汉王ocr 涨价涨价了。。
	host = 'http://text.aliapi.hanvon.com'
	path = '/rt/ws/v1/ocr/text/recg'
	method = 'POST'
	appcode = 'a962e94260ee4043b824d2f40c126d8e'    #汉王识别appcode（填你自己的）
	querys = 'code=74e51a88-41ec-413e-b162-bd031fe0407e'
	bodys = {}
	url = host + path + '?' + querys

	f=open("D:\LDJ\misc\misc\MillionHero\MillionHeroes-master\crop\\"+image,'rb') 
	ls_f=base64.b64encode(f.read())
	f.close()
	s = bytes.decode(ls_f) 

	bodys[''] = "{\"uid\":\"118.12.0.12\",\"lang\":\"chns\",\"color\":\"color\",\"image\":\""+s+"\"}"
	post_data = bodys['']
	request = urllib.request.Request(url, str.encode(post_data))
	request.add_header('Authorization', 'APPCODE ' + appcode)
	request.add_header('Content-Type', 'application/json; charset=UTF-8')
	request.add_header('Content-Type', 'application/octet-stream')
	response = urllib.request.urlopen(request)
	content =  bytes.decode(response.read())
	if (content):
		decode_json = json.loads(content)
		#print(decode_json['textResult'])


	#pyperclip.copy(''.join(decode_json['textResult'].split()))
	keyword = ''.join(decode_json['textResult'].split())    #识别的问题文本

	'''
	""" （百度ocr）你的 APPID AK SK """
	APP_ID = '10675766'
	API_KEY = '3LXbCnaZ5TUx9T5hpzyP7pw2'
	SECRET_KEY = 'TfKCxzZxjyTxHhOm1k2o2C5RCHiW52tl'
	client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

	def get_file_content(filePath):
		with open(filePath, 'rb') as fp:
			return fp.read()
	image = get_file_content(r"D:\LDJ\misc\misc\MillionHero\MillionHeroes-master\crop\\"+image)
	respon = client.basicGeneral(image)
	titles = respon['words_result']          #获取问题
	ans = ''
	for title in titles:
		  ans = ans +title['words']

	return ans