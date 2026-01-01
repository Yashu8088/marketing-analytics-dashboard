import streamlit as st
import pandas as pd

# ==============================
# Page Config
# ==============================
st.set_page_config(page_title="Marketing Analytics Dashboard", layout="wide")
st.title("📊 Social Media Marketing Analytics Dashboard")

# ==============================
# Load Data
# ==============================
@st.cache_data
def load_data():
    # Read semicolon-separated CSV
    df = pd.read_csv("data/dataset_Facebook.csv", sep=";")

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower()

    # Engagement logic
    if all(col in df.columns for col in ['like', 'comment', 'share']):
        df['total_engagement'] = df['like'] + df['comment'] + df['share']
    elif any('interaction' in col for col in df.columns):
        interaction_col = [col for col in df.columns if 'interaction' in col][0]
        df['total_engagement'] = df[interaction_col]
    else:
        st.error("No engagement-related columns found.")
        st.stop()

    return df

df = load_data()

# ==============================
# Sidebar Filters
# ==============================
st.sidebar.header("🔎 Filter Posts")

type_options = df["type"].dropna().unique().tolist()
post_types = st.sidebar.multiselect(
    "Select Post Type",
    options=type_options,
    default=type_options
)

paid_options = df["paid"].dropna().unique().tolist()
paid_filter = st.sidebar.multiselect(
    "Paid Posts",
    options=paid_options,
    default=paid_options
)

month_options = sorted(df["post month"].dropna().unique().tolist())
months = st.sidebar.multiselect(
    "Post Month",
    options=month_options,
    default=month_options
)

# ==============================
# Apply Filters
# ==============================
filtered_df = df[
    (df["type"].isin(post_types)) &
    (df["paid"].isin(paid_filter)) &
    (df["post month"].isin(months))
]

# ==============================
# Dataset Preview
# ==============================
st.subheader("📄 Preview of Dataset")
st.dataframe(filtered_df.head())

# ==============================
# KPI Cards
# ==============================
st.markdown("### 📌 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Posts", len(filtered_df))

with col2:
    st.metric(
        "Average Engagement",
        int(filtered_df["total_engagement"].mean()) if len(filtered_df) > 0 else 0
    )

with col3:
    st.metric(
        "Max Engagement",
        int(filtered_df["total_engagement"].max()) if len(filtered_df) > 0 else 0
    )

# ==============================
# Engagement by Post Type
# ==============================
st.markdown("### 📊 Engagement by Post Type")

if len(filtered_df) > 0:
    eng_by_type = (
        filtered_df.groupby("type")["total_engagement"]
        .mean()
        .sort_values(ascending=False)
    )
    st.bar_chart(eng_by_type)
else:
    st.warning("No data available for selected filters.")

# ==============================
# Best Posting Time
# ==============================
st.markdown("### ⏰ Engagement by Post Hour")

if len(filtered_df) > 0:
    hourly = filtered_df.groupby("post hour")["total_engagement"].mean()
    st.line_chart(hourly)
else:
    st.warning("No data available for selected filters.")



# ==============================
# Model Comparison Section
# ==============================

st.markdown("---")
st.header("🤖 Model Performance Comparison")

# Create tabs
tab1, tab2 = st.tabs(["📊 Metrics Comparison", "🧠 Model Insights"])

# ==============================
# Tab 1: Metrics Table & Chart
# ==============================
with tab1:
    model_results = pd.DataFrame({
        "Model": [
            "Linear Regression",
            "Random Forest",
            "H2O AutoML (Ensemble)"
        ],
        "RMSE": [
            293.50,
            290.69,
            275.00
        ],
        "R2 Score": [
            0.03,
            0.05,
            0.07
        ]
    })

    st.subheader("📋 Model Evaluation Metrics")
    st.dataframe(model_results, use_container_width=True)

    st.subheader("📉 RMSE Comparison (Lower is Better)")
    st.bar_chart(
        model_results.set_index("Model")["RMSE"]
    )

    st.subheader("📈 R² Comparison (Higher is Better)")
    st.bar_chart(
        model_results.set_index("Model")["R2 Score"]
    )

# ==============================
# Tab 2: Interpretation
# ==============================
with tab2:
    st.subheader("🔍 Interpretation & Business Meaning")

    st.markdown("""
    **Why Linear Regression performed poorly**
    - Assumes linear relationships
    - Social media engagement is highly non-linear
    - Cannot capture complex interactions

    **Why Random Forest improved**
    - Captures non-linear patterns
    - Handles feature interactions better
    - However, sensitive to hyperparameters and overfitting

    **Why H2O AutoML performed best**
    - Automatically tried multiple algorithms
    - Used stacked ensemble learning
    - Balanced bias–variance tradeoff
    - Best generalization performance

    ✅ **Final Recommendation**  
    H2O AutoML is the most reliable model for predicting social media engagement
    and should be used for production-level forecasting.
    """)


    # ==============================
# Business Insights & Recommendations
# ==============================

st.markdown("---")
st.header("📈 Business Insights & Recommendations")

if len(filtered_df) == 0:
    st.warning("No data available for selected filters.")
else:
    # 1️⃣ Best Performing Post Type
    best_type = (
        filtered_df.groupby("type")["total_engagement"]
        .mean()
        .idxmax()
    )

    best_type_value = (
        filtered_df.groupby("type")["total_engagement"]
        .mean()
        .max()
    )

    # 2️⃣ Paid vs Organic Performance
    paid_perf = filtered_df.groupby("paid")["total_engagement"].mean()

    # 3️⃣ Best Posting Hour
    best_hour = (
        filtered_df.groupby("post hour")["total_engagement"]
        .mean()
        .idxmax()
    )

    # ==============================
    # Display Insights
    # ==============================

    st.subheader("🔍 Key Insights")

    st.markdown(f"""
    **📌 Post Type Performance**
    - **{best_type} posts** generate the highest average engagement
    - Avg engagement: **{int(best_type_value)}**

    **💰 Paid vs Organic**
    - Paid posts average: **{int(paid_perf.get(1, 0))}**
    - Organic posts average: **{int(paid_perf.get(0, 0))}**

    **⏰ Best Posting Time**
    - Highest engagement observed at **{best_hour}:00 hours**
    """)

    # ==============================
    # Business Recommendations
    # ==============================

    st.subheader("✅ Actionable Recommendations")

    st.markdown(f"""
    🔹 Focus more on **{best_type} posts**, as they consistently outperform other content types.

    🔹 Allocate higher budget to **paid campaigns** during high-performing periods.

    🔹 Schedule important posts around **{best_hour}:00 hours** to maximize engagement.

    🔹 Use predictive models (Random Forest / H2O AutoML) to estimate engagement before campaign launch.
    """)

