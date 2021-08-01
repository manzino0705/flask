import pymysql
import datetime
from flask import Flask, render_template, request

def search(db_password, infra, to_day):

    conn = pymysql.connect(
       host='127.0.0.1',
       port=3306,
       user='root',
       password=db_password,
       db=infra)   # 인프라 이름을 database 이름으로 지정 , table 이름을 개체 이름으로 지정 

    curs = conn.cursor()

    id = request.args.get('id')
    id = str(id)  # vm1 
    print(id)

    sql = "select * from "+id+ " where DATE like '"+ str(to_day)[:10] +"%'" 
    print(sql)

    data_list = []

    curs.execute(sql)
    row = curs.fetchall()

    for obj in row :
        data_list.append( [obj[0],obj[1],obj[2]] )
        # time, CPU, mem 순서 

    return data_list