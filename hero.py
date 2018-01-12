import urllib.request, sys,base64,json,os,time,baiduSearch,threading
from PIL import Image,ImageEnhance
from common import config,screenshot
from aip import AipOcr
from tools import aitext

def get_screenshot():
  screenshot.pull_screenshot()

  im = Image.open(r"./screenshot.png")    #导入手机截图  
  img_size = im.size
  w = im.size[0]
  h = im.size[1]
  print("xx:{}".format(img_size))

  region = im.crop((70,300, w-70,600))    #裁剪的区域,可以自己修改
  enh_con = ImageEnhance.Contrast(region)   
  image_contrasted = enh_con.enhance(1.5)
  image_contrasted.save("./crop_test1.png")   #提取题目截图

def get_answer(filePath):
    with open(filePath, 'rb') as fp:
      image = fp.read()
      respon = client.basicGeneral(image)
      titles = respon['words_result']          #获取问题
      ans = ''
      for title in titles:
            ans = ans +title['words']
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


def get_ai_answer(filePath):
  with open(filePath, 'rb') as fp:
      image = fp.read()
      respon = client.basicGeneral(image)
      titles = respon['words_result']          #获取问题
      issue = ''
      answer = ['','','','','','']
      countone = 0
      answercount = 0
      for title in titles:
            countone+=1
            if(countone >=len(titles)-2):
              answer[answercount] = title['words']
              answercount+=1
            else:
              issue = issue +title['words']

      print(issue)       #打印问题
      print('  A:'+answer[0]+' B:'+answer[1]+' C:'+answer[2])       #打印问题

      keyword = issue    #识别的问题文本
      ai=aitext.Ai(issue,answer)
      ai.search()




# def show_answer(choice):
#   if int(choice) == 1:
#     get_ai_answer(r"./crop_test1.png")
#   else:
#     get_answer(r"./crop_test1.png")

# choice = input("input: 词频显示-1 内容显示-2\n")
# show_answer(choice)


threads = []
t1 = threading.Thread(target=get_ai_answer,args=(r"./crop_test1.png",))
threads.append(t1)
t2 = threading.Thread(target=get_answer,args=(r"./crop_test1.png",))
threads.append(t2)


if __name__ == '__main__':
  #导入配置百度ocr
  config = config.open_accordant_config()
  APP_ID = config['app_id']
  API_KEY = config['app_key']
  SECRET_KEY = config['app_secret']
  # 开始截图
  start = time.time()
  # screenshot.check_screenshot()
  get_screenshot()
  client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
  
  for t in threads:
    t.start()
  
  t.join()
  
  end = time.time()
  print('程序用时：'+str(end-start)+'秒')

