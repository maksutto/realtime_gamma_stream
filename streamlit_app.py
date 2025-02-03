import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("https://www.dropbox.com/scl/fi/wc92bzd29se8wv4rzam7w/gamma_range_summ_result_test_7dte.csv?rlkey=lf4pwojnlwq91jc1cfyhnuwa9&dl=1")
st.line_chart(df)
