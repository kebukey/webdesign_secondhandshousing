import streamlit as st
import requests
import pandas as pd
from PIL import Image

def load_css(css_file):
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
 
def research_houseprice(市区,户型,面积,朝向,装修,楼层,建成年份,楼型):
    a=[x for x in [市区,户型,面积,朝向,装修,楼层,建成年份,楼型]]
    df=pd.read_csv('train2.csv', encoding='utf-8') 
    prediction1=df[df.市区 ==a[0]][df.户型 ==a[1]][df.面积 ==a[2]][df.朝向 ==a[3]][df.装修 ==a[4]][df.楼层 ==a[5]][df.建成年份 ==a[6]][df.楼型 ==a[7]]['总价'].values
    return prediction1
       
 
def app():
    load_css('style/style.css')
    
    html_temp="""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">二手房价格查询</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.write("---")
    st.write("###")
    html_temp1="""
    <br></br>
    <br></br>
    """
    市区 = st.number_input("市区",min_value=0,format="%d")
    户型 = st.number_input("户型",min_value=0,format="%d")
    朝向 = st.number_input("朝向" ,min_value=0,format="%d")
    装修 = st.number_input("装修",min_value=0,format="%d")
    楼层 = st.number_input("楼层",min_value=0,format="%d")
    建成年份 = st.number_input("建成年份",min_value=0,format="%d")
    楼型 = st.number_input("楼型",min_value=0,format="%d")
    面积 = st.number_input("面积",format="%f")
    result1=""
    if st.button("查询"):
        result1=research_houseprice(市区,户型,面积,朝向,装修,楼层,建成年份,楼型)
    st.success('二手房价格：{}'.format(result1))