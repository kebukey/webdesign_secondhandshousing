import streamlit as st
import requests
import pandas as pd
from PIL import Image

def load_css(css_file):
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

def app():
    load_css('style/style.css')
    img_house=Image.open('image/房子.png')
    st.subheader('合肥二手房交易数据')
    df=pd.read_csv('链家二手房分区.csv', encoding='utf-8')
    
    with st.container():
        st.image(img_house)
    st.write("###")
    st.write("---")
    st.dataframe(df)