"""
data_visualization.py
Contains the standalone visualizations from the TANGEDCO EDA notebook.

The visualizations are grouped as:
1. Distribution Analysis
2. Trend Analysis
3. Comparison Analysis
4. Time-based Analysis
5. Category-wise Analysis
6. Relationship Analysis
7. Correlation Analysis
8. High-Demand Analysis
9. Outlier Analysis
10. Seasonal Comparison
"""
"""Feature Engineering and Data Visualization for TANGEDCO Electricity Demand Analysis"""
merged_df["Year"] = merged_df["Date"].dt.year
merged_df["Month"] = merged_df["Date"].dt.month
merged_df["Month_Name"] = merged_df["Date"].dt.month_name()
merged_df["Quarter"] = merged_df["Date"].dt.quarter
merged_df["Day"] = merged_df["Date"].dt.day
merged_df["Day_of_Week"] = merged_df["Date"].dt.day_name()
merged_df["Day_of_Year"] = merged_df["Date"].dt.dayofyear

# Convert temperature variables from Kelvin to Celsius for easier interpretation.
for col in ["2m_temperature_min", "2m_temperature_mean", "2m_temperature_max"]:
    if col in merged_df.columns:
        merged_df[col.replace("2m_temperature", "Temperature_C")] = merged_df[col] - 273.15

# Useful demand-related indicators.
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

#Descriptive statistics for the merged dataset

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


"""EDA Visualizations"""

# peak electricity load distribution
plt.figure(figsize=(10, 6))
plt.hist(merged_df["Peak_Load_MW"].dropna(), bins=30)
plt.title("Distribution of Daily Peak Electricity Load in Tamil Nadu")
plt.xlabel("Peak Load (MW)")
plt.ylabel("Number of Days")
plt.tight_layout()
plt.show()

