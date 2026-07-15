import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# 1. Konfigurasi Koneksi Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
CREDS = Credentials.from_service_account_file('kunci.json', scopes=SCOPES)
GC = gspread.authorize(CREDS)
SHEET = GC.open('Data_Dropping_2026').sheet1

# 2. Fungsi Ambil Data
def load_data():
    data = SHEET.get_all_records()
    return pd.DataFrame(data)

# 3. Tampilan Web
st.set_page_config(page_title="Dashboard Dropping Air", layout="wide")
st.title("🚰 Monitoring Dropping Air Bersih")

df = load_data()
st.dataframe(df) # Menampilkan tabel di web

# 4. Input Form (untuk tambah data)
with st.form("input_form"):
    tgl = st.date_input("Tanggal")
    lokasi = st.text_input("Desa")
    vol = st.number_input("Volume (Liter)")
    submit = st.form_submit_button("Kirim Data")
    
    if submit:
        SHEET.append_row([str(tgl), "", "", "", lokasi, "", "", vol, "", ""])
        st.success("Data berhasil ditambahkan!")