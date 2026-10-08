"""
exploratory_analysis.py
Creates the merged Tamil Nadu analytical dataset, feature-engineers it,
and performs the tabular/statistical EDA sections from the project notebook.

Project: Exploratory Analysis of TANGEDCO Electricity Demand
Study period: 01 January 2021 to 28 April 2024
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
sns.set_theme(style="whitegrid")
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1200)
pd.set_option("display.max_rows", 100)

weather_file = "../dataset/raw Data/Tamil_Nadu_21_24.csv"
peak_file = "../dataset/raw Data/peak_met_MW.csv"
unmet_file = "../dataset/raw Data/peak_unmet_MW.csv"
energy_file = "../dataset/raw Data/corrected_daily_energy_met_MU.csv"

start_date = "2021-01-01"
end_date = "2024-04-28"

df_weather = pd.read_csv(weather_file)
df_peak = pd.read_csv(peak_file)
df_unmet = pd.read_csv(unmet_file)
df_energy = pd.read_csv(energy_file)

print("Weather shape:", df_weather.shape)
print("Peak-load shape:", df_peak.shape)
print("Unmet-demand shape:", df_unmet.shape)
print("Energy-supplied shape:", df_energy.shape)

print("WEATHER DATA")
display(df_weather.head())
print("\nPEAK LOAD DATA")
display(df_peak.head())
print("\nUNMET DEMAND DATA")
display(df_unmet.head())
print("\nENERGY SUPPLIED DATA")
display(df_energy.head())

print("Column names")
print("\nWeather:", df_weather.columns.tolist())
print("\nPeak:", df_peak.columns.tolist())
print("\nUnmet:", df_unmet.columns.tolist())
print("\nEnergy:", df_energy.columns.tolist())

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

df_peak.to_csv("clean_peak_met_MW.csv", index=False)
print("Saved cleaned dataset: clean_peak_met_MW.csv")

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

df_unmet.to_csv("clean_peak_unmet_MW.csv", index=False)
print("Saved cleaned dataset: clean_peak_unmet_MW.csv")

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

df_energy.to_csv("clean_daily_energy_met_MU.csv", index=False)
print("Saved cleaned dataset: clean_daily_energy_met_MU.csv")

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

df_weather.to_csv("clean_tamil_nadu_21_24.csv", index=False)
print("Saved cleaned dataset: clean_tamil_nadu_21_24.csv")

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

merged_df = df_tn_peak.merge(df_tn_unmet, on="Date", how="inner")
merged_df = merged_df.merge(df_tn_energy, on="Date", how="inner")
merged_df = merged_df.merge(df_weather, on="Date", how="inner")

merged_df = merged_df.sort_values("Date").reset_index(drop=True)

print("Merged dataset shape:", merged_df.shape)
print("Date range:", merged_df["Date"].min(), "to", merged_df["Date"].max())
display(merged_df.head())

merged_output_file = "Tamil_Nadu_TANGEDCO_Merged_2021_2024.csv"
merged_df.to_csv(merged_output_file, index=False)
print(f"Merged dataset saved successfully as: {merged_output_file}")

merged_df["Year"] = merged_df["Date"].dt.year
merged_df["Month"] = merged_df["Date"].dt.month
merged_df["Month_Name"] = merged_df["Date"].dt.month_name()
merged_df["Quarter"] = merged_df["Date"].dt.quarter
merged_df["Day"] = merged_df["Date"].dt.day
merged_df["Day_of_Week"] = merged_df["Date"].dt.day_name()
merged_df["Day_of_Year"] = merged_df["Date"].dt.dayofyear

for col in ["2m_temperature_min", "2m_temperature_mean", "2m_temperature_max"]:
    if col in merged_df.columns:
        merged_df[col.replace("2m_temperature", "Temperature_C")] = merged_df[col] - 273.15

merged_df["Unmet_Demand_Ratio_Pct"] = np.where(
    merged_df["Peak_Load_MW"] > 0,
    (merged_df["Unmet_Demand_MW"] / merged_df["Peak_Load_MW"]) * 100,
    np.nan
)

merged_df["Energy_Per_Peak_MW"] = np.where(
    merged_df["Peak_Load_MW"] > 0,
    merged_df["Energy_Supplied_MU"] / merged_df["Peak_Load_MW"],
    np.nan
)

merged_df["Unmet_Demand_Ratio_Pct"] = merged_df["Unmet_Demand_Ratio_Pct"].round(2)
merged_df["Energy_Per_Peak_MW"] = merged_df["Energy_Per_Peak_MW"].round(4)

display(merged_df.head())

analysis_columns = [
    "Peak_Load_MW",
    "Unmet_Demand_MW",
    "Energy_Supplied_MU",
    "2m_temperature_mean",
    "2m_dewpoint_temperature_mean",
    "surface_solar_radiation_downwards_mean",
    "total_cloud_cover_mean",
    "utci_mean",
    "Unmet_Demand_Ratio_Pct"
]
analysis_columns = [c for c in analysis_columns if c in merged_df.columns]
display(merged_df[analysis_columns].describe().T.round(2))