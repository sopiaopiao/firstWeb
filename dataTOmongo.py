import pymongo

conn = pymongo.Connection(host='127.0.0.1',port=27017)
db = conn.txdata
f = open('/opt/voyager/apps/myweb/city_level_1_data.log','r')
#f = open('/opt/voyager/tools/1080.log','r')

titleList = ['seq','name','ifdelay','count3','totcount','delaycount','enName']


def dataToMongo():
    for i in f:
        dict = {}
        list = i.strip().split(',')
        for j in range(len(list)):
            dict[titleList[j]] = list[j]
        db.city_level_1.save(dict)


dataToMongo()
