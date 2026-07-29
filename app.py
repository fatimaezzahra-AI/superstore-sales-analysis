import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import sqlite3
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

# 1.
st.set_page_config(
    page_title="Superstore Analytics",
    layout="wide"
)

# 2. Styling
st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
    }
    .kpi-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease;
    }
    .kpi-card:hover {
        transform: translateY(-3px);
    }
    .kpi-title {
        font-size: 0.9rem;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
        margin-bottom: 5px;
    }
    .kpi-value {
        font-size: 1.8rem;
        color: #0f172a;
        font-weight: 700;
    }
    h1 {
        color: #0f172a;
        font-weight: 800 !important;
    }
    h2, h3 {
        color: #1e293b;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        white-space: pre-wrap;
        background-color: #ffffff;
        border-radius: 8px 8px 0px 0px;
        border: 1px solid #e2e8f0;
        font-weight: 600;
        color: #475569;
    }
    .stTabs [aria-selected="true"] {
        background-color: #2563eb !important;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3.SQLite
@st.cache_data
def load_data():
    conn = sqlite3.connect('superstore.db')
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()
    return df

df = load_data()

# 4. Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3081/3081559.png", width=70)
    st.title("Filters & Control")
    st.markdown("---")
    
    region_filter = st.multiselect(" Select Region", options=df['Region'].unique(), default=df['Region'].unique())
    category_filter = st.multiselect(" Select Category", options=df['Category'].unique(), default=df['Category'].unique())
    
    st.markdown("---")
    st.caption(" Built with Streamlit & Scikit-Learn")

filtered_df = df[(df['Region'].isin(region_filter)) & (df['Category'].isin(category_filter))]

# 5. (Title Section)
st.title(" Superstore Business Intelligence")
st.markdown("Advanced Analytics, Machine Learning Predictions & Statistical Insights")
st.markdown("---")

# 6.  KPIs ـ CSS
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Total Sales</div>
            <div class="kpi-value">${filtered_df['Sales'].sum():,.0f}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Total Profit</div>
            <div class="kpi-value" style="color: #10b981;">${filtered_df['Profit'].sum():,.0f}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Avg Discount</div>
            <div class="kpi-value" style="color: #f59e0b;">{filtered_df['Discount'].mean()*100:.1f}%</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Total Orders</div>
            <div class="kpi-value">{len(filtered_df):,}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 7.  Tabs 
tab1, tab2, tab3 = st.tabs([" Statistics & Correlations", " Machine Learning Model", " Category & Segment Breakdown"])

# TAB 1: STATISTICS
with tab1:
    st.subheader("Statistical Relationships")
    col_a, col_b = st.columns(2)
    
    with col_a:
        corr = filtered_df[['Sales', 'Quantity', 'Discount', 'Profit']].corr()
        fig_corr = px.imshow(
            corr, 
            text_auto=True, 
            color_continuous_scale='Blues',
            title="Correlation Heatmap"
        )
        fig_corr.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_corr, use_container_width=True)
        
    with col_b:
        fig_scatter = px.scatter(
            filtered_df, x='Discount', y='Profit', color='Category',
            hover_data=['Sub-Category'], trendline="ols",
            title="Impact of Discount on Profitability",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig_scatter.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_scatter, use_container_width=True)

# TAB 2: MACHINE LEARNING
with tab2:
    st.subheader(" Predict Profitability for New Orders")
    
    features = ['Sales', 'Quantity', 'Discount', 'Category', 'Sub-Category', 'Region', 'Segment']
    df_ml = pd.get_dummies(filtered_df[features + ['Profit']], drop_first=True)
    
    X = df_ml.drop('Profit', axis=1)
    y = df_ml['Profit']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=150, max_depth=12, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    
    m1, m2 = st.columns(2)
    m1.metric("Model R² Score (Accuracy)", f"{r2*100:.1f}%")
    m2.metric("Mean Absolute Error (MAE)", f"${mae:,.2f}")
    
    st.markdown("---")
    st.markdown("###  Simulator: Input Deal Details")
    
    col_i1, col_i2, col_i3 = st.columns(3)
    with col_i1:
        sales_in = st.number_input("Sales Amount ($)", min_value=1.0, value=250.0, step=10.0)
        cat_in = st.selectbox("Category", df['Category'].unique())
    with col_i2:
        qty_in = st.slider("Quantity", 1, 30, 3)
        subcat_in = st.selectbox("Sub-Category", df[df['Category'] == cat_in]['Sub-Category'].unique())
    with col_i3:
        disc_in = st.slider("Discount (%)", 0.0, 0.8, 0.1, step=0.05)
        region_in = st.selectbox("Region", df['Region'].unique())
        seg_in = st.selectbox("Segment", df['Segment'].unique())
    
    if st.button(" Predict Estimated Profit", use_container_width=True):
        input_data = pd.DataFrame(0, index=[0], columns=X.columns)
        input_data['Sales'] = sales_in
        input_data['Quantity'] = qty_in
        input_data['Discount'] = disc_in
        
        for col_name, val in [('Category', cat_in), ('Sub-Category', subcat_in), ('Region', region_in), ('Segment', seg_in)]:
            col_key = f"{col_name}_{val}"
            if col_key in input_data.columns:
                input_data[col_key] = 1
                
        pred_val = model.predict(input_data)[0]
        
        if pred_val >= 0:
            st.success(f" Estimated Profit: **${pred_val:,.2f}**")
        else:
            st.error(f" Estimated Loss: **${pred_val:,.2f}**")

# TAB 3: SEGMENTATION
with tab3:
    st.subheader("Performance Breakdown")
    col_x, col_y = st.columns(2)
    
    with col_x:
        fig_cat = px.bar(
            filtered_df.groupby('Category')[['Sales', 'Profit']].sum().reset_index(),
            x='Category', y=['Sales', 'Profit'], barmode='group',
            title="Sales vs Profit by Category",
            color_discrete_sequence=['#2563eb', '#10b981']
        )
        fig_cat.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_cat, use_container_width=True)
        
    with col_y:
        fig_seg = px.pie(
            filtered_df, names='Segment', values='Sales', 
            title="Sales Distribution by Segment", hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig_seg.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_seg, use_container_width=True)
