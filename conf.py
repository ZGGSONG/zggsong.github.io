# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/wiki/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Kepler",
    "type": "git",
    "url": "https://github.com/AlanDecode/Maverick-Theme-Kepler.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": "true",
    "repo": "ZGGSONG/wiki@gh-pages"
}

# 站点设置
# For site
site_name = "艾芝士"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020-07-14T00:00+08:00"
author = "ZGGSONG"
email = "zggsong@foxmail.com"
author_homepage = "https://www.zggsong.cn"
description = "简单的记录学习."
key_words = ["Maverick", "ZGGSONG", "Kepler", "wiki"]
language = 'zh-CN'
external_links = [
    {
        "name": "blog",
        "url": "https://www.zggsong.cn/",
        "brief": "my blog."
    },
    {
        "name": "music",
        "url": "https://www.zggsong.cn/zgg/program/music",
        "brief": "music."
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]



head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="icon" type="image/ico" href="//cdn.jsdelivr.net/gh/zggsong/cdn/favicon.ico">
'''

footer_addon = ''

body_addon = ''
