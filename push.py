# -*- coding: UTF-8 -*-
import requests,json
import xml.etree.ElementTree as ET


listurl = []
tree = ET.ElementTree(file='sitemap.xml')
root = tree.getroot()
for i in root:
	for x in i:
		listurl.append(x.text)
		break


strs = ""
for lists in listurl:


	strs = strs + lists + '\n'

ret = {"url":strs}
s = json.dumps(ret)
print(s)
headers = {'Content-Type': 'application/json'}
try:
	requests.post("http://47.100.21.174:9090/getsitemap", data=s,headers=headers,timeout=2)
except Exception :
	print("出现异常-->")
