import streamlit as st
import pandas as pd
import csv

# Constants
DATA_URL = "crewai_env/Scripts/marketplace_test_report.csv"

# Title
st.title("Marketplace Test Report Dashboard")

# Function to detect delimiter
def detect_delimiter(file_path):
    try:
        with open(file_path, "r") as f:
            return csv.Sniffer().sniff(f.read(1024)).delimiter
    except Exception as e:
        st.error(f"Error detecting delimiter: {e}")
        return ","  # Default to comma

# Function to load data
@st.cache_data
def load_data(data_url):
    try:
        # Detect delimiter dynamically
        delimiter = detect_delimiter(data_url)
        # Load the CSV file
        df = pd.read_csv(data_url, delimiter=delimiter, header=None)
        st.write("Raw Data Preview:", df.head())  # Debugging

        # Check if the first row contains valid headers
        if not df.iloc[0].isnull().all():  # Ensure the first row isn't entirely NaN
            df.columns = pd.Index([f"Column_{i}" if pd.isna(name) else name.strip() for i, name in enumerate(df.iloc[0])])
            df = df[1:]  # Remove header row from data
        else:
            df.columns = [f"Column_{i}" for i in range(df.shape[1])]

        # Ensure unique column names
        df.columns = pd.Index([f"{col}_{i}" if df.columns.duplicated()[i] else col for i, col in enumerate(df.columns)])
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# Load Data
df = load_data(DATA_URL)

# Display Data
if not df.empty:
    st.write("DataFrame has", df.shape[0], "rows and", df.shape[1], "columns.")
    st.write("Columns in DataFrame:", df.columns.tolist())
    st.write("DataFrame Preview:", df.head())
else:
    st.warning("The DataFrame is empty. Please check the CSV file.")


