---
layout: post
title: Github-DNS污染
slug: dnscachepollution
date: 2021-01-19 17:26:00
status: publish
author: ZGGSONG
categories: 
  - 日常技巧
tags: 
  - DNS
  - Github
---

## 前言

一直发现有这个问题，后来才发现是DNS污染问题，ABROAD也是没用。暂时只能修改`hosts`了

## 解决

- 打开[ipaddress.com](https://www.ipaddress.com)查询`raw.githubusercontent.com`真实ip

![ipaddress](https://cdn.zggsong.cn/2020/04/23/6ea1202e0c596.png)

> linux && mac
```shell
sudo vim /etc/hosts
#最后一行添加
199.232.68.133    raw.githubusercontent.com
```

- 刷新DNS缓存

```shell
sudo dscacheutil -flushcache    #mac刷新DNS
sudo service networking restart     #linux刷新DNS
ipconfig /flushdns     #windows刷新DNS
```