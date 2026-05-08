import streamlit as st
import numpy as np
from scipy import stats

st.set_page_config(page_title="Power Calculator — GiveDirectly", page_icon="⚡")

st.title("⚡ Power Calculator")
st.markdown("Quickly compute sample size or minimum detectable effect for RCT designs.")

# Mode selection
mode = st.radio("What do you want to calculate?", ["Sample Size (given MDE)", "MDE (given Sample Size)"])

st.divider()

# Common inputs
col1, col2 = st.columns(2)
with col1:
    alpha = st.number_input("Significance level (α)", value=0.05, min_value=0.001, max_value=0.20, step=0.01)
    power = st.number_input("Power (1 − β)", value=0.80, min_value=0.50, max_value=0.99, step=0.05)
with col2:
    sd = st.number_input("Std. deviation of outcome (σ)", value=100.0, min_value=0.01, step=10.0)
    ratio = st.number_input("Treatment share (proportion treated)", value=0.50, min_value=0.05, max_value=0.95, step=0.05)

# Cluster design
cluster = st.checkbox("Cluster-randomized design")
if cluster:
    col3, col4 = st.columns(2)
    with col3:
        icc = st.number_input("Intra-cluster correlation (ICC)", value=0.05, min_value=0.0, max_value=1.0, step=0.01)
    with col4:
        cluster_size = st.number_input("Average cluster size", value=20, min_value=2, step=5)

st.divider()

# Critical values
z_alpha = stats.norm.ppf(1 - alpha / 2)
z_beta = stats.norm.ppf(power)

# Design effect for clustering
deff = 1.0
if cluster:
    deff = 1 + (cluster_size - 1) * icc

# Variance factor for unequal allocation
var_factor = 1 / (ratio * (1 - ratio))

if mode == "Sample Size (given MDE)":
    mde = st.number_input("Minimum Detectable Effect (MDE)", value=20.0, min_value=0.01, step=5.0)

    n_total = ((z_alpha + z_beta) ** 2 * sd ** 2 * var_factor * deff) / mde ** 2
    n_total = int(np.ceil(n_total))
    n_treat = int(np.ceil(n_total * ratio))
    n_control = n_total - n_treat

    st.subheader("Results")
    st.metric("Total sample size", f"{n_total:,}")
    col5, col6 = st.columns(2)
    with col5:
        st.metric("Treatment group", f"{n_treat:,}")
    with col6:
        st.metric("Control group", f"{n_control:,}")

    if cluster:
        n_clusters = int(np.ceil(n_total / cluster_size))
        st.metric("Minimum clusters needed", f"{n_clusters:,}")

    # Effect size in SD units
    st.caption(f"Standardized effect size: {mde/sd:.3f} SD")

else:
    n_total = st.number_input("Total sample size (N)", value=1000, min_value=10, step=100)

    mde = (z_alpha + z_beta) * sd * np.sqrt(var_factor * deff / n_total)

    st.subheader("Results")
    st.metric("Minimum Detectable Effect (MDE)", f"{mde:.2f}")
    st.caption(f"Standardized: {mde/sd:.3f} SD | You can detect effects ≥ {mde:.2f} units with {power*100:.0f}% power.")

st.divider()
st.markdown("""
**How to use:**
- **σ**: Use the standard deviation of your outcome variable from baseline data or prior studies.
- **MDE**: The smallest effect that would be policy-relevant (e.g., a \$20/month increase in consumption).
- **ICC**: For cluster designs, typically 0.02–0.10 for consumption outcomes in cash transfer studies.

Built by Diego Martín — GiveDirectly Research Team
""")
