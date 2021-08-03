# start day, end day 입력 받아서 sql 문 반환 
# sql = select * from flask where date like '2021-07-23%' order by date 
# 시작일 : start,  끝나는 날 : end 

import re, pymysql, datetime 
from flask import Flask, render_template, request

def calday( start, end, infra, id ):

    sqls=[]

    s_day = datetime.datetime.strptime(re.sub("\-","",start), "%Y%m%d")
    e_day = datetime.datetime.strptime(re.sub("\-","",end), "%Y%m%d")

    diff = str(e_day - s_day) 
    # diff = 2 days, 00:00:00 

    for i in range( int(diff[0])+1 ):
        n_day =  s_day + datetime.timedelta(days=i)
        sqls.append( "select * from "+infra+" where DATE like '"+ str(n_day)[:10] +"%'"+' and NAME="'+id+'" order by DATE'  )
    return sqls

# calday('2021-07-30', '2021-08-01')

def caltotal(db_password, zone, to_day):

    conn = pymysql.connect(
       host='127.0.0.1',
       port=3306,
       user='root',
       password=db_password,
       db=zone)   # 해당 zone의 total 양 조회 

    curs = conn.cursor()
    total_count=[]

    infra = ['VM', 'VR', 'CNODE','STORAGE','CISCO','CITRIX']  
    for i_name in infra:
        sql = "select count(distinct NAME) from "+i_name+ " where DATE like '"+ str(to_day)[:10] +"%'" 
        curs.execute(sql)
        row = curs.fetchall()
        total_count.append(row[0])

    return total_count

# print(caltotal('akswl','m2', '2021-08-02 00:00:00'))