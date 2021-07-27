import pymysql
import datetime
from flask import Flask, render_template, request
from cal_day import calday 
from datepick import datepick
# local DB랑 연결, db 설정 정보 넣기 
# db name : test , table name : flask 

db_password='akswl'
conn = pymysql.connect(
       host='127.0.0.1',
       port=3306,
       user='root',
       password=db_password,
       db='test')

curs = conn.cursor()

# Flask App 생성
app = Flask(__name__)

@app.route('/')
def index():
    to_day = datetime.datetime.today()      # index 9 까지 2021-07-26 
    sql = "select * from flask where date like '"+ str(to_day)[:10] +"%'"

    data_list = []
    curs.execute(sql)
    row = curs.fetchall()

    for obj in row :
        data_list.append( [obj[0],obj[1],obj[2]] )
            # 날짜, CPU, disk 순서 

    return render_template('index.html',data_list=data_list , today=str(to_day))


@app.route('/indextest', methods=['GET'])
def indextest():
    data_list, start, end = datepick(db_password)
    return render_template('indextest.html', data_list=data_list , start=start, end=end )


# 오늘 날짜 계산하기! 
to_day = datetime.datetime.today()  
today_sql = "select * from flask where date like '"+ str(to_day)[:10] +"%'"
today_data_list = []
curs.execute(today_sql)
row = curs.fetchall()
for obj in row :
    today_data_list.append( [obj[0],obj[1],obj[2]] )


# vm page 
@app.route('/vm_start')
def vmstart():
    global to_day, today_data_list
    return render_template('vm_start.html',data_list=today_data_list , today=str(to_day))


@app.route('/vm_lookup', methods=['GET'])
def vmlookup():
    data_list, start, end = datepick(db_password)
    return render_template('vm_lookup.html', data_list=data_list , start=start, end=end )

# vr page
@app.route('/vr_start')
def vrstart():
    global to_day, today_data_list
    return render_template('vr_start.html',data_list=today_data_list , today=str(to_day))


@app.route('/vr_lookup', methods=['GET'])
def vrlookup():
    data_list, start, end = datepick(db_password)
    return render_template('vr_lookup.html', data_list=data_list , start=start, end=end )

# Cnode page 
@app.route('/cnode_start')
def cnodestart():
    global to_day, today_data_list
    return render_template('cnode_start.html',data_list=today_data_list , today=str(to_day))


@app.route('/cnode_lookup', methods=['GET'])
def cnodelookup():
    data_list, start, end = datepick(db_password)
    return render_template('cnode_lookup.html', data_list=data_list , start=start, end=end )


if __name__ == '__main__' :
    app.run(host='127.0.0.1', port=5050, debug=True) 
