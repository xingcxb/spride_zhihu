# -*- coding: utf-8 -*-
import requests
import json
import time
from bs4 import BeautifulSoup

#知乎核心爬虫类
class zhihu():

	def getzhihuhtml(self):
		time_hour = time.strftime("%H",time.localtime())
		if time_hour == "15":#设置定时时间
			title_url = "http://news-at.zhihu.com/api/4/news/latest"
			headers = {'user-agent': 'easymbol-app/0.1'}
			html = requests.get(title_url,headers=headers)

			print("return code = " + str(html.status_code))
			html.encoding = "utf-8"
			json_data = html.json()

			id_title = 0
			xiache = json_data["stories"]
			for list_title in xiache:
				titleName = list_title["title"]
				if "瞎扯" in titleName:
					id_title = list_title["id"]
			if id_title == 0:
				print("没有找到相关文章")
			else:
				word_url = "http://news-at.zhihu.com/api/4/news/" + str(id_title)
				word_html_obj = requests.get(word_url , headers = headers)
				word_html = word_html_obj.json()
			bodyInfo = word_html["body"]
			#print(bodyInfo)
			m = 1
		else:
			print("非定时时间不获取数据")
			m = 0

		if(m == 1):
			soup = BeautifulSoup(bodyInfo,"html.parser")
			list_ask = soup.find_all(class_='content')
			i = 0
			for titleName_htmlTitle in soup.find_all('h2'):
				ask_Name = titleName_htmlTitle.string
				ask = list_ask[i]
				print(ask_Name)
				print(ask)
				i = i + 1

		


#函数主入口
if __name__ == "__main__":
	zhihu1 = zhihu()
	zhihu1.getzhihuhtml()