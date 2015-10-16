# 时间格式转换脚本

## 背景
对于时间格式（也包括日期格式），不同人习惯于不同写法，例如有的人用“年/月/日”，而有的人用“月/日/年”。因此在汇总不同人提交的文档时，可能需要对时间格式进行转换。

现在想写一个函数，传入的参数是时间、原格式、目标格式这三个字符串，返回值是转换好格式的时间。

## 准备
查看Python文档，发现time库中有涉及时间格式的函数time.strftime()和time.strptime()
> time.strftime(format[, t])
Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument. If t is not provided, the current time as returned by localtime() is used. 

>time.strptime(string[, format])
Parse a string representing a time according to a format. The return value is a struct_time as returned by gmtime() or localtime().

这里面的format参数指的是用"%d/%m/%Y"和"%Y-%m-%d"这样的字符串来表示"日/月/年"和"年-月-日"这样的时间格式。更详细的format参数可以在[这里](http://strftime.org)学习。

我对这两个函数的记忆方法是：
> strftime -> `st`ring `f`ormated `time`
> 
> strptime -> `st`ring format-`p`arsed `time`

## 实现
<script src="https://gist.github.com/wp-lai/bf969384e4f7d9ea8948.js"></script>
