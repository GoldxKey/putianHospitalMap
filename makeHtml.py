#coding:utf-8
import MySQLdb


def returnLocationList():
    db = MySQLdb.connect("localhost","root","","putianhospital",charset='utf8' )
    cursor = db.cursor()
    cursor.execute("SELECT lat,lng FROM hospitallocation;")
    data = cursor.fetchall()
    db.close()
    return data

def makeHtml():
    file = open("html/test.html",'r')
    html = file.read()
    file.close()
    header = html[:html.find("//PYTHONBRIDGEBEGIN")+len("//PYTHONBRIDGEBEGIN")]
    footer = html[html.find("//PYTHONBRIDGEEND"):]

    data = returnLocationList()
    count = 0
    script = "\n"
    for lat,lng in data:
        count += 1
        script +=" var marker%s = new L.Marker(new L.latLng(%s, %s)); map.addLayer(marker%s);\n" %(count,lat,lng,count)

    file = open("html/test.html",'w')
    file.write(header+script+footer)
    file.close()




