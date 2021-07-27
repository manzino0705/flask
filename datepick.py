import pymysql
import datetime
from flask import Flask, render_template, request
from cal_day import calday

def datepick(db_password):

    conn = pymysql.connect(
       host='127.0.0.1',
       port=3306,
       user='root',
       password=db_password,
       db='test')

    curs = conn.cursor()

    m_day = request.args.get('m_day')
    m_day = str(m_day)

    day = m_day.split(' ')
    start = day[0]
    end = day[2]

    sqls = calday( start, end )

    data_list = []
    for sql in sqls: 
        print(sql)
        curs.execute(sql)
        row = curs.fetchall()

        for obj in row :
            data_list.append( [obj[0],obj[1],obj[2]] )
            # 날짜, CPU, disk 순서 

    return data_list, start, end