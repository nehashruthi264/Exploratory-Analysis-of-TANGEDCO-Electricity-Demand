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

## Datasets Used

| Dataset | Main Content | Use in Project |
|---|---|---|
| `peak_met_MW.csv` | Daily peak power supplied by state | Tamil Nadu peak load |
| `peak_unmet_MW.csv` | Daily peak unmet demand by state | Tamil Nadu unmet demand |
| `corrected_daily_energy_met_MU.csv` | Daily energy supplied by state | Tamil Nadu energy supplied |
| `Tamil_Nadu_21_24.csv` | Daily Tamil Nadu weather variables | Weather and electricity-demand analysis |

### Main Variables Used

**Electricity variables**

- `Peak_Load_MW` – selected Tamil Nadu daily peak electricity load.
- `Unmet_Demand_MW` – selected Tamil Nadu daily peak unmet demand.
- `Energy_Supplied_MU` – selected Tamil Nadu daily energy supplied.

**Weather variables** include daily minimum, mean and maximum measures for temperature, wind components, dew point, surface solar radiation, total cloud cover and UTCI, as available in the Tamil Nadu weather dataset.

---

## Tools & Technologies

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Seaborn

---

## Project Workflow

**Industry Selection → Problem Identification → Dataset Collection → Data Cleaning → Data Transformation → Data Analysis → Data Visualization → Insights → Recommendations**

### Workflow Description

1. **Industry Selection**  
   The project is based on the Electricity / Power and Energy sector.

2. **Problem Identification**  
   The project focuses on understanding Tamil Nadu electricity demand conditions using peak load, energy supplied, unmet demand and weather data.

3. **Dataset Collection**  
   Four raw datasets are collected and used: three state-wise electricity datasets and one Tamil Nadu weather dataset.

4. **Data Cleaning**  
   Each dataset is inspected and cleaned independently before any merging is performed.

5. **Data Transformation**  
   Tamil Nadu electricity records are selected from the cleaned state-wise datasets. Date-based and analytical features are then prepared.

6. **Data Analysis**  
   Descriptive, distribution, trend, time-based, comparison, correlation, relationship, high-demand and outlier analyses are performed.

7. **Data Visualization**  
   Matplotlib and Seaborn are used to create charts for the major analyses.

8. **Insights**  
   Findings are interpreted from the actual tables, statistics and visualizations produced by the notebook.

9. **Recommendations**  
   Practical recommendations are based only on the observed patterns and limitations of the selected dataset.

---

## Data Cleaning

The notebook follows a separate cleaning process for each raw dataset before merging.

The workflow includes:

- Loading each raw CSV independently.
- Inspecting structure, columns, data types and missing values.
- Handling date fields and preparing them for analysis.
- Converting relevant analytical fields into appropriate numeric formats.
- Removing invalid or unusable records where required by the cleaning process.
- Saving each cleaned dataset immediately after its cleaning stage.
- Selecting Tamil Nadu electricity records only after the state-wise datasets have been cleaned.
- Merging the cleaned Tamil Nadu electricity data with the Tamil Nadu weather data.
- Saving the merged Tamil Nadu analytical dataset before feature engineering and EDA.

---

## Project CSV Outputs

The project produces exactly five CSV outputs:

```text
clean_peak_met_MW.csv
clean_peak_unmet_MW.csv
clean_daily_energy_met_MU.csv
clean_tamil_nadu_weather.csv
Tamil_Nadu_TANGEDCO_Merged_2021_2024.csv
```

The first four files represent the cleaned source datasets. The final file is the merged Tamil Nadu analytical dataset used for feature engineering and exploratory analysis.

---

## Data Transformation and Feature Engineering

After the cleaned Tamil Nadu electricity records are selected and merged with weather data, the notebook creates useful analytical features for exploratory analysis, including date-based fields used for:

- Year-wise analysis
- Month-wise analysis
- Quarter-wise analysis
- Day-of-week analysis
- Year-month analysis

These features support the time-based, comparison and category-wise analyses performed in the notebook.

---

# Data Analysis & Visualization

The project includes the following actual analyses and visualizations.

## 1. Trend Analysis

The trend analysis studies how electricity-demand indicators change across the selected study period.

Actual visualizations:

