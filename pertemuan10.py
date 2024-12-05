import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf

st.title("Pertemuan 10: Interaksi Streamlit dan Yahoo Finance")
st.write("# Pendahuluan")

kamus_ticker = {
    'GOOGL' : 'Google',
    'AAPL' : 'Apple',
    'SBUX' : 'Starbucks',
    'MCD' : 'McDonald',
    'BBNI' : 'Bank Negara Indonesia (Persero) Tbk. PT',
    'BMRI' : 'Bank Mandiri (Persero) Tbk. PT',
    'BBRI' : 'Bank Rakyat Indonesia (Persero) Tbk. PT'
}
tickerSymbol = st.selectbox(
    'Silakan pilih kode perusahaan:',
    kamus_ticker.keys()
)
st.write(f'{kamus_ticker.keys()}')

st.write(f'Harga saham {kamus_ticker[tickerSymbol]}.')

tickerData = yf.Ticker(tickerSymbol)
pilihan_periode = st.selectbox(
    'Pilih periode:',
    ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y']
)
tickerData = yf.Ticker(tickerSymbol)
tickerDF = tickerData.history(
    period='1d',
    start='2024-10-01',
    end='2024-11-06'
)
flag_tampil = st.checkbox('Tampilkan tabel')
if flag_tampil:
    st.write(tickerDF.head(10))
flag_grafik = st.checkbox('Tampilkan grafik')
st.multiselect(
    'Silakan pilih atribut yang akan ditampilkan:',
    ['Low', 'High', 'Open', 'Close', 'Volume']
)
grafik = px.line(
    tickerDF,
    title=f'Harga Saham {tickerSymbol}',
    y = [
        'Low',
        'High',
        'Open',
        'Close',
        'Volume'
    ]
  )
st.plotly_chart(grafik)

