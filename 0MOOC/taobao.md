# 用Python实现从命令行进行淘宝搜索

## 背景
作为马云门前的败家娘们/爷们，在淘宝上搜东西是常做的事。

对于搜索，我们一般的流程是：
+ 打开浏览器
+ 打开淘宝
+ 输入搜索关键词

如果能用python写个脚本简化这个流程，那想必是极好的。

最后想达到的结果是，在命令行输入
```
python search_taobao.py 关键词1 关键词2 ...
```
就能直接打开淘宝搜索网页，并搜索关键词


## 构思
要达到上述效果，我想到的逻辑步骤是：
1. 读取命令行的参数
2. 打开浏览器，打开淘宝页面
3. 搜索关键词

经过google大法之后，了解到  
对于步骤1，标准库`sys`中
`argv`变量可以储存python命令后的参数（包括第一个参数，文件名search_taobao.py)

对于步骤2，标准库`webbrowser`中`open`方法可以打开指定网页，例如
```python
import webbrowser
webbrowser.open('www.taobao.com')
```

对于步骤3，可以使用[Query String](https://en.wikipedia.org/wiki/Query_string)在打开网址时就把关键词post上去。

对于淘宝，相应的做法是输入`https://s.taobao.com/search?q={keywords}`，将{keywords}替换成想输入的关键词就行。  

## 实现
综上所思，初步写的解决方案如下
```python
# file name "search_taobao.py"
import sys
import webbrowser

keywords = sys.argv[1:]

url = "https://s.taobao.com/search?q="
for i in keywords:
    url += i + "+"
url = url[:-1] #remove the last '+''
webbrowser.open(url)
```

命令行输入
```
python search_taobao.py python
```
成功打开淘宝搜索

尝试输入多个关键词
```
python search_taobao.py python Django
```
也搜索成功

## 问题
虽然使用英文关键词时搜索成功，但在使用中文关键词时出现了bug  
例如，搜索关键词`书` 
```
python search_taobao.py 书
```

在打开的淘宝页面，搜索的关键词却变成了`%C2%A0È`

## debug
首先这肯定是中文编码的问题，因此尝试在文件开头加一句
```
# coding=utf-8
```
测试之后问题依然存在

然后猜测是sys.argv读取中文参数时出现问题  
在脚本中加入print语句  
```python
# coding=utf-8
import sys
import webbrowser

keywords = sys.argv[1:]

url = "https://s.taobao.com/search?q="
for i in keywords:
    print i # Debug
    url += i + "+"
url = url[:-1] #remove the last '+''
# webbrowser.open(url)
```
发现output中的中文显示正常  

然后猜测是英文字符串和中文字符串concatenate过程中出现问题  
改脚本为
```python
# coding=utf-8
import sys
import webbrowser

keywords = sys.argv[1:]

url = "https://s.taobao.com/search?q="
for i in keywords:
    url += i + "+"
    print url # Debug
url = url[:-1] #remove the last '+''
# webbrowser.open(url)
```
测试发现output中文显示正常

最后猜测是`webbrowser.open`函数在使用参数含中文时会有bug  
直接运行如下脚本  
```python
import webbrowser
webbrowser.open("https://s.taobao.com/search?q=书")
```
结果证实了我的猜测，问题出在`webbrowser.open`上

## 改进
为了解决这个bug，几轮google之后还是没找到解决`webbrowser.open`对中文不支持的问题。但在这个过程中，找到了`subprocess`库，这个库中`call`函数可以让python直接运行命令行命令，另外还查到了命令行的open命令可以直接在浏览器中打开网页。遂把代码改写如下
```python
# coding=utf-8
import sys
import subprocess

keywords = sys.argv[1:]

url = "https://s.taobao.com/search?q="
for i in keywords:
    url += i + "+"
url = url[:-1]
subprocess.call(["open", url])
```
之后测试中文关键词、多关键词都运行成功，算是实现了设想的功能。

ps： Mac下面，可以在命令行多加一句`say`的命令，用于命令执行完进行提示。例如
```
python search_taobao.py 书;say mission complete
```
执行之后，系统会说mission complete，瞬间成就感爆表。

pps: 后来发现用os.system()调用命令行命令也行
代码可改为
```python
# coding:utf-8
import os
import sys

keywords = sys.argv[1:]

url = "https://s.taobao.com/search?q="
for i in keywords:
    url += i + "+"
url = url[:-1]
os.system("open "+url)
```
