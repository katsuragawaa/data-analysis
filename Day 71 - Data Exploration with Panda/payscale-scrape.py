import requests
from bs4 import BeautifulSoup

# import lxml.html as lh
import pandas as pd
from pprint import pprint

URL = (
    "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
)

page = requests.get(URL)
doc = page.content

soup = BeautifulSoup(doc, "html.parser")
table_content = soup.find_all("td")

header = []
# For each row, store each first element (header) and an empty list
for td in table_content[:6]:
    col_head = td.getText()
    # print(col_head)
    header.append(col_head.split(":")[0])

print(header)

data = []
col_data = []
for td in table_content:
    col_data = td.getText()
    # print(col_head)
    data.append(col_data.split(":")[1])

n = 6
data_rows = [data[i : i + n] for i in range(0, len(data), n)]

df = pd.DataFrame(data_rows, columns=header)

print(df)

with open("updated-salary.csv", mode="w") as f:
    df.to_csv(f, encoding='utf-8', index=False)