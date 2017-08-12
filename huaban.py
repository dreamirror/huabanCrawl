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
import analysisUrl
import outImg


context = analysisUrl.download(r'http://img.hb.aicdn.com/583dec9646d4c9e188320c5df15f8753a0de66c64afc-1FkbDV')
outImg.writeImg('x',context)


