# Exploratory Analysis of TANGEDCO Electricity Demand

## Project Information

**Project Title:** Exploratory Analysis of TANGEDCO Electricity Demand  
**Industry Name:** Electricity / Power and Energy Sector  
**Study Period:** 01 January 2021 to 28 April 2024  
**Project Type:** Python Exploratory Data Analysis (EDA)

---

## Problem Statement

Electricity demand in Tamil Nadu varies over time and can be examined using peak electricity load, energy supplied, unmet demand and weather conditions. The project focuses on analyzing daily Tamil Nadu electricity data together with weather data to understand demand patterns, high-demand periods, time-based variations and relationships between electricity-demand indicators and weather variables.

The analysis uses the available data for the selected study period and documents the observed unmet-demand pattern in the dataset without changing the recorded values.

---

## Proposed Solution / Analysis Questions

The project uses Python-based exploratory data analysis to clean, transform, merge and analyze Tamil Nadu electricity and weather datasets.

The analysis focuses on the following questions:

- How does daily peak electricity load change over the study period?
- How does daily energy supplied change over the study period?
- How does peak electricity load vary across years, months and days of the week?
- Which days recorded the highest peak electricity load?
- What is the distribution of peak electricity load and energy supplied?
- What relationships can be observed between peak electricity load and weather variables such as temperature, solar radiation and UTCI?
- What relationships can be observed between peak electricity load and daily energy supplied?
- What does the selected Tamil Nadu unmet-demand data show during the study period?
- What outliers are identified using the IQR method?

The notebook is designed as an exploratory analysis project. It focuses on cleaning, summarization, transformation, visualization, interpretation and discovery of patterns rather than building a machine-learning model.

---

## Dataset Name

**Daily electricity demand data for Indian states (2014–2024)**, with Tamil Nadu weather data used for the weather-demand analysis.

## Dataset Source

**Zenodo:** https://zenodo.org/records/14983362  
**DOI:** 10.5281/zenodo.14983362

The electricity datasets are state-wise data scraped from India's national grid. The project selects the Tamil Nadu records from the state-wise electricity datasets after cleaning. The weather dataset contains daily Tamil Nadu weather variables used to study relationships between weather conditions and electricity-demand indicators.

> **Source note:** The electricity data are used in the Tamil Nadu/TANGEDCO project context. They should not be described as directly published by TANGEDCO.

---
 ### Datasets Used

| Dataset | Purpose |
|---|---|
| `peak_met_MW.csv` | Daily peak power supplied by state |
| `peak_unmet_MW.csv` | Daily peak unmet demand by state |
| `corrected_daily_energy_met_MU.csv` | Daily energy supplied by state |
| `Tamil_Nadu_21_24.csv` | Daily Tamil Nadu weather data |

### Main Variables

**Electricity variables**

- `Peak_Load_MW` – Daily peak electricity load.
- `Unmet_Demand_MW` – Daily peak unmet demand.
- `Energy_Supplied_MU` – Daily energy supplied.

**Weather variables**

The weather dataset includes available daily measurements for temperature, wind, dew point, surface solar radiation, total cloud cover, and Universal Thermal Climate Index (UTCI).

## Tools and Technologies

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Seaborn

## Project Workflow

**Industry Selection → Problem Identification → Dataset Collection → Data Cleaning → Data Transformation → Data Analysis → Data Visualization → Insights → Recommendations**

### Workflow Description

1. **Industry Selection:** Electricity, power, and energy sector.
2. **Problem Identification:** Examine Tamil Nadu electricity demand patterns using electricity and weather data.
3. **Dataset Collection:** Use three state-wise electricity datasets and one Tamil Nadu weather dataset.
4. **Data Cleaning:** Inspect dataset structures, handle dates and numeric fields, and prepare the datasets for analysis.
5. **Data Transformation:** Select Tamil Nadu electricity records, prepare date-based features, and merge electricity data with weather data.
6. **Data Analysis:** Perform trend, distribution, comparison, time-based, correlation, relationship, high-demand, and outlier analyses.
7. **Data Visualization:** Create charts using Matplotlib and Seaborn.
8. **Insights:** Interpret patterns and observations from the actual analysis.
9. **Recommendations:** Provide practical suggestions based on the observed findings and limitations.

