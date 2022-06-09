
import streamlit as st
import requests
#from streamlit_lottie import st_lottie
from PIL import Image


def load_php(css_file):
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

def app():
    #st.write('# Home')#这个#好像是一级标题的意思
    load_php('style/style.php')
   # lottie_coding=load_lottie("https://assets8.lottiefiles.com/packages/1f20_zzytykf2.json")
    img_second_housing=Image.open('image/二手房.jpg')
    img_forest=Image.open('image/随机森林.png')
   # img_comparision=Image.open('image/对比.png')
    img_tree=Image.open('image/决策树图.png')
    img_K=Image.open('image/K近邻图.png')
    
    
    #part1
    with st.container():
        st.subheader('Welcome, this is second-hand housing information system:tiger:')
        st.title('A Brief Web Design')
        st.write(
            "本系统提供了二手房数据的查询，和估价"
            )
        st.write('[Learn More...](https://hf.lianjia.com/ershoufang/)')
        
    #part2
    with st.container():
        st.write("---")
        l_column,r_column=st.columns(2)
        with l_column:
            st.header("What I Do")
            st.write("###")
            st.write(
                """
                On this system, you can easily understand the second-housing market in Hefei:
                - past price preview.
                - predict new prices.
            
                """
                )
        with r_column:
            #st_lottie(lottie_coding,height=300,key='coding')
            #在这里显示二手房照片吧
            st.image(img_second_housing)
    #part 3
    with st.container():
        st.write('---')
        st.header('Evaluation of prediction results.')
        st.write('##')
        image_col,text_col=st.columns((1,1))
        with image_col:
            st.image(img_forest)
        with text_col:
            
            
            st.write("###")
            html_temp1="""
            <br></br>
            <br></br>
            """
            st.markdown(html_temp1,unsafe_allow_html=True)
            st.write(
                """
                - train score:  0.9720580069812336
                - test score:  0.8070697443901073
                - MAE: 35.11
                - MSE: 4113.16
                - RMSE: 64.13
                """
                )
    with st.container():
        image_col,text_col=st.columns((1,1))
        with image_col:
            st.image(img_tree)
        with text_col:
            st.write("###")
            html_temp1="""
            <br></br>
            <br></br>
            """
            st.markdown(html_temp1,unsafe_allow_html=True)
            st.write(
                """
                - train score:  0.6559367132060008
                - test score:  0.5162994552000963
                - MAE: 69.65
                - MSE: 10312.22
                - RMSE: 101.55
                """
                )
    with st.container():
        image_col,text_col=st.columns((1,1))
        with image_col:
            st.image(img_K)
        with text_col:
            st.write("###")
            html_temp1="""
            <br></br>
            <br></br>
            """
            st.markdown(html_temp1,unsafe_allow_html=True)
            st.write(
                """
                - train score:  0.7335588640709738
                - test score:  0.5607642251542704
                - MAE: 61.85
                - MSE: 9364.26
                - RMSE: 96.77
                """
                )
    #<form action='https://formsubmit.co/YOUR@MAIL.COM' method="POST"
    with st.container():
        st.write('---')
        st.header('Get In Touch With Us')
        st.write("##")
        contact_form="""
                <form action='mailto:1204505037@qq.com' method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="sbumit">Send</button>
                </form>
            """
            
    l_column,r_column=st.columns(2)
    with l_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with r_column:
        st.empty()
     
    
    
