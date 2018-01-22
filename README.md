# 百万英雄答题助手
----------------------------------------------------------------------------------------------

# 用的是python3.6版本
参考微信跳一跳助手，使用adb截图。

# 把问题区域裁剪出来后用百度的ocr识别出文本，然后调用百度搜索（把搜索到的前两个答案显示在屏幕）

# 整个程序运行完估计5秒左右，还可以有时间答题（---）

# 使用教程
1,安装ADB 驱动，可以到[这里下载](https://adb.clockworkmod.com/)<br />
   安装 ADB 后，请在环境变量里将 adb 的安装路径保存到 PATH 变量里，确保 adb 命令可以被识别到
  
2.需要安装模块 在命令行输入(pip install 模块名称) 模块名称： baidu-aip  lxml  Pillow  requests bs4

3.在hero.py里填写自己百度ocr的APPid</br>
百度ocr：http://ai.baidu.com/tech/ocr/general

4.连接手机<br>运行python hero.py (搜索百度的内容) <br>或test文件下的hero.py（搜素内容并统计词频）<br />
（只支持安卓手机）
# 效果图
![截图](http://chuantu.biz/t6/198/1515261841x-1566687351.png)
![截图](https://github.com/wuditken/MillionHeroes/blob/master/test/1.PNG?raw=true)


一开始也想要tesseract来识别，但是经过测试太慢了要用10秒左右。
# 大家有时间的话可以试试把它弄成全自动的

有一个思路 就是把问题的选项答案也给识别出来，然后把百度搜出来的答案匹配选项答案，如果有答案直接一个模拟点击.

# 交流学习
### QQ群:675516092



