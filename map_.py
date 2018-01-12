import baiduSearch, test
from test import Ai

def map_baidu(keyword, mode):
	# mode=1则输出搜索结果
	convey = 'n'

	if convey == 'y' or convey == 'Y':
		results = baiduSearch.search(keyword, convey=True)
	elif convey == 'n' or convey == 'N' or not convey:
		results = baiduSearch.search(keyword)
	else:
		print('输入错误')
		exit(0)
	
	search_num = results[0]

	if mode == 1:
		count = 0
		for result in results[1:]:
			#print('{0} {1} {2} {3} {4}'.format(result.index, result.title, result.abstract, result.show_url, result.url))  # 此处应有格式化输出
			print('{0}'.format(result.abstract))  # 此处应有格式化输出
			count=count+1
			if(count == 2):
				break
	return search_num

def map_options(question, option):
	ai=Ai(question, option)
	result = ai.search()
	return result