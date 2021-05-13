---
layout: post
title: 用户不在sudoers文件中
slug: sudoers
date: 2020-09-11 22:13:00
status: publish
author: ZGGSONG
categories: 
  - 编程笔记
  - linux
tags: 
  - sudoers
---

## 解决方案

> 将用户添加至`sudoers`中

- 使用`root`连接

```
chmod 640 /etc/sudoers

vi /etc/sudoers

#添加用户名至sudoers中去

:wq

chmod 440 /etc/sudoers
```

![sudoers](./img/sudoers.png)