import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# 1. Konfigurasi Koneksi Google Sheets dari Secrets
@st.cache_resource
def get_connection():
    creds_dict = st.secrets["gcp_service_account"]
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    CREDS = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
    GC = gspread.authorize(CREDS)
    return GC

GC = get_connection()
SHEET = GC.open('Data_Dropping_2026').sheet1

# 2. Fungsi Ambil Data
def load_data():
    data = SHEET.get_all_records()
    return pd.DataFrame(data)

# 3. Tampilan Web
st.set_page_config(page_title="Dashboard Dropping Air", layout="wide")
st.title("🚰 Monitoring Dropping Air Bersih")

try:
    df = load_data()
    st.dataframe(df)
except Exception as e:
    st.error(f"Gagal mengambil data: {e}")
