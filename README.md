# Retail Sales Forecasting — Walmart Weekly Sales

Forecasts weekly sales for every store-department across 45 Walmart stores to support inventory, staffing and promotion planning.

## Data
[Walmart Recruiting – Store Sales Forecasting](https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting/data) (Kaggle): `train.csv`, `stores.csv`, `features.csv` (~4.2 lakh weekly records, Feb 2010 – Oct 2012).
The data is not included in this repo — download it from Kaggle.

## Approach
1. **Cleaning & merging:** dates, store type/size, external factors (temperature, fuel price, CPI, unemployment), markdowns (promotions).
2. **Feature engineering:** year, month, week, holiday flag, one-hot store type, lag features (last week, same week last year), 4-week rolling average.
3. **Time-based split:** train on the older 80% of weeks, test on the most recent 20% (avoids data leakage).
4. **Models:** baseline (store-department average), Linear Regression, Random Forest, XGBoost.
5. **Evaluation:** MAE, RMSE, and holiday-weighted WMAE; time-series cross-validation across four periods.
6. **Outputs:** Power BI dashboard and a Streamlit app.

## Results
<!-- Paste your results table from the notebook here -->
| Model | MAE | RMSE | WMAE |
|---|---|---|---|
| Baseline | | | |
| Linear Regression | | | |
| Random Forest | | | |
| XGBoost | | | |

## Key insights
<!-- e.g. holiday uplift %, top features -->

## Dashboard
<!-- Add Power BI and Streamlit screenshots -->

## How to run
```
pip install -r requirements.txt
# put train.csv, stores.csv, features.csv next to the notebook, then run retail_sales_forecasting.ipynb
streamlit run app.py
```
