import urllib.request, sys, base64, json, os

def ocr(image):
	host = 'http://text.aliapi.hanvon.com'
	path = '/rt/ws/v1/ocr/text/recg'
	method = 'POST'
	appcode = '8b9a002246d6451c96cc5d0bc22b705c'    #汉王识别appcode（填你自己的）
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
	return keyword