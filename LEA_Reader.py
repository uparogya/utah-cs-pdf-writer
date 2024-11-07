import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.ticker import MaxNLocator
from re import sub

xls = pd.ExcelFile('./excel_sheet.xlsx')

data_years = [
    "2019-2020",
    "2020-2021",
    "2021-2022",
    "2022-2023",
]


def getCorrectValue(raw_value):
    if pd.isna(raw_value):
        return 0
    
    elif raw_value == 'n<10':
        return 1
    
    else:
        return raw_value
    
all_years_lea_sheets = [pd.read_excel(xls, sheet_name=f"LEA-Level Data SY {year}", header=[1]) for year in data_years]
all_leas = {}

for i in range(len(all_years_lea_sheets)):
    for index, row in all_years_lea_sheets[i].iterrows():
        if pd.isna(row['District Number (NCES)']): continue
        if int(row['District Number (NCES)']) not in all_leas:
            all_leas[int(row['District Number (NCES)'])] = row['District Name']


for district_number in all_leas:
    pdf_file = './PDF/lea_pdfs/' + sub(r'[^a-zA-Z ]', '', all_leas[district_number]).lower().replace(' ','_') + '.pdf'

    total_Total = [0,0,0,0]
    total_Female = [0,0,0,0]
    total_Male = [0,0,0,0]
    total_American_Indian_or_Alaska_Native = [0,0,0,0]
    total_Asian = [0,0,0,0]
    total_Black_or_African_American = [0,0,0,0]
    total_Hispanic_or_Latino = [0,0,0,0]
    total_Native_Hawaiian_or_Pacific_Islander = [0,0,0,0]
    total_Two_or_more_races = [0,0,0,0]
    total_White = [0,0,0,0]
    total_Disability = [0,0,0,0]
    total_Eco_Dis = [0,0,0,0]
    total_Eng_Learners = [0,0,0,0]

    for i in range(len(data_years)):
        lea_row = all_years_lea_sheets[i][all_years_lea_sheets[i]['District Number (NCES)'] == district_number]
        if lea_row.empty:
            continue

        total_Total[i] = (getCorrectValue(lea_row.iloc[0]["TOTAL: Total"]))
        total_Female[i] = (getCorrectValue(lea_row.iloc[0]["TOTAL: Female"]))
        total_Male[i] = (getCorrectValue(lea_row.iloc[0]["TOTAL: Male"]))
        total_American_Indian_or_Alaska_Native[i] = (getCorrectValue(lea_row.iloc[0]["TOTAL: American Indian or Alaska Native"]))
        total_Asian[i] = (getCorrectValue(lea_row.iloc[0]["TOTAL: Asian"]))
        total_Black_or_African_American[i] = (getCorrectValue(lea_row.iloc[0]["TOTAL: Black or African American"]))
        total_Hispanic_or_Latino[i] = (getCorrectValue(lea_row.iloc[0]["TOTAL: Hispanic or Latino"]))
        total_Native_Hawaiian_or_Pacific_Islander[i] = (getCorrectValue(lea_row.iloc[0]["TOTAL: Native Hawaiian or Pacific Islander"]))
        total_Two_or_more_races[i] = (getCorrectValue(lea_row.iloc[0]["TOTAL: Two or more races"]))
        total_White[i] = (getCorrectValue(lea_row.iloc[0]["TOTAL: White"]))
        total_Disability[i] = (getCorrectValue(lea_row.iloc[0]["TOTAL: Disability"]))
        total_Eco_Dis[i] = (getCorrectValue(lea_row.iloc[0]["TOTAL: Eco. Dis."]))
        total_Eng_Learners[i] = (getCorrectValue(lea_row.iloc[0]["TOTAL: Eng. Learners"]))
    
    with PdfPages(pdf_file) as pdf:
        fig, axs = plt.subplots(4, 3, figsize=(15, 15))
        fig.suptitle(all_leas[district_number], fontsize=16)

        axs[0, 0].plot(data_years, total_Total, label='Total', marker='o')
        axs[0, 0].plot(data_years, total_Female, label='Female', marker='o')
        axs[0, 0].plot(data_years, total_Male, label='Male', marker='o')
        axs[0, 0].set_title('Total Students')
        axs[0, 0].set_xlabel('School Year')
        axs[0, 0].set_ylabel('Students')
        axs[0, 0].set_ylim(bottom=0)
        axs[0, 0].yaxis.set_major_locator(MaxNLocator(integer=True))
        axs[0, 0].legend()
        axs[0, 0].grid()

        categories = [
            (total_American_Indian_or_Alaska_Native, 'American Indian or Alaska Native'),
            (total_Asian, 'Asian'),
            (total_Black_or_African_American, 'Black or African American'),
            (total_Hispanic_or_Latino, 'Hispanic or Latino'),
            (total_Native_Hawaiian_or_Pacific_Islander, 'Native Hawaiian or Pacific Islander'),
            (total_Two_or_more_races, 'Two or More Races'),
            (total_White, 'White'),
            (total_Disability, 'Disability'),
            (total_Eco_Dis, 'Economically Disadvantaged'),
            (total_Eng_Learners, 'English Learners'),
        ]

        axs_flat = axs.flatten()

        for i, (data, title) in enumerate(categories):
            axs_flat[i + 1].plot(data_years, data, marker='o')
            axs_flat[i + 1].set_title(title)
            axs_flat[i + 1].set_xlabel('School Year')
            axs_flat[i + 1].set_ylabel('Students')
            axs_flat[i + 1].set_ylim(bottom=0, top=max(data)*1.1)
            axs_flat[i + 1].yaxis.set_major_locator(MaxNLocator(integer=True))
            axs_flat[i + 1].grid()

        for j in range(i + 2, len(axs_flat)):
            axs_flat[j].axis('off')
        
        plt.text(0.95, 0.01, '[*] Values that are between 1 and 9 are shown as 1 due to data masking.',
             verticalalignment='bottom', horizontalalignment='right',
             transform=plt.gca().transAxes, fontsize=8, color='gray')

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        pdf.savefig(fig)
        plt.close(fig)

    print(all_leas[district_number] + ' --- Completed')
    # break