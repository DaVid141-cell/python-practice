# 🦠 COVID-19 Data Analysis Project  

## 📌 Overview  
This project focuses on analyzing global COVID-19 data to explore patterns, trends, and correlations across time, countries, and regions. Using Python, pandas, and visualization libraries, the project is divided into multiple activities — each designed to highlight different aspects of the pandemic, such as worldwide impact, regional differences, time series trends, and external influencing factors.  

---

## ⚙️ Technical Environment  
The project was developed using the following tools and libraries:  
- **VS Code** → Main IDE used for coding.  
- **Jupyter Notebook (inside VS Code)** → Used for step-by-step execution and converting `.py` files into `.ipynb`.  
- **Pandas** → For data manipulation, cleaning, and feature engineering.  
- **Matplotlib.pyplot** → For generating basic plots and visualizations.  
- **Seaborn** → For advanced statistical visualization and heatmaps.  

---

## 📊 Activities  

### **Activity 1: Data Loading and Exploration**  
- Loaded the COVID-19 dataset using pandas.  
- Displayed the first 5 and last 5 rows.  
- Checked for missing values and decided handling strategies.  
- Dropped columns with more than 90% missing values.  
- Converted the `'date'` column to datetime format.  

---

### **Activity 2: Data Cleaning and Feature Engineering**  
- Imputed missing values in key columns.  
- Removed duplicate rows.  
- Created new features (e.g., extracting year and month from `'date'`).  
- Explored unique countries and counted the total number of countries.  

---

### **Activity 3: Worldwide COVID-19 Overview**  
- Visualized WHO regions with total cases and deaths using bar plots.  
- Explored worldwide monthly case trends with line plots.  
- Investigated correlation between total cases and total deaths with a heatmap.  
- Analyzed case evolution over time for a specific country (e.g., India).  

---

### **Activity 4: Regional Analysis**  
- Created grouped bar charts for new cases by continent and month.  
- Visualized yearly total cases using box plots.  
- Compared total deaths across continents with bar plots.  
- Analyzed month-by-month total case progression with bar plots.  

---

### **Activity 5: Time Series Analysis**  
- Explored daily global trends for new cases and new deaths using line plots.  
- Calculated and visualized daily averages of cases and deaths.  
- Examined vaccination coverage trends over time.  
- Analyzed total tests and positivity rates using a log scale for clearer visualization.  

---

### **Activity 6: In-Depth Country Analysis**  
- Visualized specific country’s total cases and deaths over time.  
- Added user input to select a country and metric (`total_cases` or `total_deaths`) for line chart plotting.  
- Analyzed distribution of total cases across continents using box plots.  
- Visualized year-wise monthly trends of new cases for user-selected countries.  

---

### **Activity 7: Additional Insights**  
- Visualized global fatality rate trends (`total_deaths / total_cases`).  
- Explored positivity rate versus total tests using log-scale x-axis.  
- Investigated fatality rate correlations with smoking rates (male vs female).  
- Created heatmaps to analyze hospital bed availability versus fatality rates.  

---



