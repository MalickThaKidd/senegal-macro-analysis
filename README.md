# 🇸🇳 Senegal Macroeconomic Analysis

This project analyzes key macroeconomic indicators for Senegal using data from the World Bank API.

The goal is to build a clean, reproducible pipeline to retrieve, process, and visualize economic data.

---

## Indicators

The analysis currently focuses on:

- GDP — `NY.GDP.MKTP.CD`
- Inflation — `FP.CPI.TOTL.ZG`

---

## Data Source

All data is retrieved from the World Bank Open Data API.

- Country: Senegal (SN)
- Period: 1990 – 2024

---

## Project Structure

```
senegal-macro-analysis/
|
├── data/
│   ├── raw/
│   └── processed/
|
├── notebooks/
│   └── senegal_macroeconomic_analysis.ipynb
|
├── src/
│   ├── utils.py          # Data retrieval, cleaning, and visualization functions
│   └── indicators.py     # Macroeconomic indicator functions
|
├── README.md
└── requirements.txt
```

---

## Methodology

The analysis follows a structured pipeline:

1. Data collection from the World Bank API
2. Data cleaning, including missing values handling and outlier detection
3. Macroeconomic indicator computation
   - GDP growth rate
   - CAGR / TCAM
4. Data visualization and economic interpretation

---

## Utility Functions

Reusable functions are implemented in the `src/` directory.

`src/utils.py` includes:
- `get_data` → retrieve and structure data from the World Bank API
- `clean_data` → clean datasets and detect/remove outliers
- `line_plt` → time series visualization
- `hist_plt` → distribution analysis
- `scat_plt` → relationship between variables
- `box_plt` → outlier visualization

`src/indicators.py` includes:
- `compute_growth_rate` → compute annual percentage growth
- `compute_cagr` → compute compound annual growth rate over a selected period

---
## 🎯 Future Improvements

### Roadmap

- [x] Build a clean data pipeline using the World Bank API

- [x] Add data cleaning and outlier detection functions

- [x] Add reusable visualization functions

- [x] Add GDP growth rate indicator

- [x] Add CAGR / TCAM indicator

- [ ] Add more macroeconomic indicators such as debt, trade balance, openness ratio, and investment rate

- [ ] Add time series analysis tools such as moving averages, volatility, and stationarity tests

- [ ] Add forecasting models such as ARIMA and VAR

- [ ] Add economic interpretation modules linking macroeconomic variables

- [ ] Build an interactive dashboard for country-level macroeconomic analysis

---

## How to Use

Clone the repository:

```bash
git clone https://github.com/MalickThaKidd/senegal-macro-analysis.git
cd senegal-macro-analysis
