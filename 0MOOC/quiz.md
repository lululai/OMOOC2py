# Quiz

## 背景
在技术类文档编写的过程中，有时会需要问答的形式来巩固知识点的学习。

## 安装
在book.json中添加"plugins": ["quiz"]

## 配置
可以定制"pluginsConfig中的参数，我用的设置如下：
```
"pluginsConfig": {
        "quiz": {
            "labels": {
                "showCorrect"       : "显示正确答案",
                "check"             : "确认",
                "showExplanation"   : "查看解释",
                "explanationHeader" : "Explanation"
            },
            "text": {
                "noChosen"    : "",
                "incomplete"  : ""
            },
            "buttons": {
                "showCorrect"       : true, 
                "showExplanation"   : true
            }
        }
    }
```


## 使用
具体写法类似html语法
```
<quiz>
    <question>
        <p>1 + 1 = ?</p>
        <answer>1024</answer>
        <answer correct>2</answer>
    </question>
</quiz>
```

这个例子实现的效果如下：
<quiz>
    <question>
        <p>1 + 1 = ?</p>
        <answer>1024</answer>
        <answer correct>2</answer>
    </question>
</quiz>

也可以有多选题
```
<quiz name="Gitbook Quiz">
    <question multiple>
        <p>What is gitbook used for?</p>
        <answer correct>To read books</answer>
        <answer>To book hotel named git</answer>
        <answer correct>To write and publish beautiful books</answer>
        <explanation>GitBook.com lets you write, publish and manage your books online as a service.</explanation>
    </question>
</quiz>
```

显示效果如下：
<quiz name="Gitbook Quiz">
    <question multiple>
        <p>What is gitbook used for?</p>
        <answer correct>To read books</answer>
        <answer>To book hotel named git</answer>
        <answer correct>To write and publish beautiful books</answer>
        <explanation>GitBook.com lets you write, publish and manage your books online as a service.</explanation>
    </question>
</quiz>


## 体验
通过添加quiz插件，可以实现单选题和多选题的问答。

