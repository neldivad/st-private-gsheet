import streamlit as st
import pandas as pd
from gsheetsdb import connect

st.title("Try to connect to private google sheet")
df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
st.write(df)

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

st.title("Connect to Google Sheets")
sheet_url = st.secrets["private_gsheets_url"]
rows = conn.execute(f'SELECT * FROM "{sheet_url}"')
df_gsheet = pd.DataFrame(rows)
st.write(df_gsheet)
