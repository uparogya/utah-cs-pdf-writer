import pandas as pd
import InstitutionList

xls = pd.ExcelFile('./assets/IPEDS/IPEDS.xlsx')

all_sheets = xls.sheet_names
excluded_unitid = [433387]
final_data = []
unitid_totals = {}

for sheet in all_sheets:
    data_frame = pd.read_excel(xls, sheet_name=sheet, header=[0])
    unitid_data = data_frame[~data_frame['UNITID'].isin(excluded_unitid)]
    unitid_data = unitid_data.groupby(['UNITID', 'AWLEVEL'], as_index=False)[['CTOTALW', 'CTOTALM', 'CTOTALT']].sum()
    unitid_totals[sheet] = unitid_data

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
            ctotal[awlevel] = {'CTOTALW': 0, 'CTOTALM': 0, 'CTOTALT': 0}
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

base_columns = ['Year', 'AWLEVEL', 'CTOTALW', 'CTOTALM', 'CTOTALT']
final_df = pd.DataFrame(final_data, columns=base_columns)

institution_columns = []
institution_map = {}

for sheet, unitid_data in unitid_totals.items():
    for _, row in unitid_data.iterrows():
        unitid = row['UNITID']
        inst_name = InstitutionList.InstitutionList[unitid]["name"]
        awlevel = row['AWLEVEL']
        mask = (final_df['Year'] == sheet) & (final_df['AWLEVEL'] == awlevel)
        row_idx = final_df.index[mask]
        if row_idx.empty:
            continue
        for metric in ['CTOTALW', 'CTOTALM', 'CTOTALT']:
            col_name = f'{inst_name}_{metric}'
            if col_name not in final_df.columns:
                final_df[col_name] = ''
            final_df.loc[row_idx[0], col_name] = row[metric]
            institution_map.setdefault(inst_name, []).append(col_name)

institution_columns = []
for inst_name in sorted(institution_map):
    institution_columns.extend([
        f'{inst_name}_CTOTALW',
        f'{inst_name}_CTOTALM',
        f'{inst_name}_CTOTALT'
    ])
final_df = final_df[base_columns + institution_columns]

subheader_1 = base_columns.copy()
subheader_2 = [''] * len(base_columns)

for inst_name in sorted(institution_map):
    subheader_1.extend([inst_name] * 3)
    subheader_2.extend(['CTOTALW', 'CTOTALM', 'CTOTALT'])

subheaders = pd.DataFrame([subheader_1, subheader_2], columns=final_df.columns)
final_df_with_subheaders = pd.concat([subheaders, final_df], ignore_index=True)

final_df_with_subheaders.to_excel('./IPEDS_excel_extract/ctotal.xlsx', index=False, header=False)