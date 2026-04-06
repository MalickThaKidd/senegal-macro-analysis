# Senegal Macroeconomic Analysis

This project analyzes key macroeconomic indicators for Senegal using data from the World Bank API.

The goal is to build a clean, reproducible pipeline to retrieve, process, and visualize economic data.

---

## Indicators

The analysis currently focuses on:

- GDP (NY.GDP.MKTP.CD)
- Inflation (FP.CPI.TOTL.ZG)

---

## Data Source

All data is retrieved from the World Bank API.

- Country: Senegal (SN)
- Period: 2000 – 2024

---

## Project Structure
senegal-macro-analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── senegal_macroeconomic_analysis.ipynb
│
├── src/
│   └── utils.py
│
├── README.md
└── requirements.txt

---

## Methodology

The analysis follows a structured pipeline:

1. Data collection using the World Bank API  
2. Data cleaning (handling missing values and detecting outliers using the IQR method)  
3. Data visualization (time series, distributions, and relationships)

---

## Utility Functions

Reusable functions are implemented in:

`src/utils.py`

They include:

- `get_data` → retrieve and structure data from the API  
- `clean_data` → clean dataset and detect/remove outliers  
- `line_plt` → time series visualization  
- `hist_plt` → distribution analysis  
- `scat_plt` → relationship between variables  
- `box_plt` → outlier detection  

Each function is modular and documented with clear parameters.

---

## How to Use

Clone the repository:

```bash
git clone https://github.com/your-username/senegal-macro-analysis.git
cd senegal-macro-analysis
