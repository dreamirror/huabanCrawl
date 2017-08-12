# -*- coding: utf-8 -*-

import requests
from parsel import Selector
import time

import mongoMgr

from urllib import urlencode

startUrl = "http://huaban.com/search/"

# 在huaban，beauty的分类里面找出的pin ids


def crawl_pin_ids():

    pin_ids = []

    

    flag = True
    page = 2
    while flag:
        try:
            url = startUrl
            headers1 = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                'Accept': 'application/json',
                'X-Request': 'JSON',
                'X-Requested-With': 'XMLHttpRequest',
            }

            # 分类画板的ajax
            # params = {
            #     'j0l4lymf': '',
            #     'max': pin_id,
            #     'limit': '20',
            #     'wfl': '1',
            # }
            params = {
                'q': u'臀',
                'j66728fy': '',
                'page': page,
                'per_page': '20',
                'wfl': '1',
            }

            # ajax request
            print "_"*50
            print "request page [%d]" % page
            z1 = requests.get(url, params=params, headers=headers1)

            if z1.json()['pins']:
                for i in z1.json()['pins']:
                    pin_id = i['pin_id']
                    print pin_id
                    
                    if mongoMgr.get_img(pin_id) == None:
                        pin_ids.append(pin_id)
                        print i['pin_id']
                        mongoMgr.insert(pin_id)
                    # with open("pin_ids.txt",'ab') as f:
                    #     f.write(str(i['pin_id'])+"\n")
                    #     f.close()
                    time.sleep(0.001)
                page = page + 1
                return
            else:
                flag = False
                return set(pin_ids)
        except Exception as e:
            print e
            continue


if __name__ == "__main__":
    print "run urlCrawl"
    crawl_pin_ids()

