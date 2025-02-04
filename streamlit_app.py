import streamlit as st
import pandas as pd
import yfinance
st.write("""
GAVNA*
""")
 
df_7dte = pd.read_csv("https://www.dropbox.com/scl/fi/wc92bzd29se8wv4rzam7w/gamma_range_summ_result_test_7dte.csv?rlkey=lf4pwojnlwq91jc1cfyhnuwa9&dl=1")
df_7dte['date'] = pd.to_datetime(df_7dte['date'], format='mixed')
# df.index = df['date']
# st.line_chart(df['zero'],width = 1000, height = 1000)
st.line_chart(
    df_7dte,
    x = 'date',
    y = ["zero", "low"],
    color=["#FF0000", "#0000FF"],
    width = 2000, height = 1000  # Optional
)
