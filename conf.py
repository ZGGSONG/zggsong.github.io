# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 30
template = {
    "name": "Kepler",
    "type": "git",
    "url": "https://github.com/AlanDecode/Maverick-Theme-Kepler.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": "true",
    "repo": "ZGGSONG/zggsong.github.io@master"
}

# 站点设置
# For site
site_name = "ZGGSONG WIKI"
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
        "name": "BLOG",
        "url": "https://www.zggsong.cn/",
        "brief": "blog."
    },
    {
        "name": "GITHUB",
        "url": "https://www.github.com/ZGGSONG",
        "brief": "github."
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
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="apple-touch-icon" href="https://cdn.jsdelivr.net/gh/zggsong/cdn/apple-icon/Icon-40.png">
<link rel="apple-touch-icon" sizes="72x72" href="https://cdn.jsdelivr.net/gh/zggsong/cdn@master/apple-icon/Icon-72.png">
<link rel="apple-touch-icon" sizes="120x120" href="https://cdn.jsdelivr.net/gh/zggsong/cdn/apple-icon/Icon-60@2x.png">
<link rel="apple-touch-icon" sizes="144x144" href="https://cdn.jsdelivr.net/gh/zggsong/cdn/apple-icon/Icon-72@2x.png">
<link rel="apple-touch-icon" sizes="152x152" href="https://cdn.jsdelivr.net/gh/zggsong/cdn/apple-icon/Icon-76@2x.png">
<link rel="apple-touch-icon" sizes="180x180" href="https://cdn.jsdelivr.net/gh/zggsong/cdn/apple-icon/Icon-60@3x.png">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="icon" type="image/ico" href="//cdn.jsdelivr.net/gh/zggsong/cdn/favicon.ico">
'''

footer_addon = ''
# footer_addon = r'''
# <script>
# var _hmt = _hmt || [];
# (function() {
#   var hm = document.createElement("script");
#   hm.src = "https://hm.baidu.com/hm.js?5f4e80f87318224a9c76e9def1019df5";
#   var s = document.getElementsByTagName("script")[0]; 
#   s.parentNode.insertBefore(hm, s);
# })();
# </script>
# '''

body_addon = ''

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "By9KWYDVoOIP5DmAFLdSkgYJ-gzGzoHsz",
    "appKey": "V5X2XQjTRFxU4RBE9dHcE5iO",
}