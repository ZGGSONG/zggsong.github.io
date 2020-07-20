---
layout: post
title: Sql Developer连接Oracle数据库
slug: sql_developer
date: 2020-07-17 01:02:00
status: publish
author: ZGGSONG
categories: 
  - 编程笔记
  - 环境配置
tags: 
  - sql developer
  - oracle数据库
---

## <span id="jump">安装数据库</span>

> 安装`oracle`数据库所有的文件都在[这里](https://www.oracle.com/cn/downloads/)

![](./img/oracle.png)

## 连接数据库

- 使用`cmd` 输入 `sqlplus`进行连接数据库

- 打开软件根目录`/product/11.2/db_home1/sqldeveloper/sqldeveloper.exe`

然而这将无法使用，因为不论是自带的jdk还是一般自己配制的jdk都是64位，但是官方在制作时这里面自带的`sqlDeveloper`是不支持64位jdk的，所以需要更换成新版本的，[点这里](#jump)

## 遇到的问题

__然而，在使用64位jdk之后，可能`C:\\Program Files\\java\\jdk***\\jre\\bin\\`里面并没有`msvcr100.dll`，就只需要将`sqlDeveloper/jdk/jre/bin/`里面的`msvcr100.dll`copy一份过去，也可以直接使用带jdk的`sqlDeveloper`里面的jdk也是可以的__

## 参考

- [安装Oracle11g后无法使用其自带的SQLdeveloper](https://blog.csdn.net/qq_32528231/article/details/52914329?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522159524101219195188406377%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=159524101219195188406377&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v3~pc_rank_v2-1-52914329.first_rank_ecpm_v3_pc_rank_v2&utm_term=%E5%AE%89%E8%A3%85oracle11g%E5%90%8E%E6%97%A0%E6%B3%95%E4%BD%BF%E7%94%A8%E5%85%B6%E8%87%AA%E5%B8%A6)