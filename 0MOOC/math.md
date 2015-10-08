# Ketax

## 背景
在技术文档书写过程中常常会碰到数学公式的编写，GitBook中的Ketax插件可以展示Tex格式的数学公式

## 安装
在book.json的"plugins": []中加入"ketax"即可

<!-- ## 配置 -->

## 使用
使用\$\$将公式代码包围，或用`{% math %}`和`{% endmath %}`将公式代码包围

## 体验
显示效果如下：

Inline math: $$\int_{-\infty}^\infty g(x) dx$$

Block math:
$$
\int_{-\infty}^\infty g(x) dx
$$


ps. 注意不要将\$\$写入MarkDown文件的代码区域里，否则的话编译时会出现` Unexpected character`的错误。

