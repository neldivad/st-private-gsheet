#-----------------------
#
#-----------------------
def df_from_gsheet(spreadsheet_id, sheetname):
  import pygsheets
  
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
