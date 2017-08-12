# -*- coding: utf-8 -*-


import requests
from parsel import Selector
import time
import re
import random
import os
from lxml import etree
from bson.binary import Binary, UUIDLegacy, STANDARD

import mongoMgr
import urlCrawl


_keywords = [u"臀", u"屁股"]


def download(url):
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    n = 1

    # for (key, value) in urls.items():
        
    try:
      
        r = requests.get(url, headers=headers1)
        # if len(r.content)>10000:
      
        return r.content
            # time.sleep(3)
    except Exception as e:
        print(e)
               
    

def findText(pat, txt):
    board_pat = re.compile(
        pat, re.S)
    return re.findall(board_pat, txt)


def scraw_urls(i):
    downloadUrls = {}

    url = 'http://huaban.com/pins/' + str(i) + '/'
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }
        z3 = requests.get(url, headers=headers)
        text = z3.text

        # app["page"] = {"$url":"/pins/151414190/", "pin":{"pin_id":151414190, "user_id":7704433, "board_id":4097124, "file_id":40644692, "file":{"farm":"farm1", "bucket":"hbimg", "key":"3b3652d85fcd35ba3a498ca98387e81364291be9b402-rj2XeL",
        # find above key

        pat = r'app\[\"page\"\].*?\"%s\":\"(.*?)\"'

        # url find
        items = findText(pat % 'key', text)
        # key words find
        keywords = findText(pat % 'raw_text', text)
        # # borad name
        # boradname = findText(pat % 'title', text)
        # # borad desc
        # boradname = findText(pat % 'description', text)

        appPage = findText(r'app\[\"page\"\].*?;', text)

        imgContent = ''
        url = 'http://img.hb.aicdn.com/' + items[0]

        if len(keywords) >= 1 and len(items) >= 1:
            for key in _keywords:
                if key in keywords[0]:
                    # urls.extend(items)
                    downloadUrls[keywords[0]] = items[0]
                    print items
                    
                    imgContent = download(url)

                    print '============================================================================================================'
        # update db
        pin = i
        des = keywords[0]

        # con = mongoMgr.mongodb.imgs.find_one(
        #     {"pin": pin, "urlContent": {'$exists': False}})

        print "update imgs:::" + des
        mongoMgr.mongodb.imgs.update_one(
            {"pin": pin}, {"$set": {"des": des, "url": url, "urlContent": appPage[0], "context":   Binary(imgContent), "md5": 0}})

    except Exception as e:
        print(e)      
    return downloadUrls





if __name__ == "__main__":
    # get url context
    pins = []
    print "start find db all records"
    for imgDoc in mongoMgr.find():
        # print i 
        if not imgDoc.has_key("url"):
            pin =  imgDoc["pin"]
            print pin
            scraw_urls(pin)
    print "end find db all records"
