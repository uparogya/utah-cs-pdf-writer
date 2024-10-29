import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

xls = pd.ExcelFile('./excel_sheet.xlsx')

data_years = [
    "2019-2020",
    "2020-2021",
    "2021-2022",
    "2022-2023",
]

all_years_lea_sheets = [pd.read_excel(xls, sheet_name=f"LEA-Level Data SY {year}", header=[1]) for year in data_years]
all_leas = {}

for index, row in all_years_lea_sheets[0].iterrows():
    if pd.isna(row['District Number (NCES)']): continue
    all_leas[int(row['District Number (NCES)'])] = row['District Name']


for district_number in all_leas:
    for i in range(len(data_years)):

        test = all_years_lea_sheets[0][all_years_lea_sheets[0]['District Number (NCES)'] == district_number]
        print(test)

    break