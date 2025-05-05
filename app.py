import streamlit as st
from PIL import Image

st.set_page_config(page_title="Incredible India - Culture Explorer", layout="wide")

# Banner
st.image("images/banner.jpg", use_column_width=True)

st.title("Incredible India: Culture, Art, and Heritage")
st.markdown("Explore India’s diverse art forms, hidden cultural treasures, and responsible tourism insights.")

# Tabs
tab1, tab2, tab3 = st.tabs(["Traditional Art Forms", "Cultural Hotspots", "Tourism & Sustainability"])

with tab1:
    st.subheader("Traditional Indian Art")
    st.write("Explore Warli, Madhubani, Pattachitra, and more through curated visuals and stories.")

with tab2:
    st.subheader("Cultural Hotspots Map")
    st.write("Coming soon: Interactive map of cultural destinations with visitor data!")

with tab3:
    st.subheader("Responsible Tourism")
    st.write("Understand how tourism affects heritage sites and how to be a conscious traveler.")

# Footer
st.markdown("---")
st.caption("Built for Snowflake Hackathon 2025 | Team CulturalConnect")