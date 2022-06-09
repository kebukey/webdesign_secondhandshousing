import streamlit as st
import requests
import pandas as pd
from PIL import Image



def app():
    
    img_house=Image.open('image/房子.png')
    st.subheader('合肥二手房交易数据')
    df=pd.read_csv('链家二手房分区.csv', encoding='utf-8')
    
    with st.container():
        st.image(img_house)
    st.write("###")
    st.write("---")
    st.dataframe(df)
