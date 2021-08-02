import pymysql
import datetime
from flask import Flask, render_template, request

def db_connect(db_password, zone, infra, to_day):
    conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password=db_password,
    db=zone) 

    curs = conn.cursor()
    id = request.args.get('id')
    id = str(id)  # vm1 

    sql = "select * from "+infra+ " where DATE like '"+ str(to_day)[:10] +"%'" +" and NAME='"+id+"' order by DATE"

    curs.execute(sql)
    row = curs.fetchall()
    return row 


def search(db_password, zone, infra, to_day):

    row = db_connect(db_password, zone, infra, to_day )
    data_list = []

    for obj in row :
        data_list.append( [str(obj[0]),obj[2],obj[3]] )
        # DATE, CPU, MEM 순서  
        # DATE | IOPS  | LATENCY 
        # DATE, input bound, output bound 순서 

    return data_list

