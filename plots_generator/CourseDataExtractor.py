import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
from re import sub
from ExtractionFunctions import ExtractionTools

xls = ExtractionTools.xls
data_years = ExtractionTools.data_years

class CourseDataExtraction:

    def getData(self):
        all_years_course_sheets = [pd.read_excel(xls, sheet_name=f"Course-Level Data SY {year}", header=[1]) for year in data_years]
        all_courses = {}

        for i in range(len(all_years_course_sheets)):
            for index, row in all_years_course_sheets[i].iterrows():
                if pd.isna(row['Course Code']): continue
                if int(row['Course Code']) not in all_courses:
                    all_courses[int(row['Course Code'])] = row['Course Name']
        
        concurrent_enrollment_courses = {}
        
        for course_code in all_courses:
            pdf_file = './PDF/course_pdfs/' + sub(r'[^a-zA-Z ]', '', all_courses[course_code]).lower().replace(' ','_') + '.pdf'

            if 'CE' in all_courses[course_code]:
                concurrent_enrollment_courses[course_code] = course_code - 13000
                continue

            total_Total = [0]*len(data_years)
            total_Female = [0]*len(data_years)
            total_Male = [0]*len(data_years)
            total_American_Indian_or_Alaska_Native = [0]*len(data_years)
            total_Asian = [0]*len(data_years)
            total_Black_or_African_American = [0]*len(data_years)
            total_Hispanic_or_Latino = [0]*len(data_years)
            total_Native_Hawaiian_or_Pacific_Islander = [0]*len(data_years)
            total_Two_or_more_races = [0]*len(data_years)
            total_White = [0]*len(data_years)
            total_Disability = [0]*len(data_years)
            total_Eco_Dis = [0]*len(data_years)
            total_Eng_Learners = [0]*len(data_years)

            for i in range(len(data_years)):
                lea_row = all_years_course_sheets[i][all_years_course_sheets[i]['Course Code'] == course_code]
                if lea_row.empty:
                    continue

                total_Total[i] = (ExtractionTools.getCorrectValue(lea_row.iloc[0]["Total"]))
                total_Female[i] = (ExtractionTools.getCorrectValue(lea_row.iloc[0]["Female"]))
                total_Male[i] = (ExtractionTools.getCorrectValue(lea_row.iloc[0]["Male"]))
                total_American_Indian_or_Alaska_Native[i] = (ExtractionTools.getCorrectValue(lea_row.iloc[0]["American Indian or Alaska Native"]))
                total_Asian[i] = (ExtractionTools.getCorrectValue(lea_row.iloc[0]["Asian"]))
                total_Black_or_African_American[i] = (ExtractionTools.getCorrectValue(lea_row.iloc[0]["Black or African American"]))
                total_Hispanic_or_Latino[i] = (ExtractionTools.getCorrectValue(lea_row.iloc[0]["Hispanic or Latino"]))
                total_Native_Hawaiian_or_Pacific_Islander[i] = (ExtractionTools.getCorrectValue(lea_row.iloc[0]["Native Hawaiian or Pacific Islander"]))
                total_Two_or_more_races[i] = (ExtractionTools.getCorrectValue(lea_row.iloc[0]["Two or more races"]))
                total_White[i] = (ExtractionTools.getCorrectValue(lea_row.iloc[0]["White"]))
                total_Disability[i] = (ExtractionTools.getCorrectValue(lea_row.iloc[0]["Disability"]))
                total_Eco_Dis[i] = (ExtractionTools.getCorrectValue(lea_row.iloc[0]["Eco. Dis."]))
                total_Eng_Learners[i] = (ExtractionTools.getCorrectValue(lea_row.iloc[0]["Eng. Learners"]))

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

                    ExtractionTools.plotStudentData(pdf, data_years, total_categories, 'Total Students', all_courses[course_code], self.plotPercentages(course_code))
        
        for ce_course_code in concurrent_enrollment_courses:
            pdf_file = './PDF/course_pdfs/' + sub(r'[^a-zA-Z ]', '', all_courses[concurrent_enrollment_courses[ce_course_code]]).lower().replace(' ','_') + '.pdf'

            total_Total = [0]*len(data_years)
            total_Female = [0]*len(data_years)
            total_Male = [0]*len(data_years)
            total_American_Indian_or_Alaska_Native = [0]*len(data_years)
            total_Asian = [0]*len(data_years)
            total_Black_or_African_American = [0]*len(data_years)
            total_Hispanic_or_Latino = [0]*len(data_years)
            total_Native_Hawaiian_or_Pacific_Islander = [0]*len(data_years)
            total_Two_or_more_races = [0]*len(data_years)
            total_White = [0]*len(data_years)
            total_Disability = [0]*len(data_years)
            total_Eco_Dis = [0]*len(data_years)
            total_Eng_Learners = [0]*len(data_years)

            for i in range(len(data_years)):
                lea_row = all_years_course_sheets[i][all_years_course_sheets[i]['Course Code'] == concurrent_enrollment_courses[ce_course_code]]
                lea_row_ce = all_years_course_sheets[i][all_years_course_sheets[i]['Course Code'] == ce_course_code]

                if lea_row.empty or lea_row_ce.empty:
                    continue

                total_Total[i] = ExtractionTools.concurrentEnrollmentAddedValueCorrection((ExtractionTools.getCorrectValue(lea_row.iloc[0]["Total"])) + (ExtractionTools.getCorrectValue(lea_row_ce.iloc[0]["Total"])))
                total_Female[i] = ExtractionTools.concurrentEnrollmentAddedValueCorrection((ExtractionTools.getCorrectValue(lea_row.iloc[0]["Female"])) + (ExtractionTools.getCorrectValue(lea_row_ce.iloc[0]["Female"])))
                total_Male[i] = ExtractionTools.concurrentEnrollmentAddedValueCorrection((ExtractionTools.getCorrectValue(lea_row.iloc[0]["Male"])) + (ExtractionTools.getCorrectValue(lea_row_ce.iloc[0]["Male"])))
                total_American_Indian_or_Alaska_Native[i] = ExtractionTools.concurrentEnrollmentAddedValueCorrection((ExtractionTools.getCorrectValue(lea_row.iloc[0]["American Indian or Alaska Native"])) + (ExtractionTools.getCorrectValue(lea_row_ce.iloc[0]["American Indian or Alaska Native"])))
                total_Asian[i] = ExtractionTools.concurrentEnrollmentAddedValueCorrection((ExtractionTools.getCorrectValue(lea_row.iloc[0]["Asian"])) + (ExtractionTools.getCorrectValue(lea_row_ce.iloc[0]["Asian"])))
                total_Black_or_African_American[i] = ExtractionTools.concurrentEnrollmentAddedValueCorrection((ExtractionTools.getCorrectValue(lea_row.iloc[0]["Black or African American"])) + (ExtractionTools.getCorrectValue(lea_row_ce.iloc[0]["Black or African American"])))
                total_Hispanic_or_Latino[i] = ExtractionTools.concurrentEnrollmentAddedValueCorrection((ExtractionTools.getCorrectValue(lea_row.iloc[0]["Hispanic or Latino"])) + (ExtractionTools.getCorrectValue(lea_row_ce.iloc[0]["Hispanic or Latino"])))
                total_Native_Hawaiian_or_Pacific_Islander[i] = ExtractionTools.concurrentEnrollmentAddedValueCorrection((ExtractionTools.getCorrectValue(lea_row.iloc[0]["Native Hawaiian or Pacific Islander"])) + (ExtractionTools.getCorrectValue(lea_row_ce.iloc[0]["Native Hawaiian or Pacific Islander"])))
                total_Two_or_more_races[i] = ExtractionTools.concurrentEnrollmentAddedValueCorrection((ExtractionTools.getCorrectValue(lea_row.iloc[0]["Two or more races"])) + (ExtractionTools.getCorrectValue(lea_row_ce.iloc[0]["Two or more races"])))
                total_White[i] = ExtractionTools.concurrentEnrollmentAddedValueCorrection((ExtractionTools.getCorrectValue(lea_row.iloc[0]["White"])) + (ExtractionTools.getCorrectValue(lea_row_ce.iloc[0]["White"])))
                total_Disability[i] = ExtractionTools.concurrentEnrollmentAddedValueCorrection((ExtractionTools.getCorrectValue(lea_row.iloc[0]["Disability"])) + (ExtractionTools.getCorrectValue(lea_row_ce.iloc[0]["Disability"])))
                total_Eco_Dis[i] = ExtractionTools.concurrentEnrollmentAddedValueCorrection((ExtractionTools.getCorrectValue(lea_row.iloc[0]["Eco. Dis."])) + (ExtractionTools.getCorrectValue(lea_row_ce.iloc[0]["Eco. Dis."])))
                total_Eng_Learners[i] = ExtractionTools.concurrentEnrollmentAddedValueCorrection((ExtractionTools.getCorrectValue(lea_row.iloc[0]["Eng. Learners"])) + (ExtractionTools.getCorrectValue(lea_row_ce.iloc[0]["Eng. Learners"])))

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

                    ExtractionTools.plotStudentData(pdf, data_years, total_categories, 'Total Students', all_courses[concurrent_enrollment_courses[ce_course_code]] + ' + CE', self.plotPercentages(ce_course_code))

    def plotPercentages(self, course_code):
        percentage_required_courses = set([35020000007, 35020000060, 35020000030, 35020000035, 35020000045])
        percentage_required_courses = percentage_required_courses | set([course + 13000 for course in percentage_required_courses])
        return True if course_code in percentage_required_courses else False

CourseDataExtraction().getData()