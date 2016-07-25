# -*- coding: UTF-8 -*-

import urllib2,json
import MySQLdb
import spider


def getLocation(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = ''
    uri = url + '?' + 'address=' + address + '&output=' + output + '&ak=' + ak
    temp = urllib2.urlopen(uri)
    temp = json.loads(temp.read())
    if temp['status'] == 0:
        return temp
    return False


def insertLocationToDatabase():
    names = spider.returnHospitalName()

    db = MySQLdb.connect("localhost","root","","putianhospital",charset='utf8' )

    for name in names:
        address_json = getLocation(name)
        if not address_json:
            print(name+"GET LOCATION FAILED")
            continue
        lng = (address_json['result']['location']['lng'])
        lat = (address_json['result']['location']['lat'])
        cursor = db.cursor()

        sql = 'INSERT INTO hospitalLocation VALUES("%s","%s","%s");' %(name,lng,lat)
        try:
            cursor.execute(sql)
        except:
            print(name+"INSERT FAILED")

    db.close()



if __name__ == '__main__':
    insertLocationToDatabase()
