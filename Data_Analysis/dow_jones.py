import streamlit as st
import seaborn as sns


# Set page config (optional)
st.set_page_config(page_title="Data Analysis of Dow Jones Dataset", layout="wide")


# --- Custom CSS for Sidebar ---
# --- Custom CSS for Sidebar Buttons ---
st.markdown(
    """
    <style>
    /* Make sidebar buttons bigger and bold */
    section[data-testid="stSidebar"] button {
        font-size: 18px !important;
        font-weight: 700 !important;
        padding: 12px 16px !important;
        margin-bottom: 12px !important;
        border-radius: 10px !important;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)




# Side bar section
st.sidebar.title("Sidebar Menu")

# Create buttons
pages = ["Home" , "Highlights", "Dashboard", "Analytics", "Settings"]
selected_page = None

for page in pages:
    if st.sidebar.button(page):
        selected_page = page

# Default to Home if nothing clicked
if not selected_page:
    selected_page = "Home"

#Display section
if selected_page == "Home":
    st.title("Home")
    st.write("*This App analyzes the Dow Jones datasets between 1911-1968*")

elif selected_page == "Highlights":
    st.title("highlights")
    st.write("# Data Analysis of Dow Jones Dataset")

    #Load pre built dow jones dataset
    df = sns.load_dataset("dowjones")

    st.write("### Highlight of begining of Dow Jones Dataset")
    st.write(df.head())

    st.write("### Highlight of ending of Dow Jones Dataset")
    st.write(df.tail())






