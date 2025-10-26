import pandas as pd

# Load the Excel file
df = pd.read_excel(
    "./assets/excel_sheet.xlsx",
    sheet_name="School-Level Data SY 2019-2020",
    skiprows=1
)

# List of demographic suffixes with exact names
demographic_suffixes = [
    "American Indian or Alaska Native",
    "Asian",
    "Black or African American",
    "Hispanic or Latino",
    "Native Hawaiian or Pacific Islander",
    "Two or more races",
    "White",
    "504",
    "Disability",
    "Eco. Dis.",
    "Eng. Learners"
]

output_rows = []

def safe_num(val):
    if isinstance(val, str) and val.strip().lower().startswith("n<"):
        return 0
    try:
        num = pd.to_numeric(val, errors='coerce')
        if pd.isna(num):
            return 0
        return num
    except:
        return 0

def safe_sum(a, b):
    return safe_num(a) + safe_num(b)

def compute_totals(row_dict):
    # Total group core
    row_dict["Total_Courses"] = safe_sum(row_dict.get("Basic_Courses", ""), row_dict.get("Adv_Courses", ""))
    row_dict["Total"] = safe_sum(row_dict.get("Basic_Total", ""), row_dict.get("Adv_Total", ""))
    row_dict["Girl"] = safe_sum(row_dict.get("Basic_Girl", ""), row_dict.get("Adv_Girl", ""))
    row_dict["Boy"] = safe_sum(row_dict.get("Basic_Boy", ""), row_dict.get("Adv_Boy", ""))
    row_dict["GenderX"] = safe_sum(row_dict.get("Basic_GenderX", ""), row_dict.get("Adv_GenderX", ""))
    row_dict["GenderNP"] = safe_sum(row_dict.get("Basic_GenderNP", ""), row_dict.get("Adv_GenderNP", ""))

    # Demographic totals
    for suffix in demographic_suffixes:
        row_dict[f"Total_{suffix}"] = safe_sum(
            row_dict.get(f"Basic_{suffix}", ""), row_dict.get(f"Adv_{suffix}", "")
        )
    return row_dict

def extract_demographics(row, prefix):
    result = {}
    for suffix in demographic_suffixes:
        col_name = f"{prefix}: {suffix}"
        result[suffix] = row.get(col_name, "")
    return result

# Process each row
for _, row in df.iterrows():
    base = {
        "School Year": row["School Year"],
        "School Name": row["School Name"],
        "School Number (State)": row["School Number (State)"],
        "School Number (NCES)": row["School Number (NCES)"],
        "District Name": row["District Name"],
        "District Number (State)": row["District Number (State)"],
        "District Number (NCES)": row["District Number (NCES)"]
    }

    # Extract demographic values
    basic_demo = extract_demographics(row, "CSB")
    adv_demo = extract_demographics(row, "CSA")
    csr_demo = extract_demographics(row, "CSR")

    # Row 1: CoreCS_OLD
    corecs = {
        **base,
        "Category": "CoreCS_OLD",
        "Basic_Courses": row.get("CSB: Number of Courses Offered", ""),
        "Basic_Total": row.get("CSB: Total", ""),
        "Basic_Girl": row.get("CSB: Female", ""),
        "Basic_Boy": row.get("CSB: Male", ""),
        "Basic_GenderX": "",
        "Basic_GenderNP": "",
        "Adv_Courses": row.get("CSA: Number of Courses Offered", ""),
        "Adv_Total": row.get("CSA: Total", ""),
        "Adv_Girl": row.get("CSA: Female", ""),
        "Adv_Boy": row.get("CSA: Male", ""),
        "Adv_GenderX": "",
        "Adv_GenderNP": ""
    }

    for suffix, val in basic_demo.items():
        corecs[f"Basic_{suffix}"] = val
    for suffix, val in adv_demo.items():
        corecs[f"Adv_{suffix}"] = val

    corecs = compute_totals(corecs)

    # Row 2: CS-Related
    csrel = {
        **base,
        "Category": "CS-Related",
        "Total_Courses": row.get("CSR: Number of Courses Offered", ""),
        "Total": row.get("CSR: Total", ""),
        "Girl": row.get("CSR: Female", ""),
        "Boy": row.get("CSR: Male", ""),
        "GenderX": "",
        "GenderNP": "",
        "Basic_Courses": "",
        "Basic_Total": "",
        "Basic_Girl": "",
        "Basic_Boy": "",
        "Basic_GenderX": "",
        "Basic_GenderNP": "",
        "Adv_Courses": "",
        "Adv_Total": "",
        "Adv_Girl": "",
        "Adv_Boy": "",
        "Adv_GenderX": "",
        "Adv_GenderNP": ""
    }

    for suffix, val in csr_demo.items():
        csrel[f"Total_{suffix}"] = val

    # Row 3: Total
    total = {
        **base,
        "Category": "CS Total"
    }

    numeric_fields = [
        "Total_Courses", "Total", "Girl", "Boy", "GenderX", "GenderNP",
        "Basic_Courses", "Basic_Total", "Basic_Girl", "Basic_Boy", "Basic_GenderX", "Basic_GenderNP",
        "Adv_Courses", "Adv_Total", "Adv_Girl", "Adv_Boy", "Adv_GenderX", "Adv_GenderNP"
    ]
    for suffix in demographic_suffixes:
        numeric_fields.extend([
            f"Basic_{suffix}", f"Adv_{suffix}", f"Total_{suffix}"
        ])

    for field in numeric_fields:
        v1 = safe_num(corecs.get(field, ""))
        v2 = safe_num(csrel.get(field, ""))
        total[field] = v1 + v2

    output_rows.extend([corecs, csrel, total])

# Create the final DataFrame
final_df = pd.DataFrame(output_rows)

# Define column order
ordered_cols = [
    "School Year", "School Name", "School Number (State)",
    "School Number (NCES)", "District Name", "District Number (State)",
    "District Number (NCES)", "Category",

    # Total group
    "Total_Courses", "Total", "Girl", "Boy", "GenderX", "GenderNP"
]
for suffix in demographic_suffixes:
    ordered_cols.append(f"Total_{suffix}")

# Basic group
ordered_cols += [
    "Basic_Courses", "Basic_Total", "Basic_Girl", "Basic_Boy", "Basic_GenderX", "Basic_GenderNP"
]
for suffix in demographic_suffixes:
    ordered_cols.append(f"Basic_{suffix}")

# Adv group
ordered_cols += [
    "Adv_Courses", "Adv_Total", "Adv_Girl", "Adv_Boy", "Adv_GenderX", "Adv_GenderNP"
]
for suffix in demographic_suffixes:
    ordered_cols.append(f"Adv_{suffix}")

# Reorder columns and export to Excel
final_df = final_df[ordered_cols]
final_df.to_excel("reshaped_output.xlsx", index=False)
