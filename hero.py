# -*- coding:utf-8 -*-

import urllib.request, sys,base64,json,os,time,baiduSearch,screenshot,re
from PIL import Image
from common import config
from functools import partial
from common.baiduocr import get_text_from_image as bai_get_text
#配置appcode

index = input("input: 百万英雄-1 冲顶大会-2 芝士超人-3\n")
config = config.open_accordant_config()
region_kind = config['region_million']
if index=='1':
    region_kind = config['region_million']
elif index=='2':
    region_kind = config['region_top']
elif index=='3':
    region_kind = config['region_super']
else:
    print('输入格式错误')

def start_answer():
    input('题目出现后按回车：\n')

    start = time.time()
    # 开始截图
    # screenshot.check_screenshot()
    # screenshot.pull_screenshot()
    host = 'http://text.aliapi.hanvon.com'
    path = '/rt/ws/v1/ocr/text/recg'
    method = 'POST'
    appcode = config['appcode']  # 汉王识别appcode（填你自己的）
    querys = 'code=74e51a88-41ec-413e-b162-bd031fe0407e'
    bodys = {}
    url = host + path + '?' + querys

    im = Image.open(r"./screenshot.png")

    # 识别截图大小 省略
    # img_size = im.size
    # w = im.size[0]
    # h = im.size[1]
    # print("xx:{}".format(img_size))

    # region = im.crop((70,300, 1010,600))    #裁剪的区域 百万超人 手机1080*1920 高度范围300~600 // 芝士超人250-350
    # region = im.crop((70,200,650,400))    #裁剪的区域 百万超人 手机720*1080 高度范围300~600 // 芝士超人250-350

    region = (tuple(region_kind))
    region = im.crop(region)
    region.save("./crop_test1.png")

    f = open('./crop_test1.png', 'rb')
    img_data = f.read()
    #ls_f = base64.b64encode(f.read())
    f.close()
    #s = bytes.decode(ls_f)

    #print(type(s))

    # bodys[''] = "{\"uid\":\"118.12.0.12\",\"lang\":\"chns\",\"color\":\"color\",\"image\":\"" + s + "\"}"
    # post_data = bodys['']
    # request = urllib.request.Request(url, str.encode(post_data))
    # request.add_header('Authorization', 'APPCODE ' + appcode)
    #
    # request.add_header('Content-Type', 'application/json; charset=UTF-8')
    # request.add_header('Content-Type', 'application/octet-stream')
    # response = urllib.request.urlopen(request)
    # content = response.read()
    # if (content):
    #     decode_json = json.loads(content.decode('utf-8'))
    #     print(decode_json['textResult'])

    #print(config['api_version'][0])

    get_text_from_image = partial(bai_get_text,
                                  app_id=config['app_id'],
                                  app_key=config['app_key'],
                                  app_secret=config['app_secret'],
                                  api_version=config['api_version'][0],
                                  timeout=5)

    # text_binary = analyze_current_screen_text(
    #     directory=data_directory,
    #     compress_level=image_compress_level[0]
    # )
    keyword = get_text_from_image(
        image_data=img_data,
    )
    print(keyword)


    # keyword = ''.join(decode_json['textResult'].split())  # 识别的问题文本
    # keyword = re.sub(r"\d+.", "", keyword, 1)
    convey = 'n'
    results = None

    if convey == 'y' or convey == 'Y':
        try:
            results = baiduSearch.search(keyword, convey=True)
        except:
            print('error')
            pass
    elif convey == 'n' or convey == 'N' or not convey:
        try:
            results = baiduSearch.search(keyword)
        except:
            print('error')
            pass
    else:
        print('输入错误')
        exit(0)
    count = 0
    if results is not None:
        for result in results:
            #print('{0} {1} {2} {3} {4}'.format(result.index, result.title, result.abstract, result.show_url,result.url))  # 此处应有格式化输出
            print('{0}'.format(result.abstract))  # 此处应有格式化输出
            # count=count+1
            if (count == 2):
                break
    else:
        print('失败了')
    end = time.time()
    print('程序用时：' + str(end - start) + '秒')
    print(keyword)


#---- 主程序
while(1):
    start_answer()


