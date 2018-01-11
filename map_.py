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


	return results
