# DISQUS 

<!-- ## 背景 -->

## 安装
首先在disqus.com中注册一个账号，登入之后在[此页面](https://disqus.com/admin/create/)注册一个Disqus页面，记住`.disqus.com`之前空白处填写的用户名

然后，在book.json的"plugins": []中加入"disqus"

## 配置
在book.json中加入如下设置
```
"pluginsConfig": {
        "disqus": {
            "shortName": "用户名"
        }
}
```

用户名是之前注册Disqus页面时`.disqus.com`前的用户名

## 使用
进行正确安装和配置之后，在GitBook每个内容页面的最下端就可以看到Disqus评论区。


<!-- ## 体验 -->

