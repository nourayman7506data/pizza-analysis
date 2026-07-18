# 🍕 Pizza Sales Dynamic Dashboard

An interactive and dynamic web application built with **Python**, **Streamlit**, **Pandas**, and **Plotly** to analyze and visualize pizza sales data. This project was developed as a hands-on practical application to solidify data analysis concepts during my learning journey with the **Digital Egypt Pioneers Initiative (DEBI)**.

## ✨ Key Features
* **Data Cleaning & Preprocessing:** Handled duplicate records, formatted mixed date styles, and extracted explicit temporal features (Months and Hours) utilizing `Pandas`.
* **Real-time Key Performance Indicators (KPIs):** Dynamically tracks and displays **Total Revenue**, **Total Orders**, and **Average Order Value (AOV)** based on custom selection.
* **Interactive Data Visualizations:** 
  * Bar chart representing *Revenue by Pizza Category*.
  * Pie chart illustrating *Revenue Distribution by Pizza Size*.
* **Peak Hours Analysis:** Line plot tracking total orders across hours of the day to identify peak business operational timing.
* **Dynamic Sidebar Filters:** Multiselect options allowing deep-dive filtering across Months, Categories, Sizes, and Specific Pizza Names simultaneously.

## 🛠️ Tech Stack & Libraries
* **Language:** Python
* **Framework:** Streamlit (Dashboard UI)
* **Data Manipulation:** Pandas
* **Data Visualization:** Plotly Express

## 📂 Project Structure
```bash
├── pizza.py          # Main Streamlit application source code
└── pizza_sales.csv   # Raw pizza sales transaction dataset
