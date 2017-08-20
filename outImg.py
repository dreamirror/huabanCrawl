# -*- coding: utf-8 -*-
import os
import requests
import mongoMgr


# file_path = r'E:\huaban'
file_path = r'./'
n = 1

def writeImg(name,content):
    try:
        global n 
        global file_path
        print file_path
        if not os.path.exists(os.path.join(file_path, "huaban")):
            os.makedirs(os.path.join(file_path, "huaban"))
        os.chdir(file_path + '\\' + "huaban")
        
        with open(name + ".jpg", 'wb') as f:
            f.write(content)
            f.flush()
            f.close()
            print u"第" + str(n) + u"张图片下载成功" + "size:" + str(len(content) / 1000)
            n += 1
    except Exception as e:
        print(e)

if __name__ == "__main__":
    try:
    # get url context
        pins = []
        print "start find db all records"
        for imgDoc in mongoMgr.findstr({"$where":"Object.bsonsize({context:this.context})>21"}):
            # print i 
            if  imgDoc.has_key("url"):
                pin =  imgDoc["pin"]
                print imgDoc["des"]
               

                context = imgDoc["context"]
                #print type(context)
                #print context
                writeImg(imgDoc["pin"],imgDoc["context"])
            
        print "end find db all records"
    except Exception as e:
        print(e)