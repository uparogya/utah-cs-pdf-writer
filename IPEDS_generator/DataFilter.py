import pandas as pd

df = pd.read_csv("NAME_OF_CSV_FILE.csv", dtype=str)

df["CIPCODE"] = pd.to_numeric(df["CIPCODE"], errors="coerce")

valid_unitids = {
    "230010", "447421", "230038", "448220", "230065", "448239", "230144", "448248",
    "230162", "449816", "230171", "451574", "230199", "451583", "230205", "455381",
    "230214", "456454", "230366", "458104", "230418", "459541", "230490", "461272",
    "230597", "461342", "230603", "461494", "230676", "461926", "230728", "474924",
    "230737", "475495", "230746", "475723", "230764", "476708", "230782", "476993",
    "230807", "480985", "380438", "481100", "406486", "481456", "421610", "484394",
    "433387", "489247", "441830", "494649", "444787", "495101", "444857", "495411",
    "445692", "497268", "447263", "499307"
}

filtered_df = df[(df["CIPCODE"].between(11, 12)) & (df["UNITID"].isin(valid_unitids))]

filtered_df.to_csv("../IPEDS_excel_extract/filtered_data.csv", index=False)
print(f"Filtering complete. {len(filtered_df)} rows saved to 'filtered_data.csv'.")