- **Daily Peak Electricity Load in Tamil Nadu (2021–2024)**
- **Daily Energy Supplied in Tamil Nadu (2021–2024)**
- **Daily Peak Unmet Demand in Tamil Nadu (2021–2024)**

The unmet-demand visualization is retained as a dataset finding because the selected Tamil Nadu unmet-demand values show no variation during the study period.

## 2. Category-wise Analysis

The category-wise analysis compares average peak electricity load across days of the week.

Actual visualization:

- **Average Peak Load by Day of Week**

## 3. Distribution Analysis

The distribution analysis examines how the main electricity variables are spread across the available observations.

Actual visualizations:

- **Distribution of Daily Peak Electricity Load in Tamil Nadu**
- **Peak Load Distribution**
- **Energy Supplied Distribution**

The peak-load and energy-supplied boxplots are shown separately because the variables use different units.

## 4. Correlation Analysis

The correlation analysis examines the associations among selected electricity and weather variables.

Actual visualization:

- **Correlation Matrix: Electricity and Weather Variables**

The unmet-demand field is excluded from the correlation matrix because it has no variation in the selected Tamil Nadu records.

## 5. Comparison Analysis

The comparison analysis compares electricity-demand values across years and identifies the highest-demand days.

Actual visualizations:

- **Average Daily Peak Load by Year**
- **Average Energy Supplied by Year**
- **Top 15 Days by Peak Electricity Load**

## 6. Time-based Analysis

The time-based analysis examines recurring demand patterns across months and year-month combinations.

Actual visualizations:

- **Average Peak Load by Month**
- **Average Energy Supplied by Month**
- **Average Peak Load by Year and Month** (heatmap)

## 7. Relationship Analysis

The relationship analysis examines the association between electricity-demand indicators and selected weather or electricity variables.

Actual visualizations:

- **Mean Temperature vs Daily Peak Electricity Load**
- **Maximum Temperature vs Daily Peak Electricity Load**
- **Mean Solar Radiation vs Daily Peak Load**
- **Mean UTCI vs Daily Peak Electricity Load**
- **Peak Load vs Daily Energy Supplied**
- **Monthly Temperature and Average Peak Load**

These analyses are interpreted as relationships or associations in the data and are not treated as proof of causation.

---

## Additional Analysis Performed

### High-Demand Analysis

The notebook extracts and displays the **Top 15 peak-load days** by sorting daily `Peak_Load_MW` values in descending order. This provides a focused table of the highest-demand periods for closer examination.

### Outlier Analysis Using IQR

The notebook applies the Interquartile Range (IQR) method to identify unusually high or low observations for selected variables.

The analysis includes:

- `Peak_Load_MW`
- `Unmet_Demand_MW`
- `Energy_Supplied_MU`
- `Temperature_C_mean`

Outliers are identified for analysis and are not automatically removed from the dataset.

---

# Key Insights

The following points are based only on the analysis performed in the project notebook:

- The selected Tamil Nadu electricity data show clear daily, yearly, monthly and day-of-week variations in peak electricity load and energy supplied.
- The project identifies the highest-demand days using a Top 15 peak-load analysis.
- The selected Tamil Nadu `Unmet_Demand_MW` values show no variation during the study period; the unmet-demand observations recorded in the selected data are zero.
- The project compares electricity-demand indicators with temperature, solar radiation, UTCI and other weather variables to examine observed relationships.
- Correlation analysis is used to examine the strength and direction of associations among selected electricity and weather variables.
- IQR-based outlier analysis identifies observations that fall outside the calculated lower and upper bounds for selected variables.
- The 2024 study data cover only the period available through **28 April 2024**, so 2024 is a partial year in the analysis.

---

# Recommendations

Based only on the project findings and analysis scope:

- Use the identified high peak-load days as focus periods for closer electricity-demand monitoring and further analysis.
- Consider the observed weather-demand relationships as supporting exploratory evidence when examining demand patterns, without treating them as causal effects.
- Preserve and clearly document the zero unmet-demand pattern in the selected data rather than modifying the recorded values to create variation.
- Treat the 2024 results as a partial-year view because the available study period ends on 28 April 2024.
- Use the outlier results to identify unusual observations for further investigation rather than automatically removing them.

---

# Visualization Screenshots

