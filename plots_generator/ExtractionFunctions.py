import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from PIL import Image

class ExtractionTools:

    print("Extracting Data...")

    xls = pd.ExcelFile('./assets/excel_sheet.xlsx')

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
                        if total_students[j] == 0:
                            continue
                        axs_flat[i].annotate(str(round(data[j]*100/total_students[j],2))+'%', (data_years[j], data[j]), textcoords="offset points", xytext=(5,-15), ha='center', fontsize=8, fontweight='bold', color='firebrick')

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

    def plotGenderGraphs(pdf, data_years, gender_data_all_categories, subTitle, title, institution = 'Utah'):
        fig, axs = plt.subplots(3, 4, figsize=(23, 15))
        fig.suptitle(title, fontsize=16, fontweight='bold')
        fig.text(0.5, 0.95, subTitle, fontsize=12, fontweight='bold', ha='center')
        axs_flat = axs.flatten()

        for i, (category_title, category_data) in enumerate(gender_data_all_categories.items()):
            if i == 0:
                ax_text = axs_flat[2 * i + 1]
                ax_img = axs_flat[2 * i]
                ax_text.axis('off')
                ax_img.axis('off')

                pos0 = axs_flat[0].get_position()
                pos1 = axs_flat[1].get_position()
                x0 = pos0.x0 - 0.05
                y0 = pos0.y0 + 0.033
                width = pos1.x1 - pos0.x0
                height = pos0.height

                ax_img = fig.add_axes([x0, y0, width, height])
                ax_img.axis('off')

                img = Image.open("./assets/images/cs_course_venn_diagram.png")
                ax_img.imshow(img, aspect='auto')

                ax_img.text(
                    0.5, -0.02, "In 2023-24, the total "+institution+" student population for grades 9-12 was " + f"{category_data['Total'][-1]:,}",
                    transform=ax_img.transAxes,
                    ha='center', va='top',
                    fontsize=12, fontweight='bold'
                )

                ax_img.text(
                    0.5, -0.09, "Any student enrollment less than 10 has been redacted for student privacy and is graphed as 1.",
                    transform=ax_img.transAxes,
                    ha='center', va='top',
                    fontsize=10
                )

                continue

            ax_graph = axs_flat[2 * i + 1]
            ax_graph.plot(data_years, category_data['Total'], label='Total', marker='o')
            ax_graph.plot(data_years, category_data['Female'], label='Female', marker='o')
            ax_graph.plot(data_years, category_data['Male'], label='Male', marker='o')
            ax_graph.set_title(category_title + " Courses", fontweight='bold')
            ax_graph.set_xlabel('School Year')
            ax_graph.set_ylabel('Students')
            ax_graph.set_ylim(bottom=0)
            ax_graph.yaxis.set_major_locator(MaxNLocator(integer=True))
            ax_graph.legend()
            ax_graph.grid()

            ax_table = axs_flat[2 * i]
            ax_table.axis('off')

            df = pd.DataFrame(category_data, index=data_years)

            table_data = [['Year', 'Total', 'Female', 'Male']]
            for x, year in enumerate(data_years):
                total = category_data['Total'][x]
                female = category_data['Female'][x]
                male = category_data['Male'][x]

                female_percentage = (female / total * 100) if total != 0 else 0
                male_percentage = (male / total * 100) if total != 0 else 0

                female_cell = f"n<10 \n" if female == 1 else f"{female:,} \n({female_percentage:.1f}%)"
                male_cell = f"n<10 \n" if male == 1 else f"{male:,} \n({male_percentage:.1f}%)"

                total = f"{total:,}"
                

                table_data.append([
                    year,
                    total,
                    female_cell,
                    male_cell
                ])


            ax_table.text(0.5, 0.96, institution + " Students Enrolled in \n" + category_title + " Courses", fontsize=12, fontweight='bold', ha='center', va='bottom', transform=ax_table.transAxes)
            table = ax_table.table(cellText=table_data, loc='center', cellLoc='center', colLabels=None, bbox=[0, 0, 1, 0.94])
            table.auto_set_font_size(False)
            table.set_fontsize(10)
            table.scale(1, 0.8)
            
            for (x, y), cell in table.get_celld().items():
                if x == 0:
                    cell.set_text_props(fontweight='bold')

        for j in range(2 * len(gender_data_all_categories), len(axs_flat)):
            axs_flat[j].axis('off')

        # plt.tight_layout(rect=[0.03, 0.03, 0.97, 0.95])
        fig.subplots_adjust(left=0.06, right=0.94, bottom=0.06, top=0.92, wspace=0.3, hspace=0.2)
        pdf.savefig(fig)
        plt.close(fig)

    def concurrentEnrollmentAddedValueCorrection(raw_value):
        return 1 if raw_value == 2 else raw_value