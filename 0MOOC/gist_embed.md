# 在gitbook中添加代码链接
在gitbook中显示代码块很容易，直接用markdown编写就行。  
这里介绍另一中显示代码块的方法————嵌入gist代码链接。

## gist
[GitHubGist](https://gist.github.com)是一个代码片段分享的服务。使用GitHubGist，你可以上传和分享自己的代码，或者搜索、评论或下载别人的代码，另外每个gist都是一个git，也就是说自带版本控制功能。更多的说明详见[官方帮助文档](https://help.github.com/articles/about-gists/)。

本文主要介绍如何在gitbook中嵌入gist代码。

## gitbook中嵌入gist代码
1. 注册gist账号（可以使用GitHub的账号，也可以新建账号）
2. 上传代码片段（也可以在[gist](https://gist.github.com)中直接编辑，下面以我上传的[代码](https://gist.github.com/wp-lai/bf969384e4f7d9ea8948)为例
3. 在右下方找到`Embed URL`(如下图)，
![Gist Embed](https://help.github.com/assets/images/help/gist/gist_embed_link.png)
复制里面的地址
4. 在.md文档中想要嵌入代码块的地方粘贴`Embed URL`即可
5. 最后编译出来的效果如下
![Embed code demo](http://i13.tietuku.com/aa20b29caa7945f0.png)
6. 点击代码区下方的文件名就可以链接到代码在GitHubGist上的网址，可以在这里对代码进行评论。


## 体验 
用markdown展示代码块已经够方便了，为什么还要用嵌入gist代码的方式呢。于我来说，原因有以下几点：
+ 便于储存代码块。将代码存在一个地方比分散在不同文章里更利于管理。
+ 便于评论。Gitbook中添加Disqus插件可以实现评论功能，但不方便单独对文章中的代码进行评论，另外，在disqus评论中要用额外的html tag来实现代码区显示。
+ 便于版本控制。可以查看代码的修改历史，看这个代码是怎么改进的。

