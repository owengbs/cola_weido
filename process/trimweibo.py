# -*- coding: utf-8-*-
contentlist = []
import re, sys, json
if __name__=='__main__':
    for line in sys.stdin:
        try:
            content = line.replace('\n','').replace('\t','').replace(' ','').replace('\r','')
            if len(content) and content not in contentlist:
                contentlist.append(content)
                print content
        except Exception as e:
            sys.__stderr__.write("%s %s\n" % (line, e))
            continue
