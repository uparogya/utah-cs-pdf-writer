import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

class ExtractionTools:

    print("Extracting Data...")

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
    
    def plotStudentData(pdf, data_years, categories, subTitle, title, labelPercentages = False):
        fig, axs = plt.subplots(4, 3, figsize=(15, 15))
        fig.suptitle(f"{title}\n\n{subTitle}", fontsize=16)

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
        total_students = categories['Total']
        categories.pop(list(categories.keys())[0])
        categories.pop(list(categories.keys())[1])

        for i, (category_name, data) in enumerate(categories.items()):
            if category_name not in ['Total', 'Female', 'Male']:
                axs_flat[i].plot(data_years, data, marker='o')

                if labelPercentages:
                    for j, year in enumerate(data_years):
                        # axs_flat[i].annotate(str(data[j])+'[99%]', (data_years[j], data[j]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)
                        axs_flat[i].annotate(str(round(data[j]*100/total_students[j],2))+'%', (data_years[j], data[j]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, fontweight='light', color='black')

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

        # print(title + " --- Completed")

    def concurrentEnrollmentAddedValueCorrection(raw_value):
        return 1 if raw_value == 2 else raw_value