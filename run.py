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

@app.route('/detail_vm')
def detail_vm():
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

if __name__ == '__main__' :
    app.run(host='127.0.0.1', port=5050, debug=True) 
