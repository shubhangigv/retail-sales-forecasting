# Streamlit app: explore actual vs predicted weekly sales
# Run with:  streamlit run app.py   (needs predictions.csv and model_results.csv in the same folder)
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Retail Sales Forecasting", layout="wide")
st.title("Retail Sales Forecasting — Walmart")
st.write("Actual vs predicted weekly sales for each store and department (test period).")

@st.cache_data                                   # load once, reuse on every interaction
def load():
    preds = pd.read_csv("predictions.csv", parse_dates=["Date"])
    results = pd.read_csv("model_results.csv")
    return preds, results

preds, results = load()

# Sidebar filters
store = st.sidebar.selectbox("Store", sorted(preds["Store"].unique()))
depts = sorted(preds.loc[preds["Store"] == store, "Dept"].unique())
dept = st.sidebar.selectbox("Department", depts)

data = preds[(preds["Store"] == store) & (preds["Dept"] == dept)].sort_values("Date")

# Key numbers for this store-department
c1, c2, c3 = st.columns(3)
c1.metric("Store type", data["StoreType"].iloc[0])
c2.metric("Avg weekly sales", f"${data['Actual'].mean():,.0f}")
c3.metric("Avg forecast error (MAE)", f"${data['AbsError'].mean():,.0f}")

st.subheader("Actual vs predicted")
st.line_chart(data.set_index("Date")[["Actual", "Predicted"]])

st.subheader("Model comparison (all stores)")
st.dataframe(results, use_container_width=True)

st.subheader("Recommendations")
st.write("- Increase stock and staffing before holiday weeks, which sell more on average.")
st.write("- Plan inventory per department and store size rather than one rule for all stores.")
st.write("- Use the model's forecasts for ordering instead of simple averages to reduce stock-outs.")
