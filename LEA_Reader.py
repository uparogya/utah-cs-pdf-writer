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
    "2023-2024",
]


def getCorrectValue(raw_value):
    if pd.isna(raw_value):
        return 0
    
    elif raw_value == 'n<10':
        return 1
    
    else:
        return int(raw_value)

def plot_student_data(pdf, data_years, categories, title, district_name):
    fig, axs = plt.subplots(4, 3, figsize=(15, 15))
    fig.suptitle(f"{district_name}\n\n{title}", fontsize=16)

    axs[0, 0].plot(data_years, categories['Total'], label='Total', marker='o')
    axs[0, 0].plot(data_years, categories['Female'], label='Female', marker='o')
    axs[0, 0].plot(data_years, categories['Male'], label='Male', marker='o')
    axs[0, 0].set_title('Total Students')
    axs[0, 0].set_xlabel('School Year')
    axs[0, 0].set_ylabel('Students')
    axs[0, 0].set_ylim(bottom=0)
    axs[0, 0].yaxis.set_major_locator(MaxNLocator(integer=True))
    axs[0, 0].legend()
    axs[0, 0].grid()

    axs_flat = axs.flatten()
    categories.pop(list(categories.keys())[0])
    categories.pop(list(categories.keys())[1])

    for i, (category_name, data) in enumerate(categories.items()):
        if category_name not in ['Total', 'Female', 'Male']:
            axs_flat[i].plot(data_years, data, marker='o')
            axs_flat[i].set_title(category_name)
            axs_flat[i].set_xlabel('School Year')
            axs_flat[i].set_ylabel('Students')
            axs_flat[i].set_ylim(bottom=0, top=1) if all(val == 0 for val in data) else axs_flat[i].set_ylim(bottom=0, top=max(data)*1.1)
            axs_flat[i].yaxis.set_major_locator(MaxNLocator(integer=True))
            axs_flat[i].grid()

    for j in range(i + 1, len(axs_flat)):
        axs_flat[j].axis('off')

    plt.text(0.95, 0.01, '[*] Values that are between 1 and 9 are shown as 1 due to data masking.',
             verticalalignment='bottom', horizontalalignment='right',
             transform=plt.gca().transAxes, fontsize=8, color='gray')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    pdf.savefig(fig)
    plt.close(fig)
    
all_years_lea_sheets = [pd.read_excel(xls, sheet_name=f"LEA-Level Data SY {year}", header=[1]) for year in data_years]
all_leas = {}

for i in range(len(all_years_lea_sheets)):
    for index, row in all_years_lea_sheets[i].iterrows():
        if pd.isna(row['District Number (NCES)']): continue
        if int(row['District Number (NCES)']) not in all_leas:
            all_leas[int(row['District Number (NCES)'])] = row['District Name']


for district_number in all_leas:
    pdf_file = './PDF/lea_pdfs/' + sub(r'[^a-zA-Z ]', '', all_leas[district_number]).lower().replace(' ','_') + '.pdf'

    total_Total, cs_Total = [0]*len(data_years), [0]*len(data_years)
    total_Female, cs_Female = [0]*len(data_years), [0]*len(data_years)
    total_Male, cs_Male = [0]*len(data_years), [0]*len(data_years)
    total_American_Indian_or_Alaska_Native, cs_American_Indian_or_Alaska_Native = [0]*len(data_years), [0]*len(data_years)
    total_Asian, cs_Asian = [0]*len(data_years), [0]*len(data_years)
    total_Black_or_African_American, cs_Black_or_African_American = [0]*len(data_years), [0]*len(data_years)
    total_Hispanic_or_Latino, cs_Hispanic_or_Latino = [0]*len(data_years), [0]*len(data_years)
    total_Native_Hawaiian_or_Pacific_Islander, cs_Native_Hawaiian_or_Pacific_Islander = [0]*len(data_years), [0]*len(data_years)
    total_Two_or_more_races, cs_Two_or_more_races = [0]*len(data_years), [0]*len(data_years)
    total_White, cs_White = [0]*len(data_years), [0]*len(data_years)
    total_Disability, cs_Disability = [0]*len(data_years), [0]*len(data_years)
    total_Eco_Dis, cs_Eco_Dis = [0]*len(data_years), [0]*len(data_years)
    total_Eng_Learners, cs_Eng_Learners = [0]*len(data_years), [0]*len(data_years)

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

        cs_Total[i] = (getCorrectValue(lea_row.iloc[0]["CS: Total"]))
        cs_Female[i] = (getCorrectValue(lea_row.iloc[0]["CS: Female"]))
        cs_Male[i] = (getCorrectValue(lea_row.iloc[0]["CS: Male"]))
        cs_American_Indian_or_Alaska_Native[i] = (getCorrectValue(lea_row.iloc[0]["CS: American Indian or Alaska Native"]))
        cs_Asian[i] = (getCorrectValue(lea_row.iloc[0]["CS: Asian"]))
        cs_Black_or_African_American[i] = (getCorrectValue(lea_row.iloc[0]["CS: Black or African American"]))
        cs_Hispanic_or_Latino[i] = (getCorrectValue(lea_row.iloc[0]["CS: Hispanic or Latino"]))
        cs_Native_Hawaiian_or_Pacific_Islander[i] = (getCorrectValue(lea_row.iloc[0]["CS: Native Hawaiian or Pacific Islander"]))
        cs_Two_or_more_races[i] = (getCorrectValue(lea_row.iloc[0]["CS: Two or more races"]))
        cs_White[i] = (getCorrectValue(lea_row.iloc[0]["CS: White"]))
        cs_Disability[i] = (getCorrectValue(lea_row.iloc[0]["CS: Disability"]))
        cs_Eco_Dis[i] = (getCorrectValue(lea_row.iloc[0]["CS: Eco. Dis."]))
        cs_Eng_Learners[i] = (getCorrectValue(lea_row.iloc[0]["CS: Eng. Learners"]))
    
    with PdfPages(pdf_file) as pdf:
        total_categories = {
            'Total': total_Total,
            'Female': total_Female,
            'Male': total_Male,
            'American Indian or Alaska Native': total_American_Indian_or_Alaska_Native,
            'Asian': total_Asian,
            'Black or African American': total_Black_or_African_American,
            'Hispanic or Latino': total_Hispanic_or_Latino,
            'Native Hawaiian or Pacific Islander': total_Native_Hawaiian_or_Pacific_Islander,
            'Two or More Races': total_Two_or_more_races,
            'White': total_White,
            'Disability': total_Disability,
            'Economically Disadvantaged': total_Eco_Dis,
            'English Learners': total_Eng_Learners
        }
        plot_student_data(pdf, data_years, total_categories, 'Total Students', all_leas[district_number])

        cs_categories = {
            'Total': cs_Total,
            'Female': cs_Female,
            'Male': cs_Male,
            'American Indian or Alaska Native': cs_American_Indian_or_Alaska_Native,
            'Asian': cs_Asian,
            'Black or African American': cs_Black_or_African_American,
            'Hispanic or Latino': cs_Hispanic_or_Latino,
            'Native Hawaiian or Pacific Islander': cs_Native_Hawaiian_or_Pacific_Islander,
            'Two or More Races': cs_Two_or_more_races,
            'White': cs_White,
            'Disability': cs_Disability,
            'Economically Disadvantaged': cs_Eco_Dis,
            'English Learners': cs_Eng_Learners
        }
        plot_student_data(pdf, data_years, cs_categories, 'All CS', all_leas[district_number])

    print(all_leas[district_number] + ' --- Completed')
    # break