# -*- coding: utf-8 -*-
from pymongo import MongoClient
import re,urllib,collections
import chardet
pattern = re.compile(r'^http://zh.wikipedia.org/wiki/(.*)')
client = MongoClient('localhost', 27017)
db = client.wiki
collection = db.wiki_document
category_dict = {}
category_sorted_dict = {}
category_list = []
doc_list = []
url_list = []
title_list = []
used_cate_list = []
for docdict in collection.find():
    if 'title' in docdict and 'url' in docdict and 'content' in docdict and 'category' in docdict:
        title = docdict['title']
        url = docdict['url']
        content = docdict['content']
        content_str = content.encode("utf8")
        try:
            content_str = unicode(content_str, 'utf8').encode('gbk')
        except:
            continue
        if len(content_str) > 0:
            print content_str.replace("\n","")
        category = docdict['category']
        utfcategory = category.encode('utf8')
        match = pattern.match(url)
        if match:
            catelist = utfcategory.split('-')
            for cate in catelist:
                if cate not in category_dict:
                    category_dict[cate] = 0
                category_dict[cate] += 1
            urlstr = str(match.group(1))
            category_list.append(utfcategory)
            doc_list.append(content)
            url_list.append(url)
            title_list.append(title)
#             print urllib.unquote(urlstr)
for i in range(len(category_list)):
    catelist = category_list[i].split('-')
    catedict = {}
    for cate in catelist:
        catedict[cate] = category_dict[cate]
    cate_sorted_dict = collections.OrderedDict(sorted(catedict.items(),key = lambda t:t[1]))
    cate_sorted_list = reversed(cate_sorted_dict)
    for sct in cate_sorted_list:
#         print "category:"+sct+"\t"+title_list[i]
        break
print len(used_cate_list)
print len(doc_list)
