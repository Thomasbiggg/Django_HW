import requests as res
import json
import sqlite3

r = res.get('https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-001?'
            'Authorization=CWB-90717712-72BE-4C09-9478-ADCD9D3B031B&format=JSON&'
            'elementName=Wx')

data = json.loads(r.text)

conn = sqlite3.connect('weather.db')

cursor = conn.cursor()



SQL = ('CREATE TABLE  IF NOT EXISTS "test_Location_1" ('
       '"no" INTEGER PRIMARY KEY AUTOINCREMENT,'
       '"locationName" TEXT,'
       '"startTime" TEXT,'
       '"endTime"  TEXT,'
       '"parameterName" TEXT,'
       '"parameterValue" TEXT,'
       'UNIQUE(locationName, startTime, endTime))')

cursor.execute(SQL)

data_list = data['records']['locations'][0]['location']
for x in data_list:
        for y in x['weatherElement'][0]['time']:
                cursor.execute('INSERT OR REPLACE INTO test_Location_1(locationName, startTime, endTime, parameterName, parameterValue)\
                                        VALUES (?,?,?,?,?)', (\
                                        x['locationName'],\
                                        y['startTime'],\
                                        y['endTime'],\
                                        y['elementValue'][0]['value'],\
                                        y['elementValue'][1]['value']))
                

conn.commit()





'''
TEST
time_list = data['records']['locations'][0]['location'][0]['weatherElement'][0]['time']

        for x in time_list:
                 print('{}:{}startTime: {}endTime: {}parameterName: {}parameterValue: {}'\
                          .format(location['locationName'], '\n', x['startTime']+'\n', x['endTime']+'\n', x['elementValue'][0]['value']+'\n', x['elementValue'][1]['value']+'\n'))



location_list = data['records']['locations'][0]['location']
time_list = data['records']['locations'][0]['location'][0]['weatherElement'][0]['time']
i = 1
for location in location_list:
        print(i)
        for x in time_list:
                cursor.execute('INSERT OR IGNORE INTO Location(locationName, startTime, endTime, parameterName, parameterValue)\
                                        VALUES (?,?,?,?,?)', (\
                                        location['locationName'],\
                                        x['startTime'],\
                                        x['endTime'],\
                                        x['elementValue'][0]['value'],\
                                        x['elementValue'][1]['value']))
        i+=1




SQL = 'CREATE TABLE  IF NOT EXISTS"Location"(\
                "no" INTEGER PRIMARY KEY AUTOINCREMENT, \
                "startTime" TEXT,\
                "endTime" TEXT,\
                "parameterName" TEXT,\
                "parameterValue" TEXT)'


for x in data_list:
        for y in x['weatherElement'][0]['time']:
                print('{}:{}startTime: {}endTime: {}parameterName: {}parameterValue: {}'\
                          .format(x['locationName'], '\n', y['startTime']+'\n', y['endTime']+'\n', y['elementValue'][0]['value']+'\n', y['elementValue'][1]['value']+'\n'))


'''
