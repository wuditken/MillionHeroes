import urllib.request, sys,base64,json,os,time,baiduSearch
from PIL import Image
from aip import AipOcr

start = time.time()
os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png") 
os.system("adb pull /sdcard/screenshot.png ./screenshot.png")
'''
汉王ocr 涨价涨价了。。
host = 'http://text.aliapi.hanvon.com'
path = '/rt/ws/v1/ocr/text/recg'
method = 'POST'
appcode = 'a962e94260ee4043b824d2f40c126d8e'    #汉王识别appcode（填你自己的）
querys = 'code=74e51a88-41ec-413e-b162-bd031fe0407e'
bodys = {}
url = host + path + '?' + querys
'''
""" （百度ocr）你的 APPID AK SK """
APP_ID = '10673785'
API_KEY = 'FqRvrpPwhSNXt2FhT6d3dXfc'
SECRET_KEY = 'UIu2qOPHXENScjr1yzAyXQgNkLQzkcdc'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)



im = Image.open(r"./screenshot.png")   

img_size = im.size
w = im.size[0]
h = im.size[1]
print("xx:{}".format(img_size))

region = im.crop((70,200, w-70,700))    #裁剪的区域
region.save(r"./crop_test1.png")



""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
image = get_file_content(r"./crop_test1.png")
respon = client.basicGeneral(image)   #用完500次后可改respon = client.basicAccurate(image) 
titles = respon['words_result']          #获取问题
ans = ''
for title in titles:
      ans = ans +title['words']

tissue = ans[1:2]
if str.isdigit(tissue):            #去掉题目索引
     ans = ans[3:]   
else:
     ans = ans[2:]

print(ans)       #打印问题

keyword = ans    #识别的问题文本

convey = 'n'

if convey == 'y' or convey == 'Y':
    results = baiduSearch.search(keyword, convey=True)
elif convey == 'n' or convey == 'N' or not convey:
    results = baiduSearch.search(keyword)
else:
    print('输入错误')
    exit(0)
count = 0
for result in results:
    #print('{0} {1} {2} {3} {4}'.format(result.index, result.title, result.abstract, result.show_url, result.url))  # 此处应有格式化输出
	print('{0}'.format(result.abstract))  # 此处应有格式化输出
	count=count+1
	if(count == 2):      #这里限制了只显示2条结果，可以自己设置
		break

end = time.time()
print('程序用时：'+str(end-start)+'秒')
