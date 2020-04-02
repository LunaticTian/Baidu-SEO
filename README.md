# Baidu SEO 
## 百度SEO主动推送工具

由于某种原因，我们在为网站或博客做SEO优化提交并且记录sitemap.xml时，百度官方的站长平台会无法识别或读取，这导致我们的SEO失败。


因此使用主动推送方式解决此问题。

## 原理
官方提供了主动推送的接口，通过站长平台得知自己的接口调用地址：http://data.zz.baidu.com/urls?site=www.lunatic.wang&token=xxxxx

使用ET解析由hexo解析出来的sitemap.xml，读取网站地址，再使用接口推送自己解析出来的地址。

## 使用方法
### 方法一
解析sitemap地址直接推送。
### 方法二 
解析sitemap，然后将数据传送到写好脚本的服务器服务器再推送。

此方法好处在于，在开机或者编译后都能进行推送，并且由于推送并不在本机，所以不影响本机操作循环推送，充分利用服务器以及官方给的50000的推送条数。


----------


## 依赖

- python 3+
- flask
- requests

## 使用方法
将push.py存放在sitemap文件夹中，将getURL存放在服务器中

### push.py

解析sitemap，将生成的链接通过json发送到getURL中。


### getURL.py
修改url为自己的接口地址。

Restful服务器接受json链接，循环推送地址.



## 其他版本

若未有服务器，可自行修改push.py文件，将getURL.py中的baidu()方法移至push.py中，修改push中json为str。


