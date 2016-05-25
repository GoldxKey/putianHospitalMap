# -*- coding: UTF-8 -*-
import urllib2

def downTheHTML(url):
    req_header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept':'text/html;q=0.9,*/*;q=0.8',
    'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Connection':'close'
    }
    req_timeout = 5
    req = urllib2.Request(url,None,req_header)
    resp = urllib2.urlopen(req,None,req_timeout)
    html = resp.read()
    return html

def returnHospitalName():
    url = u"http://news.ifeng.com/mainland/special/ptxyy/"
    html = downTheHTML(url)
    html = html[html.find("var hospitals = [")+len("var hospitals = [")+1:]
    html = html[:html.find("];")-1]

    eachLine = html.split('\n')
    hospitalNames = []
    for line in eachLine:
        hospital = line.split("<br/>")
        hospital[0]=hospital[0][hospital[0].find(',')+2:]
        hospital[-1]=hospital[-1][:hospital[-1].find(',')-1]
        for hosp in hospital:
            hospitalNames.append(hosp)
    return hospitalNames
