import pandas as pd
import streamlit as st

st.title("Auto" ,text_alignment="center")

lst = [1,2,3,4,5,6,7,8,9,10 , 11,12,13, 14 ,15 ,16]

df = pd.DataFrame([[0 for _ in range(3)] for _ in range(16)], columns=["Input1", "Input2", "Input3"])

df["Input2"] = ["autonomy",2,3,4,5,6,7,8,9,10 , 11,12,13, 14 ,15 ,16]

st.header("6x3 Input Table",text_alignment= "center")

st.markdown( """
<style>
    thead tr th {
        text-align : center !important;
        font-weight: bold !important;
    }
    tbody tr th {
        text-align : center !important;
        font-weight: bold !important;
    }
    tbody tr td{
        text-align : center !important;
        font-weight: bold !important;
    }
</style>
    """ , unsafe_allow_html=True)

value = st.slider("Select decoder value", 0, 15)

if st.button("find the faulty"):

    for i in range(len(df)):
        if i == value:
            df.iloc[i,2] = 1
        else:
            df.iloc[i,2] = 0

st.table(df)