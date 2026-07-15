import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Mengambil kredensial dari Streamlit Secrets
creds_dict = st.secrets["gcp_service_account"]

# Konfigurasi Koneksi Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
CREDS = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
GC = gspread.authorize(CREDS)
SHEET = GC.open('Data_Dropping_2026').sheet1
