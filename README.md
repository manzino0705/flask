# [EPC monitoring]
EPC 서비스 이상징후 점검을 위한 Cloud 인프라 점검 자동화

## 기본 setting 


python -m venv venv  
source venv/Scripts/activate  
python -m pip install --upgrade pip  
pip install -r requirements.txt  
python run.py  

## 현재 진행 상황 

template 
- index.html ( 날짜 선택 page ) 
- indextest.html ( 선택 기간 내 data 받아온 page -> chart 그려야 함 ) 

run.py  ( flask 실행 파일 )  
cal_day.py ( 기간 내 db 조회)
datepick.py (  )
