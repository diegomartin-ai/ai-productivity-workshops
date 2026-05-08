# ⚡ Power Calculator

A reusable tool for GiveDirectly teams to quickly compute sample sizes and minimum detectable effects for RCT designs.

## Features

- **Two modes:** Calculate sample size given MDE, or MDE given sample size
- **Cluster-randomized designs:** Accounts for ICC and cluster size (design effect)
- **Flexible allocation:** Supports unequal treatment/control splits
- **Instant results:** No code required — just input parameters and read the output

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Cloud

1. Push to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Point to `tools/power-calculator/app.py`
4. Done — shareable URL for the whole org

## When to use

- Designing a new RCT (how many households do we need?)
- Evaluating feasibility (can we detect a meaningful effect with our budget?)
- Comparing designs (individual vs. cluster randomization trade-offs)
