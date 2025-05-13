import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
from ExtractionFunctions import ExtractionTools

utah_sheet = [pd.read_excel(ExtractionTools.xls, sheet_name=f"State-Level Data By Year", header=[1])]
data_years = ExtractionTools.data_years

class StateDataExtraction:

    def getData():
        total_Total, cs_Total, csc_Total, csb_Total, csa_Total, csr_Total = [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years)
        total_Female, cs_Female, csc_Female, csb_Female, csa_Female, csr_Female = [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years)
        total_Male, cs_Male, csc_Male, csb_Male, csa_Male, csr_Male = [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years)
        total_American_Indian_or_Alaska_Native, cs_American_Indian_or_Alaska_Native, csc_American_Indian_or_Alaska_Native, csb_American_Indian_or_Alaska_Native, csa_American_Indian_or_Alaska_Native, csr_American_Indian_or_Alaska_Native = [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years)
        total_Asian, cs_Asian, csc_Asian, csb_Asian, csa_Asian, csr_Asian = [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years)
        total_Black_or_African_American, cs_Black_or_African_American, csc_Black_or_African_American, csb_Black_or_African_American, csa_Black_or_African_American, csr_Black_or_African_American = [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years)
        total_Hispanic_or_Latino, cs_Hispanic_or_Latino, csc_Hispanic_or_Latino, csb_Hispanic_or_Latino, csa_Hispanic_or_Latino, csr_Hispanic_or_Latino = [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years)
        total_Native_Hawaiian_or_Pacific_Islander, cs_Native_Hawaiian_or_Pacific_Islander, csc_Native_Hawaiian_or_Pacific_Islander, csb_Native_Hawaiian_or_Pacific_Islander, csa_Native_Hawaiian_or_Pacific_Islander, csr_Native_Hawaiian_or_Pacific_Islander = [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years)
        total_Two_or_more_races, cs_Two_or_more_races, csc_Two_or_more_races, csb_Two_or_more_races, csa_Two_or_more_races, csr_Two_or_more_races = [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years)
        total_White, cs_White, csc_White, csb_White, csa_White, csr_White = [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years)
        total_Disability, cs_Disability, csc_Disability, csb_Disability, csa_Disability, csr_Disability = [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years)
        total_Eco_Dis, cs_Eco_Dis, csc_Eco_Dis, csb_Eco_Dis, csa_Eco_Dis, csr_Eco_Dis = [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years)
        total_Eng_Learners, cs_Eng_Learners, csc_Eng_Learners, csb_Eng_Learners, csa_Eng_Learners, csr_Eng_Learners = [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years), [0]*len(data_years)

        for i in range(len(data_years)):
            total_Total[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["TOTAL: Total"])
            total_Female[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["TOTAL: Female"])
            total_Male[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["TOTAL: Male"])
            total_American_Indian_or_Alaska_Native[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["TOTAL: American Indian or Alaska Native"])
            total_Asian[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["TOTAL: Asian"])
            total_Black_or_African_American[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["TOTAL: Black or African American"])
            total_Hispanic_or_Latino[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["TOTAL: Hispanic or Latino"])
            total_Native_Hawaiian_or_Pacific_Islander[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["TOTAL: Native Hawaiian or Pacific Islander"])
            total_Two_or_more_races[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["TOTAL: Two or more races"])
            total_White[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["TOTAL: White"])
            total_Disability[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["TOTAL: Disability"])
            total_Eco_Dis[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["TOTAL: Eco. Dis."])
            total_Eng_Learners[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["TOTAL: Eng. Learners"])

            cs_Total[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CS: Total"])
            cs_Female[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CS: Female"])
            cs_Male[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CS: Male"])
            cs_American_Indian_or_Alaska_Native[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CS: American Indian or Alaska Native"])
            cs_Asian[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CS: Asian"])
            cs_Black_or_African_American[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CS: Black or African American"])
            cs_Hispanic_or_Latino[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CS: Hispanic or Latino"])
            cs_Native_Hawaiian_or_Pacific_Islander[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CS: Native Hawaiian or Pacific Islander"])
            cs_Two_or_more_races[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CS: Two or more races"])
            cs_White[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CS: White"])
            cs_Disability[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CS: Disability"])
            cs_Eco_Dis[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CS: Eco. Dis."])
            cs_Eng_Learners[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CS: Eng. Learners"])

            csc_Total[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSC: Total"])
            csc_Female[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSC: Female"])
            csc_Male[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSC: Male"])
            csc_American_Indian_or_Alaska_Native[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSC: American Indian or Alaska Native"])
            csc_Asian[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSC: Asian"])
            csc_Black_or_African_American[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSC: Black or African American"])
            csc_Hispanic_or_Latino[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSC: Hispanic or Latino"])
            csc_Native_Hawaiian_or_Pacific_Islander[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSC: Native Hawaiian or Pacific Islander"])
            csc_Two_or_more_races[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSC: Two or more races"])
            csc_White[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSC: White"])
            csc_Disability[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSC: Disability"])
            csc_Eco_Dis[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSC: Eco. Dis."])
            csc_Eng_Learners[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSC: Eng. Learners"])

            csb_Total[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSB: Total"])
            csb_Female[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSB: Female"])
            csb_Male[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSB: Male"])
            csb_American_Indian_or_Alaska_Native[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSB: American Indian or Alaska Native"])
            csb_Asian[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSB: Asian"])
            csb_Black_or_African_American[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSB: Black or African American"])
            csb_Hispanic_or_Latino[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSB: Hispanic or Latino"])
            csb_Native_Hawaiian_or_Pacific_Islander[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSB: Native Hawaiian or Pacific Islander"])
            csb_Two_or_more_races[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSB: Two or more races"])
            csb_White[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSB: White"])
            csb_Disability[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSB: Disability"])
            csb_Eco_Dis[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSB: Eco. Dis."])
            csb_Eng_Learners[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSB: Eng. Learners"])

            csa_Total[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSA: Total"])
            csa_Female[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSA: Female"])
            csa_Male[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSA: Male"])
            csa_American_Indian_or_Alaska_Native[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSA: American Indian or Alaska Native"])
            csa_Asian[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSA: Asian"])
            csa_Black_or_African_American[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSA: Black or African American"])
            csa_Hispanic_or_Latino[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSA: Hispanic or Latino"])
            csa_Native_Hawaiian_or_Pacific_Islander[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSA: Native Hawaiian or Pacific Islander"])
            csa_Two_or_more_races[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSA: Two or more races"])
            csa_White[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSA: White"])
            csa_Disability[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSA: Disability"])
            csa_Eco_Dis[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSA: Eco. Dis."])
            csa_Eng_Learners[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSA: Eng. Learners"])

            csr_Total[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSR: Total"])
            csr_Female[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSR: Female"])
            csr_Male[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSR: Male"])
            csr_American_Indian_or_Alaska_Native[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSR: American Indian or Alaska Native"])
            csr_Asian[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSR: Asian"])
            csr_Black_or_African_American[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSR: Black or African American"])
            csr_Hispanic_or_Latino[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSR: Hispanic or Latino"])
            csr_Native_Hawaiian_or_Pacific_Islander[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSR: Native Hawaiian or Pacific Islander"])
            csr_Two_or_more_races[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSR: Two or more races"])
            csr_White[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSR: White"])
            csr_Disability[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSR: Disability"])
            csr_Eco_Dis[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSR: Eco. Dis."])
            csr_Eng_Learners[i] = ExtractionTools.getCorrectValue(utah_sheet[0].iloc[i]["CSR: Eng. Learners"])
    
        with PdfPages('./PDF/utah_pdfs/state_data.pdf') as pdf:
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

            csc_categories = {
                'Total': csc_Total,
                'Female': csc_Female,
                'Male': csc_Male,
                'American Indian or Alaska Native': csc_American_Indian_or_Alaska_Native,
                'Asian': csc_Asian,
                'Black or African American': csc_Black_or_African_American,
                'Hispanic or Latino': csc_Hispanic_or_Latino,
                'Native Hawaiian or Pacific Islander': csc_Native_Hawaiian_or_Pacific_Islander,
                'Two or More Races': csc_Two_or_more_races,
                'White': csc_White,
                'Disability': csc_Disability,
                'Economically Disadvantaged': csc_Eco_Dis,
                'English Learners': csc_Eng_Learners
            }

            csb_categories = {
                'Total': csb_Total,
                'Female': csb_Female,
                'Male': csb_Male,
                'American Indian or Alaska Native': csb_American_Indian_or_Alaska_Native,
                'Asian': csb_Asian,
                'Black or African American': csb_Black_or_African_American,
                'Hispanic or Latino': csb_Hispanic_or_Latino,
                'Native Hawaiian or Pacific Islander': csb_Native_Hawaiian_or_Pacific_Islander,
                'Two or More Races': csb_Two_or_more_races,
                'White': csb_White,
                'Disability': csb_Disability,
                'Economically Disadvantaged': csb_Eco_Dis,
                'English Learners': csb_Eng_Learners
            }

            csa_categories = {
                'Total': csa_Total,
                'Female': csa_Female,
                'Male': csa_Male,
                'American Indian or Alaska Native': csa_American_Indian_or_Alaska_Native,
                'Asian': csa_Asian,
                'Black or African American': csa_Black_or_African_American,
                'Hispanic or Latino': csa_Hispanic_or_Latino,
                'Native Hawaiian or Pacific Islander': csa_Native_Hawaiian_or_Pacific_Islander,
                'Two or More Races': csa_Two_or_more_races,
                'White': csa_White,
                'Disability': csa_Disability,
                'Economically Disadvantaged': csa_Eco_Dis,
                'English Learners': csa_Eng_Learners
            }

            csr_categories = {
                'Total': csr_Total,
                'Female': csr_Female,
                'Male': csr_Male,
                'American Indian or Alaska Native': csr_American_Indian_or_Alaska_Native,
                'Asian': csr_Asian,
                'Black or African American': csr_Black_or_African_American,
                'Hispanic or Latino': csr_Hispanic_or_Latino,
                'Native Hawaiian or Pacific Islander': csr_Native_Hawaiian_or_Pacific_Islander,
                'Two or More Races': csr_Two_or_more_races,
                'White': csr_White,
                'Disability': csr_Disability,
                'Economically Disadvantaged': csr_Eco_Dis,
                'English Learners': csr_Eng_Learners
            }

            ExtractionTools.plotStudentData(pdf, data_years, cs_categories, 'All CS', 'Utah State Data', labelPercentages=True)
            ExtractionTools.plotStudentData(pdf, data_years, csc_categories, 'Core CS', 'Utah State Data', labelPercentages=True)
            ExtractionTools.plotStudentData(pdf, data_years, csr_categories, 'Related CS', 'Utah State Data', labelPercentages=True)
            ExtractionTools.plotStudentData(pdf, data_years, csb_categories, 'Basic CS', 'Utah State Data', labelPercentages=True)
            ExtractionTools.plotStudentData(pdf, data_years, csa_categories, 'Advanced CS', 'Utah State Data', labelPercentages=True)
            ExtractionTools.plotStudentData(pdf, data_years, total_categories, 'Total Students', 'Utah State Data', labelPercentages=True)
        
        
        with PdfPages('./PDF/utah_pdfs/state_gender_data.pdf') as pdf:
            gender_data_all_categories = {
                'Total Students': {
                    'Total': total_Total,
                    'Female': total_Female,
                    'Male': total_Male
                },
                'All CS': {
                    'Total': cs_Total,
                    'Female': cs_Female,
                    'Male': cs_Male
                },
                'Core CS': {
                    'Total': csc_Total,
                    'Female': csc_Female,
                    'Male': csc_Male
                },
                'Related CS': {
                    'Total': csr_Total,
                    'Female': csr_Female,
                    'Male': csr_Male
                },
                'Basic CS': {
                    'Total': csb_Total,
                    'Female': csb_Female,
                    'Male': csb_Male
                },
                'Advanced CS': {
                    'Total': csa_Total,
                    'Female': csa_Female,
                    'Male': csa_Male
                }
            }

            ExtractionTools.plotGenderGraphs(pdf, data_years, gender_data_all_categories, 'Gender Data - All Categories', 'Utah State Data')
        
StateDataExtraction.getData()