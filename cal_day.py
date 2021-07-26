# start day, end day 입력 받아서 sql 문 반환 
# sql = select * from flask where date like '2021-07-23%' order by date 
# 시작일 : start,  끝나는 날 : end 

import datetime
import re

def calday( start, end ):

    sqls=[]

    s_day = datetime.datetime.strptime(re.sub("\-","",start), "%Y%m%d")
    e_day = datetime.datetime.strptime(re.sub("\-","",end), "%Y%m%d")

    diff = str(e_day - s_day) 
    # diff = 2 days, 0:00:00 

    for i in range( int(diff[0])+1 ):
        n_day =  s_day + datetime.timedelta(days=i)

        sqls.append( "select * from flask where date like '"+ str(n_day)[:10] +"%'"  )
    
    return sqls


# calday('2021-07-30', '2021-08-01')