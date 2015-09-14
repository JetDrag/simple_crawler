# 关于simple_clawler
simple_clawler是一个基于gevent协程网络框架的异步爬虫，配置适当的并发连接数和时间间隔后，可以轻松占满你的带宽。

-----

## 设计理念
相关技术实现 —— 针对当前版本0.1b。

#### 已实现:
 - 基于gevent实现的全面异步IO，包括异步网页抓取和数据库入库。
 - 使用requests模块访问站点，单例模式确保同一个网站同一个连接池。
 - 模块化，全模块线程安全，日志覆盖。

#### 计划实现:
 1. 基于浏览器内核的动态爬取。
 2. 优化数据存储队列的响应方式。支持更多的存储方法。

-----

## 目前实现的功能
 - 指定某网站爬取指定深度的页面

 - 可以指定 headers 进行爬取

 - 可以指定每次请求间隔时间

 - 可以指定深度或者广度优先

 - 如果没有 keyword, 那就存储所有页面

 - 将结果存储至 mysql

 - 最多爬取多少页面

 - 使用命令行进行配置

-----

## 使用方法
    
	首先，需要到lib/configs_and_contants.py，将MySQL服务器常量修改成你自己的服务器。然后：
	
    example:
    run.py http://www.wooyun.org/ -d 3 -t 0.01 -p 2 -l 10000 -ll 10
    
    usage: run.py [-h] [-hd HEADERS] [-d DEPTH] [-t DELAY_TIME] [-p {1,2}]
              [-l LIMIT] [-k KEYWORD] [-lf LOGFILE] [-ll {0,10,20,30,40,50}]
              [-b {0,1}]
              url

    An Simple Crawler!

    positional arguments:
      url                   Input the url you want to crawler.

    optional arguments:
      -h, --help            show this help message and exit
      -hd HEADERS, --headers HEADERS
                        Specify your header for your crawler.
      -d DEPTH, --depth DEPTH
                        Specify depth for your crawler.
      -t DELAY_TIME, --delay_time DELAY_TIME
                        Specify delay time for your crawler.
      -p {1,2}, --priority {1,2}
                        Specify strategy for your crawler.
      -l LIMIT, --limit LIMIT
                        Specify page limit count of pages.
      -k KEYWORD, --keyword KEYWORD
                        Specify keyword for your crawler.
      -lf LOGFILE, --logfile LOGFILE
                        Specify logfile location.
      -ll {0,10,20,30,40,50}, --loglevel {0,10,20,30,40,50}
                        Specify logger level.
      -b {0,1}, --benchmark {0,1}
                        Disable data store process to benchmark crawler speed.
