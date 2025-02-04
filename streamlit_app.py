import streamlit as st
import pandas as pd

st.write("""
GAVNA*
""")
 
df_7dte = pd.read_csv("https://www.dropbox.com/scl/fi/wc92bzd29se8wv4rzam7w/gamma_range_summ_result_test_7dte.csv?rlkey=lf4pwojnlwq91jc1cfyhnuwa9&dl=1")
df_7dte['date'] = pd.to_datetime(df_7dte['date'], format='mixed')
df_7dte.index = df_7dte['date']
df_7dte = df_7dte[df_7dte['date'] >= '2025-01-30']
vanna_df_7dte = pd.read_csv('https://www.dropbox.com/scl/fi/c3qd9wv4ltbb3t8neobu1/vanna_range_summ_result_test_7dte.csv?rlkey=y2fngkjtqrjhs4rbs8tu8hhgv&dl=1')
vanna_df_7dte['date'] = pd.to_datetime(vanna_df_7dte['date'], format='mixed')
vanna_df_7dte.index = vanna_df_7dte['date']   
vanna_df_7dte = vanna_df_7dte[vanna_df_7dte['date'] >= '2025-01-30']

full_df = pd.concat([df_7dte["zero"],df_7dte["low"],vanna_df_7dte["maxVanna"],vanna_df_7dte["minVanna"],vanna_df_7dte["zero"]],keys = ["zero","low","vanna_maxVanna","vanna_minVanna","vanna_zero"],axis = 1)

st.line_chart(
    vanna_df_7dte,
    x = 'date',
    y = ["zero","maxVanna","minVanna"],
    color=["#FF0000"],
    width = 2000, height = 1000  # Optional
)
st.line_chart(
    df_7dte,
    x = 'date',
    y = ["zero","low"],
    color=["#FF0000"],
    width = 2000, height = 1000  # Optional
)
