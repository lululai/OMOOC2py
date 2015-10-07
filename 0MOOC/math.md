# Mathjax plugin 私人教程

## 背景
在技术文档书写过程中常常会碰到数学公式的编写，GitBook中的Mathjax插件可以展示Tex格式的数学公式

## 安装
在book.json的"plugins": []中加入"mathjax"即可

## 配置

## 使用
写文档时：
1. 可以在`{% math %}`区块中添加Tex公式  
如  
```
When {% math %}a \ne 0{% endmath %}, there are two solutions to {% math %}(ax^2 + bx + c = 0){% endmath %} and they are {% math %}x = {-b \pm \sqrt{b^2-4ac} \over 2a}.{% endmath %}
```
会显示为  

When {% math %}a \ne 0{% endmath %}, there are two solutions to {% math %}(ax^2 + bx + c = 0){% endmath %} and they are {% math %}x = {-b \pm \sqrt{b^2-4ac} \over 2a}.{% endmath %}

2. 用`$$`包围公式代码区块  
如
```
When $$a \ne 0$$, there are two solutions to $$(ax^2 + bx + c = 0)$$ and they are $$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$
```

显示结果为

When $$a \ne 0$$, there are two solutions to $$(ax^2 + bx + c = 0)$$ and they are $$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$

## 体验
将本地repo push到github之后，gitbook可以正确显示公式

但在本地用`gitbook serve`会显示
```
Error: Error loading plugins: mathjax.
```

虽然已经用`gitbook install`安装了mathjax plugin

暂时尚未找到解决办法

