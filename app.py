import streamlit as st
from multipage import MultiPage
from pages import home,gross_data,predict,research,visualization

st.set_page_config(page_title='二手房交易网站',page_icon='tiger:',layout='wide')
st.title('二手房信息系统')


app=MultiPage()

app.add_page('Home',home.app)
app.add_page('查看以往数据',gross_data.app)
app.add_page('预测房价',predict.app)
app.add_page('查询房价',research.app)
app.add_page('图表展示',visualization.app)


if __name__=='__main__':
    app.run()
