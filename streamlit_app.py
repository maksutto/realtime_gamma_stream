import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("https://www.dropbox.com/scl/fi/wc92bzd29se8wv4rzam7w/gamma_range_summ_result_test_7dte.csv?rlkey=lf4pwojnlwq91jc1cfyhnuwa9&dl=1")
df['date'] = pd.to_datetime(df['date'], format='mixed')
# df.index = df['date']
# st.line_chart(df['zero'],width = 1000, height = 1000)
st.line_chart(
    df,
    x = df['date'],
    y = ["zero", "low"],
    color=["#FF0000", "#0000FF"],
    width = 1000, height = 1000  # Optional
)
