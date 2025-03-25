import pandas as pd

xls = pd.ExcelFile('./assets/IPEDS/IPEDS.xlsx')

all_sheets = xls.sheet_names
# sheets_data_frames = [pd.read_excel(xls, sheet_name=sheet, header=[0]) for sheet in all_sheets]

excluded_unitid = []
final_data = []

for sheet in all_sheets:
    data_frame = pd.read_excel(xls, sheet_name=sheet, header=[0])
    ctotal = {}
    
    for i in range(len(data_frame)):

        unitid = data_frame['UNITID'].iloc[i]
        if unitid in excluded_unitid:
            continue

        awlevel = data_frame['AWLEVEL'].iloc[i]
        ctotalw = data_frame['CTOTALW'].iloc[i]
        ctotalm = data_frame['CTOTALM'].iloc[i]
        ctotalt = data_frame['CTOTALT'].iloc[i]
        
        if awlevel not in ctotal:
            ctotal[awlevel] = {
                'CTOTALW': 0,
                'CTOTALM': 0,
                'CTOTALT': 0
            }
        
        ctotal[awlevel]['CTOTALW'] += ctotalw
        ctotal[awlevel]['CTOTALM'] += ctotalm
        ctotal[awlevel]['CTOTALT'] += ctotalt
    
    year_data = []

    for awlevel, values in ctotal.items():
        year_data.append({
            'Year': sheet,
            'AWLEVEL': awlevel,
            'CTOTALW': values['CTOTALW'],
            'CTOTALM': values['CTOTALM'],
            'CTOTALT': values['CTOTALT']
        })
    
    final_data.extend(year_data)
    
    total_row = {
        'Year': sheet,
        'AWLEVEL': 'Total',
        'CTOTALW': sum(values['CTOTALW'] for values in ctotal.values()),
        'CTOTALM': sum(values['CTOTALM'] for values in ctotal.values()),
        'CTOTALT': sum(values['CTOTALT'] for values in ctotal.values())
    }
    
    final_data.append(total_row)

    

final_df = pd.DataFrame(final_data)
# final_df.sort_values(by=['Year', 'AWLEVEL'], ascending=[True, True], inplace=True)
final_df.to_excel('./IPEDS_excel_extract/ctotal.xlsx', index=False)