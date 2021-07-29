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

# 오늘 날짜 계산하기! 
to_day = datetime.datetime.today()  
today_sql = "select * from flask where date like '"+ str(to_day)[:10] +"%'"
today_data_list = []
curs.execute(today_sql)
row = curs.fetchall()
for obj in row :
    today_data_list.append( [obj[0],obj[1],obj[2]] )

@app.route('/')
def index():
    global to_day, today_data_list
    return render_template('index.html',data_list=today_data_list , today=str(to_day))


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


# storage page 
@app.route('/storage_start')
def storagestart():
    global to_day, today_data_list
    return render_template('storage_start.html',data_list=today_data_list , today=str(to_day))


@app.route('/storage_lookup', methods=['GET'])
def storagelookup():
    data_list, start, end = datepick(db_password)
    return render_template('storage_lookup.html', data_list=data_list , start=start, end=end )


# NW page 
@app.route('/nw_start')
def nwstart():
    global to_day, today_data_list
    return render_template('nw_start.html',data_list=today_data_list , today=str(to_day))


@app.route('/nw_lookup', methods=['GET'])
def nwlookup():
    data_list, start, end = datepick(db_password)
    return render_template('nw_lookup.html', data_list=data_list , start=start, end=end )


# LB page 
@app.route('/lb_start')
def lbstart():
    global to_day, today_data_list
    return render_template('lb_start.html',data_list=today_data_list , today=str(to_day))


@app.route('/lb_lookup', methods=['GET'])
def lblookup():
    data_list, start, end = datepick(db_password)
    return render_template('lb_lookup.html', data_list=data_list , start=start, end=end )




if __name__ == '__main__' :
    app.run(host='127.0.0.1', port=5050, debug=True) 
