import streamlit as st
import pandas as pd

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("social_media_post_ideas_full.csv")

df = load_data()

# App Title
st.title("📢 Niche Social Media Post Idea Generator")
st.markdown("Generate fresh post ideas tailored to your niche and tone!")

# Sidebar Filters
st.sidebar.header("Filters")
niche = st.sidebar.selectbox("Select your niche", df['niche'].unique())
tone = st.sidebar.selectbox("Select content tone", df['tone'].unique())
num_ideas = st.sidebar.slider("Number of ideas", 1, 10, 5)

# Filter Data
filtered_df = df[(df['niche'] == niche) & (df['tone'] == tone)]

# Generate
if st.button("Generate Ideas"):
    if not filtered_df.empty:
        ideas = filtered_df.sample(min(num_ideas, len(filtered_df)), random_state=None)
        for _, row in ideas.iterrows():
            st.subheader(f"💡 {row['hook']}")
            st.write(row['idea'])
            st.write(f"**Hashtags:** {row['hashtags']}")
            st.markdown("---")
    else:
        st.warning("No ideas found for this selection.")

st.caption("Created by YourName – Full version available on Gumroad.")
