# E-commerce Sales & Customer Behaviour Insights

Interactive Streamlit dashboard for exploring a small e‑commerce dataset.  
Built as an end‑to‑end EDA + ML project for internship portfolio and class presentation.

## 🔍 Project Overview

This project analyzes transaction‑level sales data for an online retailer to understand:

- Overall performance (revenue, orders, customers, average order value)
- Sales trends by time, region and product category
- Customer behaviour using RFM segmentation
- Simple churn modelling to identify at‑risk customers

The final deliverable is a Streamlit web app that non‑technical users (like managers or teachers) can open in a browser and explore.

## 🧱 Tech Stack

- **Python**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **ML**: scikit‑learn (RandomForest for churn)
- **App**: Streamlit
- **Data source**: Kaggle – *Sales & Customer Behaviour Insights (Green Cart Ltd)*

## 📂 Project Structure

```text
ecommerce_project/
├── app.py                  # Streamlit dashboard
├── requirements.txt        # Python dependencies
├── data_files/             # Precomputed data used by the app
│   ├── sales_data.csv
│   ├── customer_info.csv
│   ├── product_info.csv
│   ├── kpi_summary.csv
│   ├── rfm_summary.csv
│   └── rfm_with_churn.csv
└── assets/                 # Saved charts used in the app
    ├── revenue_trend.png
    ├── top_categories.png
    └── rfm_segments.png


> Note: The Streamlit app also generates some charts (e.g. churn distribution) dynamically at runtime.

## 📊 What the Dashboard Shows

### 1. KPI Cards

At the top of the app, four cards summarise business performance:

- **Total Revenue** – sum of all order revenue.
- **Total Orders** – number of unique orders.
- **Total Customers** – number of unique customers.
- **Average Order Value (AOV)** – revenue per order.

These come from `kpi_summary.csv` computed during the EDA notebook.

### 2. Sales Trends Tab

- **Monthly Revenue Trend**  
  Simple line plot of total revenue by month (`YearMonth`).  
  In this dataset, all orders occur in June 2025, so the line shows one peak month.

- **Revenue by Region**  
  Bar chart of `quantity × unit_price` aggregated by `region`.  
  Shows that all regions contribute similar revenue, with a slight lead for the South region.

- **Top 10 Categories by Revenue**  
  Horizontal bar chart of the 10 product categories generating the most revenue.  
  Cleaning products dominate, followed by Storage and Outdoors.

### 3. RFM & Churn Tab

- **RFM Segment Summary**  
  RFM (Recency, Frequency, Monetary) scores are computed per customer and grouped into segments such as `511`, `522`, etc.  
  The table shows median recency, frequency, monetary value and count per segment.

- **Top RFM Segments (by count)**  
  Bar chart of the most common RFM scores.  
  This highlights which types of customers (e.g. recent but low‑spend vs. loyal high‑value) dominate the customer base.

- **Churn Distribution & Model**  
  Customers with only one order are labelled as **churned**.  
  A RandomForestClassifier is trained on R, F, M features to predict churn.  
  The app shows:
  - A sample of the `rfm_with_churn.csv` table.
  - A bar chart “Churn vs Non‑Churn Customers”, which clearly shows most customers are currently retained.

### 4. Raw Tables Tab

- Displays the first 20 rows of `sales_data.csv` for transparency and manual inspection.


text
## ⚙️ How to Run Locally

Clone the repo
git clone https://github.com/aniqua14/ecommerce-sales-customer-behaviour.git
cd ecommerce-sales-customer-behaviour

Create virtual environment (optional but recommended)
python -m venv .venv
..venv\Scripts\activate # Windows

Install dependencies
pip install -r requirements.txt

Run Streamlit app
streamlit run app.py

text

Open the URL shown in the terminal (usually `http://localhost:8501`) in your browser.

## 🧠 Key Insights (Example for teacher/interviewer)

- Cleaning and Storage categories generate the highest revenue, suggesting they should be stocked and promoted carefully.
- Revenue is evenly distributed across regions, but South has a small lead.
- RFM analysis reveals that segments `511` and `512` contain the highest number of customers – relatively recent shoppers with low frequency and spend.
- Churn labelling shows only a small fraction of customers churn after a single order, but these customers can be targeted with re‑engagement campaigns.

## 📌 Credits

Dataset: *Sales & Customer Behaviour Insights – Green Cart Ltd* on Kaggle.  
Project author: *[Aniqua Nawar]*.