## Data Cleaning and Transformation

The project cleans each raw dataset independently before merging.

The process includes:

- Loading and inspecting the raw CSV files.
- Checking dataset structure, columns, data types, and missing values.
- Preparing date fields for analysis.
- Converting relevant analytical fields into suitable numeric formats.
- Handling invalid or unusable records where required by the cleaning process.
- Saving the cleaned datasets.
- Selecting Tamil Nadu electricity records.
- Merging the electricity data with Tamil Nadu weather data.
- Saving the merged dataset for feature engineering and exploratory analysis.

### Feature Engineering

Date-based features are prepared to support:

- Year-wise analysis.
- Month-wise analysis.
- Quarter-wise analysis.
- Day-of-week analysis.
- Year-month analysis.

Temperature is also converted from Kelvin to Celsius for the relevant analysis.

## Data Analysis and Visualization

The following analyses and visualizations are included in the project.

### 1. Trend Analysis

Examines changes in electricity-demand indicators across the study period.

- Daily energy supplied trend.
- Daily peak load trend.
- Daily unmet demand trend.

### 2. Category-wise Analysis

Compares average peak electricity load across days of the week.

- Day-of-week analysis.

### 3. Comparison Analysis

Compares electricity-demand indicators across years and identifies high-demand days.

- Year-wise energy comparison.
- Year-wise peak load comparison.

### 4. Correlation Analysis

Examines associations among selected electricity and weather variables.

- Correlation matrix for electricity and weather variables.

The unmet-demand variable is excluded from the correlation matrix because it has no variation in the selected records.

### 5. Distribution Analysis

Examines the distribution of electricity-demand variables and high-demand observations.

- Peak electricity load distribution.
- Boxplots for the main electricity variables.
- Top peak-load days.

### 6. Relationship Analysis

Examines relationships between peak electricity load and selected weather or electricity variables.

- UTCI versus peak load.
- Maximum temperature versus peak load.
- Peak load versus energy supplied.
- Solar radiation versus peak load.
- Temperature versus peak load.

### 7. Time-based Analysis

Examines monthly and year-month variations in electricity-demand indicators.

- Monthly energy supplied analysis.
- Monthly peak load analysis.
- Year-month heatmap of peak load.

### 8. Outlier Analysis

Uses the Interquartile Range (IQR) method to identify unusual observations in selected variables, including peak load, unmet demand, energy supplied, and mean temperature in Celsius.

Outliers are identified for further examination and are not automatically removed.

## Key Insights

The following observations are based on the project's analysis:

- Peak electricity load and energy supplied show daily, yearly, monthly, and day-of-week variations in the selected data.
- The top 15 peak-load days are identified for closer examination of high-demand periods.
- The selected Tamil Nadu `Unmet_Demand_MW` values are recorded as zero throughout the study period.
- Relationships between electricity-demand indicators and weather variables are examined using visualizations and correlation analysis.
- The IQR method is used to identify observations outside the calculated bounds for selected variables.
- The 2024 data cover only the period available through 28 April 2024, so 2024 is a partial year.

## Recommendations

Based on the observed patterns and the scope of this analysis:

- Use the identified high peak-load days as focus periods for further demand monitoring and investigation.
- Consider observed weather-demand relationships as exploratory evidence rather than proof of causation.
- Preserve and document the recorded zero unmet-demand values instead of modifying them to create variation.
- Interpret 2024 results as a partial-year analysis.
- Investigate IQR-identified unusual observations before deciding whether any data-quality action is necessary.

