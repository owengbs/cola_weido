# -*- coding: utf-8 -*-
from pymongo import MongoClient
import re,urllib,collections
import chardet
client = MongoClient('localhost', 27017)
patternstr = ".*可穿戴设备.*".decode('utf8')
pattern = re.compile(r''+patternstr)
db = client.sina
collection_micro_blog = db.micro_blog
collection_weibo_user = db.weibo_user
for docdict in collection_micro_blog.find():
    content = docdict['content']
    uid = docdict['uid']
    match = pattern.match(content)
    if match:
        userinfo = collection_weibo_user.find({'uid':uid})
        print userinfo['info']
        print uid+"\t"+content
    else:
        pass