# TREND ANALYSIS
# daily peak load trend
plt.figure(figsize=(14, 6))
plt.plot(merged_df["Date"], merged_df["Peak_Load_MW"], linewidth=1.5)
plt.title("Daily Peak Electricity Load in Tamil Nadu (2021–2024)")
plt.xlabel("Date")
plt.ylabel("Peak Load (MW)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# daily energy supplied trend
plt.figure(figsize=(14, 6))
plt.plot(merged_df["Date"], merged_df["Energy_Supplied_MU"], linewidth=1.5)
plt.title("Daily Energy Supplied in Tamil Nadu (2021–2024)")
plt.xlabel("Date")
plt.ylabel("Energy Supplied (MU)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# daily unmet demand trend
plt.figure(figsize=(14, 6))
plt.plot(merged_df["Date"], merged_df["Unmet_Demand_MW"], linewidth=1.5)
plt.title("Daily Peak Unmet Demand in Tamil Nadu (2021–2024)")
plt.xlabel("Date")
plt.ylabel("Unmet Demand (MW)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# COMPARISON ANALYSIS
# Year-wise peak load comparison
year_peak = merged_df.groupby("Year")["Peak_Load_MW"].mean().reset_index()

plt.figure(figsize=(9, 5))
plt.bar(year_peak["Year"].astype(str), year_peak["Peak_Load_MW"])
plt.title("Average Daily Peak Load by Year")
plt.xlabel("Year")
plt.ylabel("Average Peak Load (MW)")
plt.tight_layout()
plt.show()

display(year_peak.round(2))

# year-wise energy supplied comparison
yearly_energy = (
    merged_df.groupby("Year", observed=True)["Energy_Supplied_MU"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(9, 6))
sns.barplot(data=yearly_energy, x="Year", y="Energy_Supplied_MU", errorbar=None)
plt.title("Average Energy Supplied by Year")
plt.xlabel("Year")
plt.ylabel("Average Energy Supplied (MU)")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# TIME-BASED ANALYSIS
# Montly load peak analysis
month_order = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

monthly_peak = (
    merged_df.groupby("Month_Name", observed=True)["Peak_Load_MW"]
    .mean()
    .reindex(month_order)
    .reset_index()
)

plt.figure(figsize=(12, 6))
plt.bar(monthly_peak["Month_Name"], monthly_peak["Peak_Load_MW"])
plt.title("Average Peak Load by Month")
plt.xlabel("Month")
plt.ylabel("Average Peak Load (MW)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

display(monthly_peak.round(2))

# monthly energy supplied analysis
month_order = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

monthly_energy = (
    merged_df.groupby("Month_Name", observed=True)["Energy_Supplied_MU"]
    .mean()
    .reindex(month_order)
    .reset_index()
)

plt.figure(figsize=(11, 6))
sns.barplot(data=monthly_energy, x="Month_Name", y="Energy_Supplied_MU", errorbar=None)
plt.title("Average Energy Supplied by Month")
plt.xlabel("Month")
plt.ylabel("Average Energy Supplied (MU)")
plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# year-month heatmap for peak load
year_month_peak = merged_df.pivot_table(
    index="Year",
    columns="Month",
    values="Peak_Load_MW",
    aggfunc="mean"
)

plt.figure(figsize=(12, 5))
sns.heatmap(year_month_peak, annot=True, fmt=".0f", cmap="YlOrRd")
plt.title("Average Peak Load by Year and Month")
plt.xlabel("Month")
plt.ylabel("Year")
plt.tight_layout()
plt.show()

# Category-wise Analysis
# day of week peak load analysis
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_peak = (
    merged_df.groupby("Day_of_Week", observed=True)["Peak_Load_MW"]
    .mean()
    .reindex(day_order)
    .reset_index()
)

plt.figure(figsize=(10, 5))
plt.bar(day_peak["Day_of_Week"], day_peak["Peak_Load_MW"])
plt.title("Average Peak Load by Day of Week")
plt.xlabel("Day")
plt.ylabel("Average Peak Load (MW)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

display(day_peak.round(2))

# Relationship Analysis
# Temperature vs Peak Load
plt.figure(figsize=(9, 6))
sns.scatterplot(data=merged_df, x="Temperature_C_mean", y="Peak_Load_MW", alpha=0.6)
plt.title("Mean Temperature vs Daily Peak Electricity Load")
plt.xlabel("Mean Temperature (°C)")
plt.ylabel("Peak Load (MW)")
plt.tight_layout()
plt.show()

# Maximum Temperature vs Peak Load
plt.figure(figsize=(9, 6))
sns.scatterplot(data=merged_df, x="Temperature_C_max", y="Peak_Load_MW", alpha=0.6)
plt.title("Maximum Temperature vs Daily Peak Electricity Load")
plt.xlabel("Maximum Temperature (°C)")
plt.ylabel("Peak Load (MW)")
plt.tight_layout()
plt.show()

# Solar Radiation vs Peak Load
plt.figure(figsize=(9, 6))
sns.scatterplot(
    data=merged_df,
    x="surface_solar_radiation_downwards_mean",
    y="Peak_Load_MW",
    alpha=0.6
)
plt.title("Mean Solar Radiation vs Daily Peak Load")
plt.xlabel("Mean Solar Radiation")
plt.ylabel("Peak Load (MW)")
plt.tight_layout()
plt.show()

# UTCI vs Peak Load
plt.figure(figsize=(9, 6))
sns.scatterplot(
    data=merged_df,
    x="surface_solar_radiation_downwards_mean",
    y="Peak_Load_MW",
    alpha=0.6
)
plt.title("Mean Solar Radiation vs Daily Peak Load")
plt.xlabel("Mean Solar Radiation")
plt.ylabel("Peak Load (MW)")
plt.tight_layout()
plt.show()

# peak load vs energy supplied
plt.figure(figsize=(9, 6))
sns.scatterplot(data=merged_df, x="Peak_Load_MW", y="Energy_Supplied_MU", alpha=0.6)
plt.title("Peak Load vs Daily Energy Supplied")
plt.xlabel("Peak Load (MW)")
plt.ylabel("Energy Supplied (MU)")
plt.tight_layout()
plt.show()


# Correlation Analysis
corr_columns = [
    "Peak_Load_MW",
    "Energy_Supplied_MU",
    "Temperature_C_mean",
    "Temperature_C_max",
    "Temperature_C_min",
    "2m_dewpoint_temperature_mean",
    "surface_solar_radiation_downwards_mean",
    "total_cloud_cover_mean",
    "utci_mean"
]

correlation_matrix = merged_df[corr_columns].corr()

plt.figure(figsize=(12, 9))
sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0,
    linewidths=0.5
)
plt.title("Correlation Matrix: Electricity and Weather Variables")
plt.tight_layout()
plt.show()


# Distribution analysis
top_peak_days = (
    merged_df[["Date", "Peak_Load_MW", "Unmet_Demand_MW", "Energy_Supplied_MU", "Temperature_C_mean"]]
    .sort_values("Peak_Load_MW", ascending=False)
    .head(15)
    .reset_index(drop=True)
)

print("Top 15 peak-load days")
display(top_peak_days.round(2))

# unmets top 15 days
top_unmet_days = (
    merged_df[["Date", "Unmet_Demand_MW", "Peak_Load_MW", "Energy_Supplied_MU", "Temperature_C_mean"]]
    .sort_values("Unmet_Demand_MW", ascending=False)
    .head(15)
    .reset_index(drop=True)
)

print("Top 15 unmet-demand days")
display(top_unmet_days.round(2))

# Top-peak load days visualization
plot_df = top_peak_days.sort_values("Peak_Load_MW", ascending=True)

plt.figure(figsize=(10, 7))
plt.barh(plot_df["Date"].astype(str), plot_df["Peak_Load_MW"])
plt.title("Top 15 Days by Peak Electricity Load")
plt.xlabel("Peak Load (MW)")
plt.ylabel("Date")
plt.tight_layout()
plt.show()


# monthly and yearly summary tables
monthly_summary = merged_df.groupby(["Year", "Month", "Month_Name"], observed=True).agg(
    Avg_Peak_Load_MW=("Peak_Load_MW", "mean"),
    Max_Peak_Load_MW=("Peak_Load_MW", "max"),
    Avg_Unmet_Demand_MW=("Unmet_Demand_MW", "mean"),
    Max_Unmet_Demand_MW=("Unmet_Demand_MW", "max"),
    Avg_Energy_Supplied_MU=("Energy_Supplied_MU", "mean"),
    Avg_Temperature_C=("Temperature_C_mean", "mean")
).reset_index()

display(monthly_summary.round(2).head(30))

yearly_summary = merged_df.groupby("Year").agg(
    Avg_Peak_Load_MW=("Peak_Load_MW", "mean"),
    Max_Peak_Load_MW=("Peak_Load_MW", "max"),
    Avg_Unmet_Demand_MW=("Unmet_Demand_MW", "mean"),
    Max_Unmet_Demand_MW=("Unmet_Demand_MW", "max"),
    Avg_Energy_Supplied_MU=("Energy_Supplied_MU", "mean"),
    Total_Energy_Supplied_MU=("Energy_Supplied_MU", "sum"),
    Avg_Temperature_C=("Temperature_C_mean", "mean")
).reset_index()

display(yearly_summary.round(2))


# Boxplot for main electricity demand variables
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.boxplot(y=merged_df["Peak_Load_MW"], ax=axes[0])
axes[0].set_title("Peak Load Distribution")
axes[0].set_ylabel("Peak Load (MW)")

sns.boxplot(y=merged_df["Energy_Supplied_MU"], ax=axes[1])
axes[1].set_title("Energy Supplied Distribution")
axes[1].set_ylabel("Energy Supplied (MU)")

plt.tight_layout()
plt.show()


# Outlier Analysis
def iqr_summary(data, column):
    q1 = data[column].quantile(0.25)
    q3 = data[column].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = data[(data[column] < lower) | (data[column] > upper)]
    return {
        "Variable": column,
        "Q1": q1,
        "Q3": q3,
        "IQR": iqr,
        "Lower_Bound": lower,
        "Upper_Bound": upper,
        "Outlier_Count": len(outliers)
    }

outlier_variables = ["Peak_Load_MW", "Unmet_Demand_MW", "Energy_Supplied_MU", "Temperature_C_mean"]
outlier_variables = [c for c in outlier_variables if c in merged_df.columns]

outlier_summary = pd.DataFrame([iqr_summary(merged_df, c) for c in outlier_variables])
display(outlier_summary.round(2))

# temperature vs peak load seasonal comparison
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.boxplot(y=merged_df["Peak_Load_MW"], ax=axes[0])
axes[0].set_title("Peak Load Distribution")
axes[0].set_ylabel("Peak Load (MW)")

sns.boxplot(y=merged_df["Energy_Supplied_MU"], ax=axes[1])
axes[1].set_title("Energy Supplied Distribution")
axes[1].set_ylabel("Energy Supplied (MU)")

plt.tight_layout()
plt.show()
