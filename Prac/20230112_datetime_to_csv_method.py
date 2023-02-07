import FinanceDataReader as fdr
import pandas as pds
import datetime as date

#시간을 나타내는 클래스는 datetime클래스를 사용하면 됨
today = date.datetime.now()
#strftime매써드를통하여 날짜를 String형식으로 바꿈
date = today.strftime("%F")
df_krx = fdr.StockListing('KRX')

print(today)
print(date)
print(df_krx)

#dataframe객체에 담긴 내용은 to_csv를 통하여 엑셀파일로 만들어서 저장할 수 있다.
df_krx.to_csv(path_or_buf="C://Users/sanghee/Desktop/develop/finance/QuantBeginner/data/"+date+".csv"
              ,index = False,encoding="utf-8-sig")
#글자가 깨질 시에 encoding형식을 utf-8-sig으로 바꿔주면 스무스