The actual visualization screenshots can be uploaded to the `Visualizations/` folder in the GitHub repository. Since screenshot filenames have not been supplied here, no made-up filenames are included below.

### Daily Peak Electricity Load in Tamil Nadu (2021–2024)

<!-- Add the actual uploaded screenshot path here. -->

### Daily Energy Supplied in Tamil Nadu (2021–2024)

<!-- Add the actual uploaded screenshot path here. -->

### Average Daily Peak Load by Year

<!-- Add the actual uploaded screenshot path here. -->

### Average Peak Load by Month

<!-- Add the actual uploaded screenshot path here. -->

### Average Peak Load by Day of Week

<!-- Add the actual uploaded screenshot path here. -->

### Correlation Matrix: Electricity and Weather Variables

<!-- Add the actual uploaded screenshot path here. -->

### Mean Temperature vs Daily Peak Electricity Load

<!-- Add the actual uploaded screenshot path here. -->

### Peak Load vs Daily Energy Supplied

<!-- Add the actual uploaded screenshot path here. -->

### Top 15 Days by Peak Electricity Load

<!-- Add the actual uploaded screenshot path here if a screenshot of this table/analysis is uploaded. -->

---

# Project Folder Structure

```text
Exploratory_Analysis_of_TANGEDCO_Electricity_Demand/
│
├── README.md
│
├── Dataset/
│   ├── Raw Data/
│   │   ├── peak_met_MW.csv
│   │   ├── peak_unmet_MW.csv
│   │   ├── corrected_daily_energy_met_MU.csv
│   │   └── Tamil_Nadu_21_24.csv
│   │
│   └── Cleaned Data/
│       ├── clean_peak_met_MW.csv
│       ├── clean_peak_unmet_MW.csv
│       ├── clean_daily_energy_met_MU.csv
│       ├── clean_tamil_nadu_weather.csv
│       └── Tamil_Nadu_TANGEDCO_Merged_2021_2024.csv
│
├── Notebook/
│   └── Exploratory_Analysis_of_TANGEDCO_Electricity_Demand_Final(2).ipynb
│
└── Visualizations/
    └── (Actual visualization screenshots uploaded to GitHub)
```

---

# Reproducibility

The project is organized so that the analysis can be reproduced from the Jupyter Notebook by using the required raw datasets and the listed Python libraries.

The main workflow is:

```text
Load Raw Datasets
        ↓
Initial Inspection
        ↓
Independent Data Cleaning
        ↓
Save Cleaned CSV Files
        ↓
Select Tamil Nadu Electricity Records
        ↓
Merge with Tamil Nadu Weather Data
        ↓
Save Merged Dataset
        ↓
Feature Engineering
        ↓
Exploratory Data Analysis
        ↓
Visualization
        ↓
Interpretation and Findings
```

---

# Project Scope and Limitations

- The project is an exploratory data analysis study and does not build a predictive machine-learning model.
- The selected study period is **01 January 2021 to 28 April 2024**.
- The year 2024 is therefore only partially represented.
- The analysis is based on the selected source datasets and their recorded values.
- The selected Tamil Nadu unmet-demand data contain no variation, so unmet demand does not provide variability for correlation or relationship analysis in this study.
- Relationships observed between weather and electricity variables are exploratory associations and should not be interpreted as causal conclusions.

---

# Dataset Citation

Hunt, K., & Bloomfield, H. (2025). *Daily electricity demand data for Indian states (2014–2024)*. Zenodo. https://doi.org/10.5281/zenodo.14983362

---

# Author

- **Name:** NEHA SHRUTHI U
- **Student ID:** AF05308253
- **Organization:** Anudip Foundation
- **Course:** AIML
- **Batch Code:** ANP-D7444

---

# Summary

**Exploratory Analysis of TANGEDCO Electricity Demand** is a Python-based exploratory data analysis project focused on Tamil Nadu electricity demand using daily electricity and weather data. The project independently cleans the source datasets, selects Tamil Nadu electricity records, merges them with Tamil Nadu weather data and performs trend, category-wise, distribution, correlation, comparison, time-based, relationship, high-demand and outlier analyses.

The final analysis is supported by tables and visualizations created using Pandas, NumPy, Matplotlib and Seaborn, with interpretations based on the actual data available for the study period