## Visualization Screenshots

The following screenshots are stored in the repository's `visualisation/` folder. The relative paths below match the provided folder structure.

### Trend Analysis

**Daily Energy Supplied Trend**

![Daily Energy Supplied Trend](visualisation/Trend%20analysis/daily%20energy%20supplied%20trend.png)

**Daily Peak Load Trend**

![Daily Peak Load Trend](visualisation/Trend%20analysis/daily%20peak%20load%20trend.png)

**Daily Unmet Demand Trend**

![Daily Unmet Demand Trend](visualisation/Trend%20analysis/daily%20unmet%20trend.png)

### Category-wise Analysis

**Day-of-Week Analysis**

![Day of Week Analysis](visualisation/Category-wise%20analysis/day%20of%20week%20analysis.png)

### Comparison Analysis

**Year-wise Energy Comparison**

![Year Wise Energy Comparison](visualisation/Comparsion%20anlaysis/Year%20wise%20energy%20comparision.png)

**Year-wise Peak Load Comparison**

![Year Wise Peak Load Comparison](visualisation/Comparsion%20anlaysis/Year%20wise%20peak%20load%20comparision.png)

### Correlation Analysis

**Electricity and Weather Variables**

![Electricity and Weather Variables](visualisation/Correlation%20analysis/electricity%20and%20weather%20variables.png)

### Distribution Analysis

**Peak Electricity Load Distribution**

![Peak Electricity Load Distribution](visualisation/Distribution%20analysis/Peak%20Electricity%20Load%20Distribution.png)

**Boxplots for Main Electricity Variables**

![Boxplots for Main Electricity Variables](visualisation/Distribution%20analysis/boxplots%20for%20main%20electricity%20variables.png)

**Top Peak Load Days**

![Top Peak Load Days](visualisation/Distribution%20analysis/top%20peak%20load%20days.png)

### Outlier Analysis

**Temperature and Peak Load Seasonal Comparison**

![Temperature and Peak Load Seasonal Comparison](visualisation/Outlier%20analysis/temperature%20and%20peak%20load%20seasonal%20comparision.png)

### Relationship Analysis

**UTCI vs Peak Load**

![UTCI vs Peak Load](visualisation/Relationship%20analysis/UTCI%20vs%20peak%20load.png)

**Maximum Temperature vs Peak Load**

![Maximum Temperature vs Peak Load](visualisation/Relationship%20analysis/max%20temp%20vs%20peak%20load.png)

**Peak Load vs Energy Supplied**

![Peak Load vs Energy Supplied](visualisation/Relationship%20analysis/peak%20load%20vs%20energy%20supplied.png)

**Solar Radiation vs Peak Load**

![Solar Radiation vs Peak Load](visualisation/Relationship%20analysis/solar%20radiation%20vs%20peak%20load.png)

**Temperature vs Peak Load**

![Temperature vs Peak Load](visualisation/Relationship%20analysis/temperature%20vs%20peak%20load.png)

### Time-based Analysis

**Monthly Energy Supplied Analysis**

![Monthly Energy Supplied Analysis](visualisation/Time%20analysis/monthly%20energy%20supplied%20analysis.png)

**Monthly Peak Load Analysis**

![Monthly Peak Load Analysis](visualisation/Time%20analysis/monthly%20peak%20load%20analysis.png)

**Year-Month Heatmap of Peak Load**

![Year Month Heatmap of Peak Load](visualisation/Time%20analysis/year%20month%20heatmap%20of%20peak%20load.png)

## Project Documentation

The project presentation PDF is available in the `documentation/` folder.

[**View the Project Presentation (PDF)**](documentation/Exploratory_Analysis_of_TANGEDCO_Electricity_Demand_Presentation.pdf)

## Project Folder Structure

