"""
data_loading.py
Loads the four raw datasets used in the TANGEDCO electricity-demand EDA project.

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

"""load the four raw datasets"""
weather_file = "../dataset/raw Data/Tamil_Nadu_21_24.csv"
peak_file = "../dataset/raw Data/peak_met_MW.csv"
unmet_file = "../dataset/raw Data/peak_unmet_MW.csv"
energy_file = "../dataset/raw Data/corrected_daily_energy_met_MU.csv"

start_date = "2021-01-01"
end_date = "2024-04-28"


"""Data Ingestion"""
df_weather = pd.read_csv(weather_file)
df_peak = pd.read_csv(peak_file)
df_unmet = pd.read_csv(unmet_file)
df_energy = pd.read_csv(energy_file)

print("Weather shape:", df_weather.shape)
print("Peak-load shape:", df_peak.shape)
print("Unmet-demand shape:", df_unmet.shape)
print("Energy-supplied shape:", df_energy.shape)


"""Intial Inspection of the datasets"""

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

