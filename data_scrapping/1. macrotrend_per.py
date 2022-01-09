## 기본 통계 ## 
# macrotrends data 가져오기
# 참고 링크
# https://pypi.org/project/finpie/#A41

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.macrotrends.net/stocks/charts/VZ/verizon/pe-ratio"
res = requests.get(url = url)
soup = BeautifulSoup(res.text, "lxml")

# column names
table = soup.find("table", attrs={"class":"table"})
name_list = table.select('thead:nth-child(2) > tr > th')
name_list = [i.text for i in name_list]

# row 
per_table = soup.find("table", attrs={"class":"table"}).tbody
per_table = per_table.find_all("tr")
row_list = [i.find_all("td") for i in per_table]
row_list = [[j.text for j in i] for i in row_list]

# 폴더 먼저 생성할 것 'stock_data_basicStat'
data = pd.DataFrame(row_list, columns=name_list)
data.to_csv("../stock_data_basicStat/per.csv", sep=",", index=False)