```text
Exploratory_Analysis_of_TANGEDCO_Electricity_Demand/
│
├── README.md
│
├── Python/
│   ├── data_cleaning.py
│   ├── data_loading.py
│   ├── data_visualization.py
│   └── exploratory_analysis.py
│
├── dataset/
│   ├── raw data/
│   │   ├── Tamil_Nadu_21_24.csv
│   │   ├── corrected_daily_energy_met_MU.csv
│   │   ├── peak_met_MW.csv
│   │   └── peak_unmet_MW.csv
│   │
│   ├── clean data/
│   │   ├── clean_daily_energy_met_MU.csv
│   │   ├── clean_peak_met_MW.csv
│   │   ├── clean_peak_unmet_MW.csv
│   │   └── clean_tamil_nadu_21_24.csv
│   │
│   └── merged dataset/
│       └── Tamil_Nadu_TANGEDCO_Merged_2021_2024.csv
│
├── documentation/
│   └── Exploratory_Analysis_of_TANGEDCO_Electricity_Demand_Presentation.pdf
│
├── notebook/
│   └── Exploratory data analysis.ipynb
│
└── visualisation/
    ├── Category-wise analysis/
    │   └── day of week analysis.png
    │
    ├── Comparsion anlaysis/
    │   ├── Year wise energy comparision.png
    │   └── Year wise peak load comparision.png
    │
    ├── Correlation analysis/
    │   └── electricity and weather variables.png
    │
    ├── Distribution analysis/
    │   ├── Peak Electricity Load Distribution.png
    │   ├── boxplots for main electricity variables.png
    │   └── top peak load days.png
    │
    ├── Outlier analysis/
    │   └── temperature and peak load seasonal comparision.png
    │
    ├── Relationship analysis/
    │   ├── UTCI vs peak load.png
    │   ├── max temp vs peak load.png
    │   ├── peak load vs energy supplied.png
    │   ├── solar radiation vs peak load.png
    │   └── temperature vs peak load.png
    │
    ├── Time analysis/
    │   ├── monthly energy supplied analysis.png
    │   ├── monthly peak load analysis.png
    │   └── year month heatmap of peak load.png
    │
    └── Trend analysis/
        ├── daily energy supplied trend.png
        ├── daily peak load trend.png
        └── daily unmet trend.png
```

## Reproducibility

The project is organized around Python scripts, a Jupyter Notebook, raw and cleaned datasets, a merged dataset, and saved visualization screenshots.

The analysis workflow is:

1. Load the raw datasets.
2. Inspect and clean the source datasets independently.
3. Save the cleaned CSV files.
4. Select the Tamil Nadu electricity records.
5. Merge electricity data with Tamil Nadu weather data.
6. Save the merged dataset.
7. Prepare analytical features.
8. Perform exploratory data analysis.
9. Generate and review visualizations.
10. Interpret the observed patterns and document findings.

## Project Scope and Limitations

- This is an exploratory data analysis project, not a predictive machine-learning model.
- The selected study period is 1 January 2021 to 28 April 2024.
- The year 2024 is only partially represented.
- The analysis depends on the selected source datasets and their recorded values.
- The selected unmet-demand data contain no variation, limiting their usefulness in correlation and relationship analysis.
- Observed relationships between electricity and weather variables do not establish causation.

## Dataset Citation

Hunt, K., & Bloomfield, H. (2025). *Daily electricity demand data for Indian states (2014–2024).* Zenodo. https://doi.org/10.5281/zenodo.14983362

## Author

- **Name:** NEHA SHRUTHI U
- **Student ID:** AF05308253
- **Organization:** Anudip Foundation
- **Course:** AIML
- **Batch Code:** ANP-D7444

---

*This project demonstrates the use of Python libraries for data cleaning, transformation, exploratory analysis, statistical examination, and visualization of electricity-demand and weather data.*


The final analysis is supported by tables and visualizations created using Pandas, NumPy, Matplotlib and Seaborn, with interpretations based on the actual data available for the study period
