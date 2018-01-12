# -*- coding:utf-8 -*-

import urllib.request, sys,base64,json,os,time,baiduSearch,screenshot,re
from PIL import Image
from common import config
from functools import partial
from common.baiduocr import get_text_from_image as bai_get_text


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

get_text_from_image = partial(bai_get_text,
                              app_id=config['app_id'],
                              app_key=config['app_key'],
                              app_secret=config['app_secret'],
                              api_version=config['api_version'][0],
                              timeout=5)

def start_answer():
    input('题目出现后按回车：\n')

    start = time.time()
    # 开始截图
    #screenshot.check_screenshot()

    screenshot.pull_screenshot()

    im = Image.open(r"./screenshot.png")
    screen_end = time.time()
    print('截图用时：' + str(screen_end - start) + '秒')

    # region = im.crop((70,300, 1010,600))    #裁剪的区域 百万超人 手机1080*1920 高度范围300~600 // 芝士超人250-350
    # region = im.crop((70,200,650,400))    #裁剪的区域 百万超人 手机720*1080 高度范围300~600 // 芝士超人250-350

    region = (tuple(region_kind))
    region = im.crop(region)
    region.save("./crop_test1.png")

    f = open('./crop_test1.png', 'rb')
    img_data = f.read()
    f.close()

    ocr_start =time.time()

    keyword = get_text_from_image(
        image_data=img_data,
    )
    print(keyword)
    ocr_end = time.time()
    print('OCR用时：' + str(ocr_end - ocr_start) + '秒')

    try:
        baiduSearch.search(keyword)
    except:
        print('error')
        pass

    end = time.time()
    print('程序用时：' + str(end - start) + '秒')
    print(keyword)


#---- 主程序
while(1):
    start_answer()


