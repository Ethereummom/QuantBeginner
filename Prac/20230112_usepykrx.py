import pykrx as pkrx
from pykrx import stock
import pandas as pds
import datetime as date
import time

#시간을 나타내는 클래스는 datetime클래스를 사용하면 됨
today = date.datetime.now()
#strftime매써드를통하여 날짜를 String형식으로 바꿈
date = today.strftime("%F")
adjusteddate = today.strftime("%Y%m%d")
#매개변수를 변수화시키기 위하여 %y%m%d형태로 만들어주고
print(adjusteddate)


#데이터프레임을 변수에 담아주기
todays_KOSPI_data = stock.get_market_ohlcv(adjusteddate,market = "KOSPI")
todays_KOSDAQ_data = stock.get_market_ohlcv(adjusteddate, market = "KOSDAQ")
todays_KONEX_data = stock.get_market_ohlcv(adjusteddate, market="KONEX")


#데이터를엑셀화하여 정리
todays_KOSPI_data.to_csv(path_or_buf="C://Users/sanghee/Desktop/develop/finance/QuantBeginner/data/"+date+"KOSPI.csv"
              ,index = False,encoding="utf-8-sig")
todays_KOSDAQ_data.to_csv(path_or_buf="C://Users/sanghee/Desktop/develop/finance/QuantBeginner/data/"+date+"KOSDAQ.csv"
              ,index = False,encoding="utf-8-sig")
todays_KONEX_data.to_csv(path_or_buf="C://Users/sanghee/Desktop/develop/finance/QuantBeginner/data/"+date+"KONEX.csv"
              ,index = False,encoding="utf-8-sig")