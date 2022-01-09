## 참고 yfinance## 
# https://junyoru.tistory.com/129

## 참고(공식 블로그) yfinance ##
# https://aroussi.com/post/python-yahoo-finance

## 참고(제무제표) yahoofinancials##
# https://pypi.org/project/yahoofinancials/

## ta-lib ##
## 주가의 기술적 분석을 위한 ta-lib ##
## ta-lib 설치시 참고자료 ##
# https://seong6496.tistory.com/149
# https://minjejeon.github.io/learningstock/2018/04/07/installing-and-using-talib.html
# https://mrjbq7.github.io/ta-lib/doc_index.html

## MACE Ocillator ##
# https://nakyup.tistory.com/5


## start ##
import yfinance as yf
import talib
import pandas as pd
## 일봉 데이터 생성
data = yf.download(["VZ"], interval="1d")
data.dropna(inplace=True) # nan있는 행 제거
data["RSI"] = talib.RSI(data["Close"], 14) # Tradingview와 일치

macd_short, macd_long, macd_signal=12,26,9 #기본값 
data["MACD_short"]=data["Close"].ewm(span=macd_short).mean() 
data["MACD_long"]=data["Close"].ewm(span=macd_long).mean() 
data["MACD"]=data.apply(lambda x: (x["MACD_short"]-x["MACD_long"]), axis=1) 
data["MACD_signal"]=data["MACD"].ewm(span=macd_signal).mean() 
data["MACD_oscillator"]=data.apply(lambda x:(x["MACD"]-x["MACD_signal"]), axis=1) 
# data["MACD_sign"]=data.apply(lambda x: ("매수" if x["MACD"]>x["MACD_signal"] else "매도"), axis=1)

data.to_csv("../stock_data/stock_day.csv", sep=",")

## 주봉 데이터 생성
data = yf.download(["VZ"], interval="1wk")
data.dropna(inplace=True) # nan있는 행 제거
data["RSI"] = talib.RSI(data["Close"], 14) # Tradingview와 일치

macd_short, macd_long, macd_signal=12,26,9 #기본값 
data["MACD_short"]=data["Close"].ewm(span=macd_short).mean() 
data["MACD_long"]=data["Close"].ewm(span=macd_long).mean() 
data["MACD"]=data.apply(lambda x: (x["MACD_short"]-x["MACD_long"]), axis=1) 
data["MACD_signal"]=data["MACD"].ewm(span=macd_signal).mean() 
data["MACD_oscillator"]=data.apply(lambda x:(x["MACD"]-x["MACD_signal"]), axis=1) 

data.to_csv("../stock_data/stock_week.csv", sep=",")

## 월봉 데이터 생성
data = yf.download(["VZ"], interval="1mo")
data.dropna(inplace=True) # nan있는 행 제거
data["RSI"] = talib.RSI(data["Close"], 14) # Tradingview와 일치

macd_short, macd_long, macd_signal=12,26,9 #기본값 
data["MACD_short"]=data["Close"].ewm(span=macd_short).mean() 
data["MACD_long"]=data["Close"].ewm(span=macd_long).mean() 
data["MACD"]=data.apply(lambda x: (x["MACD_short"]-x["MACD_long"]), axis=1) 
data["MACD_signal"]=data["MACD"].ewm(span=macd_signal).mean() 
data["MACD_oscillator"]=data.apply(lambda x:(x["MACD"]-x["MACD_signal"]), axis=1) 

# 폴더 먼저 생성할 것 'stock_data'
data.to_csv("../stock_data/stock_month.csv", sep=",", index=False)

# 변경
