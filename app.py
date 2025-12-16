import streamlit as st
import pandas as pd
from PIL import Image
import os
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="E-commerce Sales & Customer Analytics",
    layout="wide"
)

base_path = "."

st.title("📦 E-commerce Sales & Customer Behaviour Insights")
st.markdown("---")

# ---------- Load KPI summary ----------
kpi_path = os.path.join(base_path, "kpi_summary.csv")
kpi_df = pd.read_csv(kpi_path)


def get_metric(name, default=0):
    row = kpi_df.loc[kpi_df["Metric"] == name, "Value"]
    return row.values[0] if len(row) else default


col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"{get_metric('Total_Revenue'):,.0f}")
col2.metric("Total Orders", f"{int(get_metric('Total_Orders')):,}")
col3.metric("Total Customers", f"{int(get_metric('Total_Customers')):,}")
col4.metric("Avg Order Value", f"{get_metric('Avg_Order_Value'):,.2f}")

tab1, tab2, tab3 = st.tabs(["📈 Sales Trends", "👥 RFM & Churn", "📊 Raw Tables"])

# ---------- TAB 1: Sales Trends ----------
with tab1:
    st.subheader("Monthly Revenue Trend")
    rev_img_path = os.path.join(base_path, "revenue_trend.png")
    if os.path.exists(rev_img_path):
        st.image(Image.open(rev_img_path))
    else:
        st.info("No revenue_trend.png found. Re-run the plotting cell with savefig().")

    st.subheader("Revenue by Region")
    sales_path = os.path.join(base_path, "sales_data.csv")
    if os.path.exists(sales_path):
        df_sales = pd.read_csv(sales_path)

        # Ensure numeric and create Revenue column
        if "Revenue" not in df_sales.columns:
            df_sales["quantity"] = pd.to_numeric(
                df_sales["quantity"], errors="coerce")
            df_sales["unit_price"] = pd.to_numeric(
                df_sales["unit_price"], errors="coerce")
            df_sales["Revenue"] = df_sales["quantity"] * df_sales["unit_price"]

        if "region" in df_sales.columns:
            region_rev = df_sales.groupby(
                "region")["Revenue"].sum().reset_index()
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.barplot(data=region_rev, x="region",
                        y="Revenue", ax=ax, palette="viridis")
            ax.set_title("Revenue by Region")
            ax.set_xlabel("Region")
            ax.set_ylabel("Total Revenue")
            st.pyplot(fig)
        else:
            st.info("Column 'region' not found in sales_data.csv.")
    else:
        st.info("sales_data.csv not found.")

    # NEW: Top 10 categories plot
    st.subheader("Top 10 Categories by Revenue")
    top_cat_path = os.path.join(base_path, "top_categories.png")
    if os.path.exists(top_cat_path):
        st.image(Image.open(top_cat_path))
    else:
        st.info(
            "top_categories.png not found. Save the category plot as top_categories.png.")


# ---------- TAB 2: RFM & Churn ----------
with tab2:
    st.subheader("RFM Segment Summary")
    rfm_summary_path = os.path.join(base_path, "rfm_summary.csv")
    if os.path.exists(rfm_summary_path):
        rfm_summary = pd.read_csv(rfm_summary_path)
        st.dataframe(rfm_summary.head(15))
        st.subheader("Top RFM Segments (by count)")
        rfm_seg_path = os.path.join(base_path, "rfm_segments.png")
        if os.path.exists(rfm_seg_path):
            st.image(Image.open(rfm_seg_path))
        else:
            st.info(
                "rfm_segments.png not found. Save the RFM segments plot as rfm_segments.png.")

    else:
        st.info("rfm_summary.csv not found.")

    st.subheader("RFM with Churn (sample + chart)")
    rfm_churn_path = os.path.join(base_path, "rfm_with_churn.csv")
    if os.path.exists(rfm_churn_path):
        rfm_churn = pd.read_csv(rfm_churn_path)
        st.dataframe(rfm_churn.sample(min(10, len(rfm_churn))))

        # Churn distribution bar chart
        churn_counts = rfm_churn["Churn"].value_counts().rename(
            index={0: "Not Churn", 1: "Churn"}
        )
        fig2, ax2 = plt.subplots(figsize=(4, 4))
        sns.barplot(x=churn_counts.index, y=churn_counts.values,
                    ax=ax2, palette="magma")
        ax2.set_title("Churn vs Non-Churn Customers")
        ax2.set_ylabel("Number of Customers")
        st.pyplot(fig2)
    else:
        st.info("rfm_with_churn.csv not found.")

# ---------- TAB 3: Raw Tables ----------
with tab3:
    st.subheader("Sample Sales Rows")
    sales_path = os.path.join(base_path, "sales_data.csv")
    if os.path.exists(sales_path):
        df_sales = pd.read_csv(sales_path)
        st.dataframe(df_sales.head(20))
    else:
        st.info("sales_data.csv not found.")

st.markdown("---")
st.caption(
    "Built as a Data Science Portfolio Project (Sales & Customer Behaviour Analysis)"
)
