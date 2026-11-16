import streamlit as st
import pandas as pd
import numpy as np 
import yfinance as yf

tickers = ['IVV', 'ILF', 'SOXX'] #SP500, LATAM, SEMICONDUCTORES
vector_w = [0.5, 0.3, 0.2]
vector_w = np.array(vector_w).reshape(-1,1)

#========================
#APPPPP
#=========================
st.title(':v')
st.write(':v')
st.multiselect(label='tickers',options=['IVV', 'ILF', 'SOXX'],key='tickers',default='SOXX')
tickers=st.session_state['tickers']
st.write(tickers)
df_prices = yf.download(tickers,start='2024-01-01',end = '2026-09-30')['Close']
df_prices = df_prices[tickers]
st.dataframe(df_prices)