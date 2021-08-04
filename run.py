import pymysql
import datetime
from flask import Flask, render_template, request
from cal import calday , caltotal, calutil
from datepick import datepick, storage_datepick
from search import search,storage_search

# local DB랑 연결, db 설정 정보 넣기 
# db name : test , table name : flask 

db_password='gml040708'
zone = 'm2'
conn = pymysql.connect(
       host='127.0.0.1',
       port=3306,
       user='root',
       password=db_password,
       db=zone)

curs = conn.cursor()

# Flask App 생성
app = Flask(__name__)

# 오늘 날짜 계산하기! 
to_day = datetime.datetime.today()  

# index
@app.route('/')
def index():
    global to_day
    total = caltotal(db_password,zone,to_day)
    # utils = calutil(db_password, zone, to_day)
    utils = [2,4,1,6,4,2]
    return render_template('index.html', total=total , today=str(to_day), zone=zone, utils=utils)


# 내가 조회할 장치 id 
id = str()
recycle = 0 

# vm page 
@app.route('/vm_start', methods=['GET'])
def vmstart():
    global to_day,id
    global recycle
    today_data_list, recycle= search( db_password, zone, 'VM', to_day)
    id = request.args.get('id')
    return render_template('vm_start.html',data_list=today_data_list , today=str(to_day), id=id, recycle=recycle)


@app.route('/vm_lookup', methods=['GET'])
def vmlookup():
    data_list, start, end = datepick(db_password, zone, 'VM', id)
    print(data_list)
    return render_template('vm_lookup.html', data_list=data_list , start=start, end=end , id=id, recycle=recycle)

# vr page
@app.route('/vr_start')
def vrstart():
    global to_day,id
    today_data_list= search( db_password, zone,'VR', to_day)
    id = request.args.get('id')
    return render_template('vr_start.html',data_list=today_data_list , today=str(to_day), id=id)


@app.route('/vr_lookup', methods=['GET'])
def vrlookup():
    data_list, start, end = datepick(db_password,zone,'VR',id)
    return render_template('vr_lookup.html', data_list=data_list , start=start, end=end ,id=id)

# Cnode page 
@app.route('/cnode_start')
def cnodestart():
    global to_day,id
    today_data_list= search( db_password, zone, 'CNODE', to_day)
    id = request.args.get('id')
    ccpu=0
    cmem=0
    for i in today_data_list[0]:
        if i[1]>=90:
            ccpu +=1
        if i[2]>=80:
            cmem +=1
    return render_template('cnode_start.html',data_list=today_data_list , today=str(to_day),id=id, ccpu=ccpu, cmem=cmem)


@app.route('/cnode_lookup', methods=['GET'])
def cnodelookup():
    data_list, start, end = datepick(db_password,zone, 'CNODE',id)
    ccpu=0
    cmem=0
    for i in data_list[0]:
        if i[1]>=90:
            ccpu +=1
        if i[2]>=80:
            cmem +=1
    return render_template('cnode_lookup.html', data_list=data_list , start=start, end=end,id=id, ccpu=ccpu, cmem=cmem)


# storage page 
@app.route('/storage_start')
def storagestart():
    global to_day,id
    today_data_list= storage_search( db_password, zone,'STORAGE', to_day)
    id = request.args.get('id')
    return render_template('storage_start.html',data_list=today_data_list , today=str(to_day),id=id)


@app.route('/storage_lookup', methods=['GET'])
def storagelookup():
    data_list, start, end = storage_datepick(db_password,zone, 'STORAGE',id)
    return render_template('storage_lookup.html', data_list=data_list , start=start, end=end ,id=id)


# NW page 
@app.route('/nw_start')
def nwstart():
    global to_day,id
    today_data_list= search( db_password, zone,'CISCO', to_day)
    id = request.args.get('id')
    return render_template('nw_start.html',data_list=today_data_list , today=str(to_day),id=id)


@app.route('/nw_lookup', methods=['GET'])
def nwlookup():
    data_list, start, end = datepick(db_password,zone,'CISCO',id)
    return render_template('nw_lookup.html', data_list=data_list , start=start, end=end ,id=id)


# LB page 
@app.route('/lb_start')
def lbstart():
    global to_day,id
    today_data_list= search( db_password, zone,'LB', to_day)
    id = request.args.get('id')
    return render_template('lb_start.html',data_list=today_data_list , today=str(to_day),id=id)


@app.route('/lb_lookup', methods=['GET'])
def lblookup():
    data_list, start, end = datepick(db_password, zone, 'LB',id)
    return render_template('lb_lookup.html', data_list=data_list , start=start, end=end ,id=id)



if __name__ == '__main__' :
    app.run(host='127.0.0.1', port=80, debug=True) 
