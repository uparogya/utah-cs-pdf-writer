import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# pandas configurations
# pd.set_option('display.max_rows', 1)
# pd.set_option('display.max_columns', 98)

xls = pd.ExcelFile('./excel_sheet.xlsx')

data_years = [
    "2019-2020",
    "2020-2021",
    "2021-2022",
    "2022-2023",
]

all_years_lea_sheets = [pd.read_excel(xls, sheet_name=f"LEA-Level Data SY {year}", header=[1]) for year in data_years]
all_years_school_sheets = [pd.read_excel(xls, sheet_name=f"School-Level Data SY {year}", header=[1]) for year in data_years]


school_number_nces = 1512
school_name = "Green Canyon High School"
pdf_file = "test_green_canyon_high_school.pdf"
x_coordinates = np.array(data_years)
total_values = []
female_values = []
male_values = []
native_values = []
asian_values = []
black_values = []
hispanic_values = []
pacific_values = []
two_values = []
white_values = []

for index, single_year_school_df in enumerate(all_years_school_sheets):
    test_data = single_year_school_df.loc[single_year_school_df["School Number (NCES)"] == school_number_nces]

    total_value = test_data.iloc[0]["TOTAL: Total"]
    female_value = test_data.iloc[0]["TOTAL: Female"]
    male_value = test_data.iloc[0]["TOTAL: Male"]
    native_value = test_data.iloc[0]["TOTAL: American Indian or Alaska Native"]
    asian_value = test_data.iloc[0]["TOTAL: Asian"]
    black_value = test_data.iloc[0]["TOTAL: Black or African American"]
    hispanic_value = test_data.iloc[0]["TOTAL: Hispanic or Latino"]
    pacific_value = test_data.iloc[0]["TOTAL: Native Hawaiian or Pacific Islander"]
    two_value = test_data.iloc[0]["TOTAL: Two or more races"]
    white_value = test_data.iloc[0]["TOTAL: White"]

    total_values.append(0 if total_value in ["n<10", "N/A"] or test_data.empty else total_value)
    female_values.append(0 if female_value in ["n<10", "N/A"] or test_data.empty else female_value)
    male_values.append(0 if male_value in ["n<10", "N/A"] or test_data.empty else male_value)
    native_values.append(0 if native_value in ["n<10", "N/A"] or test_data.empty else native_value)
    asian_values.append(0 if asian_value in ["n<10", "N/A"] or test_data.empty else asian_value)
    black_values.append(0 if black_value in ["n<10", "N/A"] or test_data.empty else black_value)
    hispanic_values.append(0 if hispanic_value in ["n<10", "N/A"] or test_data.empty else hispanic_value)
    pacific_values.append(0 if pacific_value in ["n<10", "N/A"] or test_data.empty else pacific_value)
    two_values.append(0 if two_value in ["n<10", "N/A"] or test_data.empty else two_value)
    white_values.append(0 if white_value in ["n<10", "N/A"] or test_data.empty else white_value)

# with PdfPages(pdf_file) as pdf:
#     fig, axs = plt.subplots(4, 3, figsize=(22, 17))
#     fig.suptitle(school_name + " (NCES: " + str(school_number_nces) + ")\n", fontsize=14)

#     y_coordinates = np.array(total_values)
#     axs[0,0].plot(x_coordinates, y_coordinates)
#     axs[0,0].set_title("Total Students")
#     axs[0,0].set_xlabel("School Year")
#     axs[0,0].set_ylabel("Number")

#     y_coordinates = np.array(female_values)
#     axs[0,1].plot(x_coordinates, y_coordinates)
#     axs[0,1].set_title("Total Female")
#     axs[0,1].set_xlabel("School Year")
#     axs[0,1].set_ylabel("Number")

#     y_coordinates = np.array(male_values)
#     axs[0,2].plot(x_coordinates, y_coordinates)
#     axs[0,2].set_title("Total Male")
#     axs[0,2].set_xlabel("School Year")
#     axs[0,2].set_ylabel("Number")

#     y_coordinates = np.array(native_values)
#     axs[1,0].plot(x_coordinates, y_coordinates)
#     axs[1,0].set_title("Total American Indian or Alaska Native")
#     axs[1,0].set_xlabel("School Year")
#     axs[1,0].set_ylabel("Number")

#     y_coordinates = np.array(asian_values)
#     axs[1,1].plot(x_coordinates, y_coordinates)
#     axs[1,1].set_title("Total Asian")
#     axs[1,1].set_xlabel("School Year")
#     axs[1,1].set_ylabel("Number")

#     y_coordinates = np.array(black_values)
#     axs[1,2].plot(x_coordinates, y_coordinates)
#     axs[1,2].set_title("Total Black or African American")
#     axs[1,2].set_xlabel("School Year")
#     axs[1,2].set_ylabel("Number")

#     y_coordinates = np.array(hispanic_values)
#     axs[2,0].plot(x_coordinates, y_coordinates)
#     axs[2,0].set_title("Total Hispanic or Latino")
#     axs[2,0].set_xlabel("School Year")
#     axs[2,0].set_ylabel("Number")

#     y_coordinates = np.array(pacific_values)
#     axs[2,1].plot(x_coordinates, y_coordinates)
#     axs[2,1].set_title("Total Native Hawaiian or Pacific Islander")
#     axs[2,1].set_xlabel("School Year")
#     axs[2,1].set_ylabel("Number")

#     y_coordinates = np.array(white_values)
#     axs[2,2].plot(x_coordinates, y_coordinates)
#     axs[2,2].set_title("Total White")
#     axs[2,2].set_xlabel("School Year")
#     axs[2,2].set_ylabel("Number")

#     y_coordinates = np.array(two_values)
#     axs[3,0].plot(x_coordinates, y_coordinates)
#     axs[3,0].set_title("Total Two or more races")
#     axs[3,0].set_xlabel("School Year")
#     axs[3,0].set_ylabel("Number")

#     axs[3, 1].set_visible(False)
#     axs[3, 2].set_visible(False)

#     plt.tight_layout()
#     pdf.savefig()
#     plt.close()



# create a list/dictionary of all the districts and all the schools

# for current_year_df in all_years_lea_sheets:
#     for index, row in current_year_df.iterrows():
#         district_number_nces = row["District Number (NCES)"]
#         print(district_number_nces)
#         break
#     # print(current_year_df)
#     break