import streamlit as st
from dotenv import load_dotenv


# Import project modules
from city_logic import generate_city_plan
from map_renderer import draw_city
from metrics import calculate_metrics
from ai_explainer import explain_city
from db_operations import save_scenario

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="Smart City Planning with GenAI",
    layout="wide"
)

st.title("🏙️ Smart City Planning with Generative AI")
st.write(
    "A decision-support tool to visualize smart city layouts, "
    "evaluate sustainability, and generate explainable insights using AI."
)

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("📊 City Planning Inputs")

population = st.sidebar.selectbox(
    "Population Level", ["Low", "Medium", "High"]
)

traffic = st.sidebar.selectbox(
    "Traffic Level", ["Low", "Medium", "High"]
)

energy = st.sidebar.selectbox(
    "Energy Demand", ["Low", "Medium", "High"]
)

renewable = st.sidebar.slider(
    "Renewable Energy Target (%)", 0, 100, 40
)

green_priority = st.sidebar.selectbox(
    "Green Space Priority", ["Low", "Medium", "High"]
)

scenario = st.sidebar.radio(
    "Scenario Type", ["Baseline", "Sustainable"]
)

# Auto-adjust for sustainable scenario
if scenario == "Sustainable":
    renewable = max(renewable, 70)
    green_priority = "High"

# -----------------------------
# Generate City Plan
# -----------------------------
plan = generate_city_plan(
    population=population,
    traffic=traffic,
    green=green_priority
)

# -----------------------------
# Layout: Map + Metrics
# -----------------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🗺️ City Layout Visualization")
    draw_city(plan)

with col2:
    st.subheader("🌱 Sustainability Metrics")
    metrics = calculate_metrics(plan, renewable)
    for key, value in metrics.items():
        st.metric(label=key, value=value)

# -----------------------------
# AI Explanation Section
# -----------------------------
st.subheader("🧠 AI Explanation")

if st.button("Explain City Design"):
    with st.spinner("Generating explanation using Gemini AI..."):
        prompt = f"""
City Inputs:
Population: {population}
Traffic: {traffic}
Energy Demand: {energy}
Renewable Energy Target: {renewable}%
Green Priority: {green_priority}
Scenario: {scenario}

City Plan:
{plan}

Sustainability Metrics:
{metrics}

Explain why this city layout was generated, how sustainability goals influenced
the design, and one key trade-off made. Use simple language.
"""
        try:
            explanation = explain_city(prompt)
            st.write(explanation)
        except Exception as e:
            st.warning(
                "AI explanation could not be generated right now. "
                "Please try again later."
            )

# -----------------------------
# Save Scenario to Supabase
# -----------------------------
st.subheader("💾 Save Scenario")

if st.button("Save This Scenario"):
    save_scenario(
        {
            "population": population,
            "traffic": traffic,
            "energy": energy,
            "renewable": renewable,
            "green_priority": green_priority,
            "scenario": scenario
        },
        plan,
        metrics
    )
    st.success("Scenario saved successfully to database!")
