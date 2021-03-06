import streamlit as st
from st_aggrid import AgGrid

import pandas as pd
from gsheetsdb import connect
from google.oauth2 import service_account
import pygsheets

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

@st.cache
def make_df(secrets):
    rows = conn.execute(f'SELECT * FROM "{secrets}"')
    df_gsheet = pd.DataFrame(rows)
    return df_gsheet

spreadsheet_id = '1jmRQJC4wQtSny-JTA3KLJ4BeVFdYU3qQanZerh_5IEU'

# @st.cache
# def make_df2():
#     # gc = pygsheets.authorize(service_account_file= st.secrets["service_file_path"])
#     # gc = pygsheets.authorize(service_account_file= 'gsheet-key.json')
#     gc = pygsheets.authorize(custom_credentials= credentials)
#     sh = gc.open_by_key(spreadsheet_id)
#     sheetname = 'Daily ARKK data'
#     worksheet1 = sh.worksheet(property= 'title', value= sheetname) 
#     df2 = worksheet1.get_as_df()
#     return df2

# @st.cache( hash_funcs={_thread.RLock: lambda: None} )
def make_df2(spreadsheet_id, sheetname):
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
            ],
    )
    gc = pygsheets.authorize(custom_credentials= credentials)
    sh = gc.open_by_key(spreadsheet_id)
    worksheet = sh.worksheet(property= 'title', value= sheetname)
    df = worksheet.get_as_df()
    return df
    
st.markdown("""
# Connect to Google Sheets
[Link to original Gsheet](https://docs.google.com/spreadsheets/d/1jmRQJC4wQtSny-JTA3KLJ4BeVFdYU3qQanZerh_5IEU)
## ARK Daily Data
""")
sheet_url = st.secrets["private_gsheets_url"]
rows = conn.execute(f'SELECT * FROM "{sheet_url}"')
df_gsheet = pd.DataFrame(rows)
# st.write(df_gsheet)
AgGrid(df_gsheet)

# st.subheader('ARKK data')
arkk = st.secrets['arkk_data']
arkk_df = make_df(arkk)
# st.write(arkk_df)
st.subheader('ARKK data (AgGrid)')
AgGrid(arkk_df)

st.subheader('ARKG data')
arkg = st.secrets['arkg_data']
arkg_df = make_df(arkg)
# st.write(arkg_df)
AgGrid(arkg_df)

st.subheader('ARKF data')
arkf = st.secrets['arkf_data']
arkf_df = make_df(arkf)
# st.write(arkf_df)
AgGrid(arkf_df)

st.subheader('ARKQ data')
arkq = st.secrets['arkq_data']
arkq_df = make_df(arkq)
# st.write(arkq_df)
AgGrid(arkq_df)

st.subheader('ARKW data')
arkw = st.secrets['arkw_data']
arkw_df = make_df(arkw)
# st.write(arkw_df)
AgGrid(arkw_df)

st.subheader('ARKX data')
arkx = st.secrets['arkx_data']
arkx_df = make_df(arkx)
# st.write(arkx_df)
AgGrid(arkx_df)

st.subheader('CTRU data')
ctru = st.secrets['ctru_data']
ctru_df = make_df(ctru)
# st.write(ctru_df)
AgGrid(ctru_df)

st.subheader('PRNT data')
prnt = st.secrets['prnt_data']
prnt_df = make_df(prnt)
# st.write(prnt_df)
AgGrid(prnt_df)

st.subheader('IZRL data')
izrl = st.secrets['izrl_data']
izrl_df = make_df(izrl)
# st.write(izrl_df)
AgGrid(izrl_df)

st.subheader('Label data')
labels = st.secrets['labels']
labels_df = make_df(labels)
# st.write(labels_df)
AgGrid(labels_df)

st.subheader('Labels (in-depth) data')
labels2_df = make_df2(spreadsheet_id, 'ARK portfolio labels (in-depth)')
# st.write(labels_df)
AgGrid(labels2_df)

st.subheader('Test Pygsheets')
pgs_df = make_df2(spreadsheet_id, 'Daily ARKG data')
test = pgs_df.astype(str)
# st.write(test)
AgGrid(test)
st.subheader('Test Pygsheets ( without astype(str) )')
AgGrid(pgs_df)
