import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Pizza Sales Dashboard", layout="wide")
st.title("🍕 Pizza Sales Dynamic Dashboard")
st.markdown("Smart Pizza Sales Analysis - Control data from the sidebar")
st.markdown("---")

# 2. Load and Clean Data
@st.cache_data
def load_data():
    df = pd.read_csv('pizza_sales.csv')
    df.drop_duplicates(inplace=True)
    df.rename(columns={'order_id': 'Order Num'}, inplace=True)
    df['order_date'] = pd.to_datetime(df['order_date'], format='mixed', dayfirst=True)
    
    # Extract Month and Hour for analysis
    df['Month'] = df['order_date'].dt.month_name()
    df['Hour'] = pd.to_datetime(df['order_time'], format='%H:%M:%S').dt.hour
    return df

df = load_data()

# 3. Sidebar (Filters)
st.sidebar.header("Dashboard Filters")
months = st.sidebar.multiselect("Select Month:", options=df['Month'].unique(), default=df['Month'].unique())
categories = st.sidebar.multiselect("Select Category:", options=df['pizza_category'].unique(), default=df['pizza_category'].unique())
sizes = st.sidebar.multiselect("Select Size:", options=df['pizza_size'].unique(), default=df['pizza_size'].unique())
pizza_names = st.sidebar.multiselect("Select Pizza Name:", options=df['pizza_name'].unique(), default=df['pizza_name'].unique())

# Apply Filters
df_selection = df[
    (df['Month'].isin(months)) & 
    (df['pizza_category'].isin(categories)) & 
    (df['pizza_size'].isin(sizes)) & 
    (df['pizza_name'].isin(pizza_names))
]

# 4. KPIs
total_revenue = df_selection['total_price'].sum()
total_orders = df_selection['Order Num'].nunique()
avg_val = total_revenue / total_orders if total_orders > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Orders", total_orders)
col3.metric("Avg Order Value", f"${avg_val:,.2f}")

st.markdown("---")

# 5. Visualizations
col_a, col_b = st.columns(2)

with col_a:
    fig1 = px.bar(df_selection.groupby('pizza_category')['total_price'].sum().reset_index(), 
                  x='pizza_category', y='total_price', title="Revenue by Category", color='pizza_category')
    st.plotly_chart(fig1, use_container_width=True)

with col_b:
    fig2 = px.pie(df_selection, values='total_price', names='pizza_size', title="Revenue Distribution by Size")
    st.plotly_chart(fig2, use_container_width=True)

# 6. Peak Hours Visualization
st.subheader("📊 Peak Hours Analysis")
hourly_df = df_selection.groupby('Hour')['Order Num'].count().reset_index()
fig3 = px.line(hourly_df, x='Hour', y='Order Num', title="Orders by Hour of the Day", markers=True)
st.plotly_chart(fig3, use_container_width=True)