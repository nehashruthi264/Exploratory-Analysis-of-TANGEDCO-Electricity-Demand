"""
data_cleaning.py
Cleans the four raw datasets and creates the five project CSV outputs.

The cleaning logic follows the project notebook:
- Standardize the date column to Date.
- Convert Date to datetime.
- Restrict records to 2021-01-01 through 2024-04-28.
- Remove invalid dates and duplicate dates.
- Convert non-date columns to numeric values.
- Sort by Date.
- Save each cleaned dataset immediately.

"""
"""peak_met_MW.csv cleaning""" 
df_peak = df_peak.copy()
df_peak.rename(columns={"date": "Date", "DATE": "Date"}, inplace=True)
df_peak["Date"] = pd.to_datetime(df_peak["Date"], errors="coerce")

df_peak = df_peak[(df_peak["Date"] >= start_date) & (df_peak["Date"] <= end_date)].copy()
df_peak = df_peak.dropna(subset=["Date"]).drop_duplicates(subset=["Date"], keep="first")

for col in df_peak.columns:
    if col != "Date":
        df_peak[col] = pd.to_numeric(df_peak[col], errors="coerce")

df_peak = df_peak.sort_values("Date").reset_index(drop=True)

print("Cleaned peak-load shape:", df_peak.shape)
print("Duplicate dates:", df_peak["Date"].duplicated().sum())
print("Missing values:", df_peak.isna().sum().sum())
display(df_peak.head())

#save cleaned peak-load dataset
df_peak.to_csv("clean_peak_met_MW.csv", index=False)
print("Saved cleaned dataset: clean_peak_met_MW.csv")


"""peak_unmet_MW.csv cleaning"""
df_unmet = df_unmet.copy()
df_unmet.rename(columns={"date": "Date", "DATE": "Date"}, inplace=True)
df_unmet["Date"] = pd.to_datetime(df_unmet["Date"], errors="coerce")

df_unmet = df_unmet[(df_unmet["Date"] >= start_date) & (df_unmet["Date"] <= end_date)].copy()
df_unmet = df_unmet.dropna(subset=["Date"]).drop_duplicates(subset=["Date"], keep="first")

for col in df_unmet.columns:
    if col != "Date":
        df_unmet[col] = pd.to_numeric(df_unmet[col], errors="coerce")

df_unmet = df_unmet.sort_values("Date").reset_index(drop=True)

print("Cleaned unmet-demand shape:", df_unmet.shape)
print("Duplicate dates:", df_unmet["Date"].duplicated().sum())
print("Missing values:", df_unmet.isna().sum().sum())
display(df_unmet.head())

#save cleaned unmet-demand dataset
df_unmet.to_csv("clean_peak_unmet_MW.csv", index=False)
print("Saved cleaned dataset: clean_peak_unmet_MW.csv")



"""corrected_daily_energy_met_MU.csv cleaning"""
df_energy = df_energy.copy()
df_energy.rename(columns={"date": "Date", "DATE": "Date"}, inplace=True)
df_energy["Date"] = pd.to_datetime(df_energy["Date"], errors="coerce")

df_energy = df_energy[(df_energy["Date"] >= start_date) & (df_energy["Date"] <= end_date)].copy()
df_energy = df_energy.dropna(subset=["Date"]).drop_duplicates(subset=["Date"], keep="first")

for col in df_energy.columns:
    if col != "Date":
        df_energy[col] = pd.to_numeric(df_energy[col], errors="coerce")

df_energy = df_energy.sort_values("Date").reset_index(drop=True)

print("Cleaned energy-supplied shape:", df_energy.shape)
print("Duplicate dates:", df_energy["Date"].duplicated().sum())
print("Missing values:", df_energy.isna().sum().sum())
display(df_energy.head())

#save cleaned energy-supplied dataset
df_energy.to_csv("clean_daily_energy_met_MU.csv", index=False)
print("Saved cleaned dataset: clean_daily_energy_met_MU.csv")



"""Tamil_Nadu_21_24.csv cleaning"""
df_weather = df_weather.copy()
df_weather.rename(columns={"date": "Date", "DATE": "Date"}, inplace=True)
df_weather["Date"] = pd.to_datetime(df_weather["Date"], errors="coerce")

df_weather = df_weather[(df_weather["Date"] >= start_date) & (df_weather["Date"] <= end_date)].copy()
df_weather = df_weather.dropna(subset=["Date"]).drop_duplicates(subset=["Date"], keep="first")

for col in df_weather.columns:
    if col != "Date":
        df_weather[col] = pd.to_numeric(df_weather[col], errors="coerce")

df_weather = df_weather.sort_values("Date").reset_index(drop=True)

print("Cleaned weather shape:", df_weather.shape)
print("Duplicate dates:", df_weather["Date"].duplicated().sum())
print("Missing values:", df_weather.isna().sum().sum())
display(df_weather.head())

#save cleaned weather dataset
df_weather.to_csv("clean_tamil_nadu_weather.csv", index=False)
print("Saved cleaned dataset: clean_tamil_nadu_weather.csv")



"""cleaning summary"""
cleaning_summary = pd.DataFrame({
    "Dataset": [
        "Peak Load",
        "Peak Unmet Demand",
        "Daily Energy Supplied",
        "Tamil Nadu Weather"
    ],
    "Rows": [len(df_peak), len(df_unmet), len(df_energy), len(df_weather)],
    "Columns": [df_peak.shape[1], df_unmet.shape[1], df_energy.shape[1], df_weather.shape[1]],
    "Duplicate_Dates": [
        df_peak["Date"].duplicated().sum(),
        df_unmet["Date"].duplicated().sum(),
        df_energy["Date"].duplicated().sum(),
        df_weather["Date"].duplicated().sum()
    ],
    "Total_Missing_Values": [
        int(df_peak.isna().sum().sum()),
        int(df_unmet.isna().sum().sum()),
        int(df_energy.isna().sum().sum()),
        int(df_weather.isna().sum().sum())
    ]
})
display(cleaning_summary)


"""merge datasets"""

df_tn_peak = df_peak[["Date", "Tamil Nadu"]].copy()
df_tn_peak.rename(columns={"Tamil Nadu": "Peak_Load_MW"}, inplace=True)

df_tn_unmet = df_unmet[["Date", "Tamil Nadu"]].copy()
df_tn_unmet.rename(columns={"Tamil Nadu": "Unmet_Demand_MW"}, inplace=True)

df_tn_energy = df_energy[["Date", "Tamil Nadu"]].copy()
df_tn_energy.rename(columns={"Tamil Nadu": "Energy_Supplied_MU"}, inplace=True)

print("Tamil Nadu peak-load data:")
display(df_tn_peak.head())
print("Tamil Nadu unmet-demand data:")
display(df_tn_unmet.head())
print("Tamil Nadu energy-supplied data:")
display(df_tn_energy.head())


"""merge the three datasets on Date"""

merged_df = df_tn_peak.merge(df_tn_unmet, on="Date", how="inner")
merged_df = merged_df.merge(df_tn_energy, on="Date", how="inner")
merged_df = merged_df.merge(df_weather, on="Date", how="inner")

merged_df = merged_df.sort_values("Date").reset_index(drop=True)

print("Merged dataset shape:", merged_df.shape)
print("Date range:", merged_df["Date"].min(), "to", merged_df["Date"].max())
display(merged_df.head())


# Save the merged dataset immediately after the merge

merged_output_file = "Tamil_Nadu_TANGEDCO_Merged_2021_2024.csv"
merged_df.to_csv(merged_output_file, index=False)
print(f"Merged dataset saved successfully as: {merged_output_file}")
