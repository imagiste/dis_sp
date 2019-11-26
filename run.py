#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,re

def get_html(url):
    page = requests.get(url)
    html = page.text
    soup = BeautifulSoup(html)
    table = soup.select("tbody[id]")
    #table = list(filter(lambda x:x.select(".new a.s.xst")!=[],table))
    result_list = []
        

    for i in table:

        title = i.select(".new a.s.xst")
        if title != []:
            title_name = title[0].get_text()
            title_id = title[0]['href'].split('-')[1]
            auth = i.select("cite a")[0]['href'].split('=')[-1]
            result_list.append("%s,%s,%s"%(title_name,title_id,auth))
   
    return result_list 


def get_nxt(url):
    page = requests.get(url)
    html = page.text
    soup = BeautifulSoup(html)
    nxt = soup.select(".nxt")[0]['href']
    return "https://www.discuz.net/%s"%nxt

def write_file(li):
    for i in li:
        with open('a.txt', 'a+') as f:
            f.write(str(i))
            f.write('\n')


if __name__ == '__main__':
    url = "https://www.discuz.net/forum-10-1.html"

    write_file(get_html(url))
    while get_nxt(url):
        url = get_nxt(url)
        print(url)
        write_file(get_html(url))
        
