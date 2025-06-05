import streamlit as st
import pandas as pd

# Sample data - in a real app, this could be fetched live from APIs
data = {
    "Metric": [
        "GIFT Nifty Change", 
        "US Market (Nasdaq)", 
        "FII Activity (Prev Day)", 
        "India VIX Change", 
        "Options PCR", 
        "OI Shift", 
        "Pre-Market A/D Ratio", 
        "Event Today?"
    ],
    "Value": [
        "+115 pts", 
        "+1.6%", 
        "₹3,200 Cr Buy", 
        "12.5 ➔ 14.1", 
        "1.4", 
        "Put Writing @ 22,400-22,500", 
        "5:1", 
        "No Major Event"
    ],
    "Interpretation": [
        "Strong bullish gap-up", 
        "Momentum from global tech", 
        "Bullish institutional bias", 
        "Volatility increasing", 
        "Bullish bias", 
        "Support zone forming", 
        "Positive sentiment", 
        "No disruption expected"
    ],
    "Trend Likely": [
        "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Neutral"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Streamlit UI
st.set_page_config(page_title="Nifty Pre-Market Trend Scanner", layout="wide")
st.title("📈 Nifty50 Pre-Market Trend Scanner")

st.markdown("""
This tool helps you evaluate whether **Nifty50 is likely to trend** today based on:
- GIFT Nifty
- Global Markets
- FII/DII Flows
- India VIX
- Option Chain Data
- Pre-market Ratios
""")

# Display table
st.dataframe(df, use_container_width=True)

# Summary Score
trend_votes = df[df['Trend Likely'] == 'Yes'].shape[0]
summary = "Trending day likely!" if trend_votes >= 5 else "Possibly sideways or choppy."

st.subheader("Summary")
st.success(summary if trend_votes >= 5 else summary)

# Optional: allow user input later for live updates
