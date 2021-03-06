# 一、互联网是最好的老师

在生活、学习、工作中，互联网是我们身边最好的老师。我们接触互联网的渠道其实就两种，要么是被动，要么是主动。被动是指网站，邮箱，广告，app等媒体的内容推送。主动是指我们有特定的需求去互联网搜索相关的资源。所以，使用搜索引擎的方式会直接影响我们得到的结果。为了得到想要的结果，需要一点搜索技巧。

### 1. 搜索技巧

这里先安利一个[极客导航](http://www.jikedaohang.com/)。

**site：在指定网址中搜索内容 **如：

```
内容 site:zhihu.com
```

**filetype：指定搜索文件类型** 如：

```
内容 filetype:pdf
```

**inurl：在指定url中搜索内容** 如：

```
内容 inurl:csdn
```

[更多用法1](https://www.jianshu.com/p/9a0b33419c0b)，[更多用法2](https://blog.csdn.net/nuoya_1995/article/details/52621323)



### 2. 实用工具推荐

工欲善其事, 必先利其器。善于利用工具的人往往会事半功倍。在企业中，工具的使用可以显著的带来效率的提升。网上的工具不计其数，但适合自己的才是最好的。**对于工具的态度，要不求甚解，只求会用。不够用再学。久而久之，熟能生巧。**

#### 1. 开发工具

**1. Git + Github**

**Git**是[版本控制工具](https://blog.csdn.net/My_name_is_ZwZ/article/details/81605064)最为常用的的一种。不仅公司用，如果是个人开发者，个人设计者的话，首选也是它。

另外一种比较常用的版本控制工具就是SVN，关于两个的[区别](https://www.zhihu.com/question/265284623/answer/295754725)，可以了解一下。

**Github**（*现已被微软收购*）是全球最大代码托管网站，是程序员就先占个坑（注册）再说。我们日常可以把它当成我们的远程个人资料库。所有它可以和编程没有任何关系。写文章，写论文，学习，上课等都可以用它。

[Github相关用法](https://www.zhihu.com/question/20070065), [相关软件大全](https://gitee.com/all-about-git)



而Git和Github结合使用就可以达到类似企业日常工作的体验。当然企业一般是不会用Github的，大部分用Gitlab。因为Github主要还是开源和交友使用。

**2.远程服务器 + IDE（集成开发环境)**

大家的电脑系统有windows的，有mac os的，我们知道这两个系统基本上独立的。很多软件是不兼容的。你需要下载各自系统的软件版本。很不方便。这是一种情况。还有一种情况就是开发时需要安装很多软件，很多库。这个时候你又不想在自己的爱机中安装一堆乱七八糟的东西，怎么办？

为了摆脱上面的困况和不拘泥于系统的局限。我们可以使用远程服务器(Linux)，然后本地使用熟悉的编辑器利用ftp和ssh工具就可以同步开发了。既可以在本地开发，又可以同步到远程服务器上。就算出去旅行，遇到紧急事情，找个网吧就行了。这难道不是一种优雅的编程方式吗。

**3.Markdown编写文档**

markdown是一种类似于html的标记语言，现在的博文采用的就是这种格式，Github默认的文档也是这种格式。相比较于word，它更加轻量，更加小清新。最重要的它是跨平台的。我们都知道word文档只在windows系统有效。markdown文件是以.md结尾的，前面我们提到的用Github写文章就是用markdown。它的编辑器我推荐typora，markdown也可以很快转换成pdf等格式的文件。

#### 2. 线上求助网站

在开发中，我们一定会遇到各种各样的问题。有的问题你能解决，有的问题很坑，会导致你花很长时间也搞不定，这里一般的原则是自己花小于半个小时的时间看能否解决，不能就去问公司的其他人，如果都不知道，那说明可能在你们公司是第一次出现，这个时候就要求助于网上资源了。除了前面我们提到的搜索引擎，还有必要知道站内搜索，这样更加专业，目的性更加强，不会被其他不相干的答案所带偏。

1.[StackOverflow](https://stackoverflow.com/)

IT界百科全书，这是一个外国网站。里面你能遇到的问题基本都有出现，如果没有，也会有有大牛认真回答的，所以不要怀疑这个网站的专业性。当然，你需要英文基础（读写看，先不要求说）。做开发，一点不接触英文是不可能的。毕竟计算机源于美国。

2.[维基百科](https://en.wikipedia.org/wiki/Main_Page)

外国的百度全科，但是维基百科更加全面。

3.[思否](https://segmentfault.com/) 4.[知乎 ](https://www.zhihu.com/)5.[CSDN ](https://www.csdn.net/)6.[简书 ](http://www.jianshu.com/)7.[开源中国](http://www.oschina.net/) 8.博客园

...

#### 3. 线上小工具

有很多开发小工具都已经整理成网页版了，所以没有必要再去下载各种各样的软件。

1.https://tool.lu

2.http://tool.oschina.net

3.http://www.ofmonkey.com

4.https://www.w3schools.com

5.http://www.runoob.com

...

#### 4. Online judge网站

leetcode, linkcode,Kaggle等

#### 5. 相关技术官方网站

基本上成熟的软件或者技术都有自己的官网。



# 二、开发原则

### 1. 避免过早优化

这个问题在《黑客与画家》这本书中反复提到过。

过早优化是一切罪恶的根源”—Donald Knuth。

如果你没有弄清楚未来变化的走向而去优化，实际上让代码变得复杂外，到头来是竹篮打水一场空。

因为优化可能无法很好实现新的需求，对于优化预期的猜测也有可能是错的，所以将耗费大量的时间和精力。

### 2. 整齐的代码缩进和必要注释

虽然每个编程语言都有自己的风格，但是需要遵循它们的代码规范

### 3. 不要重复造轮子

这不是鼓励大家不去创新，相反更是为了在此基础上创新

通常而言，我们如果有稳定以及可靠的库可以用，其实是没有必要去再重新造轮子。

我们重新轮子的时候，能确保代码的稳定性吗?能确保没有BUG吗?

### 4. 每天保持技术更新

最后要说的一定也是老生常谈的，不管你同不同意，你现在会的东西5年后就会过时。

每天保持技术更新，坚信一点，逆水行舟不进则退，对于一个要靠编程吃饭的程序员来说，更是如此!只要每天技术更新才能保证自己不掉队!

不要害怕接触新知识，因为害怕也没用，不管你愿意不愿意。

...



# 三、学习方向

![img](https://dn-simplecloud.shiyanlou.com/uid/c5e305a8e9cb4329eac175649e0f4b33/1515061846849.png-wm)



### 1. 夯实基础

python编程从入门到精通，从单纯的语法理解到灵活应用解决实际问题，掌握Linux和Windows双系统开发环境，掌握常见数据结构和算法（时间复杂度计算，排序，搜索，栈，队列，二叉树），建立面向对象思维，能对问题进行抽象归类，了解设计模式，掌握单例模式和工厂模式

### 2. 网络基础

掌握Linux操作系统进程/线程管理和网络socket编程，熟练编写C/S客户机服务器通信程序，理解python的异步和协程，掌握关系型数据库MySQL和非关系型数据库MongoDB表设计与应用开发，掌握缓存服务器Redis的应用，能独立进行后台服务器的设计和开发

### 3. 爬虫工具

数据采集，掌握爬虫工作原理和反爬虫机制（Selenium，PhantomJS，Tesseract），学习scrapy等框架和scrapy-redis分布式爬虫框架，对各大知名网站数据进行采集，根据业务需求绘制html图表或Excel业务报表

### 4. 网站框架

融会贯通前端和后台所学知识，学习掌握Flask, Django等 web框架，提升开发效率，可进行前后端全栈web开发；学习微信公众号开发，掌握移动web领域开发技能，结合Tornado web框架，加强对http协议、session、跨域请求、安全传输的理解，掌握高并发web服务器开发，掌握Nginx部署和配置

### 5. 人工智能

了解深度学习常见算法，掌握监督学习训练模型的过程，熟悉常用机器深度学习框架的安装和部署，了解图像识别学习和语音识别学习的过程。掌握百度人工智能人脸识别、图像识别、文字识别、语音识别、语音合成、自然语言处理等服务接口的使用，了解百度服务机器人交互场景、定制服务开发。



