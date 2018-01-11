import baiduSearch

def map_baidu(keyword):
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
		if(count == 2):
			break

	return 0
