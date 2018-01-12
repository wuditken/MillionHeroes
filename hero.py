import urllib.request, sys,base64,json,os,time,baiduSearch,screenshot,re
from PIL import Image
from common import config
#配置appcode
config = config.open_accordant_config()

start = time.time()
# 开始截图
screenshot.check_screenshot()
screenshot.pull_screenshot()
host = 'http://text.aliapi.hanvon.com'
path = '/rt/ws/v1/ocr/text/recg'
method = 'POST'
appcode = config['appcode']    #汉王识别appcode（填你自己的）
querys = 'code=74e51a88-41ec-413e-b162-bd031fe0407e'
bodys = {}
url = host + path + '?' + querys

im = Image.open(r"./screenshot.png")   

img_size = im.size
w = im.size[0]
h = im.size[1]
print("xx:{}".format(img_size))

region = im.crop((70,300, w-70,600))    #裁剪的区域 百万超人 手机1080*1920 高度范围300~600
region.save("./crop_test1.png")


image_contrasted.save("./crop_test.png")
f=open('./crop_test.png','rb') 
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
    print(decode_json['textResult'])

text=decode_json['textResult']

text = re.sub(r"\d+.","",text,1)

qm_pos=text.find("?")
#print qm_pos
if qm_pos==-1:
    sys.exit() 
question=''.join(text[0:qm_pos].split())
#print (question)

answers=text[(qm_pos+1):].split(u"\n")
answers=list(set(answers))
if u'\r' in answers:
    answers.remove(u'\r')
if u'' in answers:
    answers.remove(u'')
#print (answers)


count = 0
results = baiduSearch.search(question)
content=''
for result in results:
    #print('{0} {1} {2} {3} {4}'.format(result.index, result.title, result.abstract, result.show_url, result.url))  # 此处应有格式化输出
    tmp='{0}'.format(result.abstract)  # 此处应有格式化输出
    print(tmp)  # 此处应有格式化输出
    content=tmp+content 
    count=count+1
    if(count == 6):
        break


arr=[]
for ans in answers:
    tmp=ans[:-1];
    arr.append(content.count(tmp));    

sum_num=sum(arr)

if(sum_num==0):
    sys.exit();

idx=arr.index(max(arr))
print ('**************************************************')
print ('最有可能的答案是:')
print (answers[idx])

print ('**************************************************')
end = time.time()
print('程序用时：'+str(end-start)+'秒')
#print(keyword)
