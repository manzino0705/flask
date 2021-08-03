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

    sql = "select * from "+infra+ " where DATE like '"+ str(to_day)[:10] +"%'" +' and NAME="'+id+'" order by DATE'
    sql2 = 'select exists ( select * from VMCARE where name = "'+id+'")'
    curs.execute(sql)
    row = curs.fetchall()

    curs.execute(sql2)
    recycle = curs.fetchall()

    return row , recycle


def search(db_password, zone, infra, to_day):

    row, recycle= db_connect(db_password, zone, infra, to_day )
    data_list = []

    for obj in row :
        data_list.append( [str(obj[0]),obj[2],obj[3]] )
        # DATE, CPU, MEM 순서  
        # DATE, input bound, output bound 순서 

    return data_list, recycle 


def storage_search(db_password, zone, infra, to_day):

    row, recycle= db_connect(db_password, zone, infra, to_day )
    data_list = []

    for obj in row :
        data_list.append( [str(obj[0]),obj[2],obj[3],obj[4]] )
        print(obj)
        # DATE | IOPS  | LATENCY  |   MBPS

    return data_list, recycle 
