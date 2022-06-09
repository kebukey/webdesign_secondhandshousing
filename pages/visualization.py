from pyg2plot import Plot
import io
import streamlit.components.v1 as components
import streamlit as st
import pandas as pd
from PIL import Image

#img_house=Image.open('image/小图标.png')只可以用在首页py上，如app.py
#st.set_page_config(page_title="合肥二手房数据图表展示",page_icon="image/小图标.png",layout="wide")
  
def generate_html_target(target):
    return io.StringIO(target.render_html()).read()

#file=st.file_uploder

def app():
    df=pd.read_csv('train2.csv', encoding='utf-8')
    df=df.head(10)
    columns=df.columns
    s2_choose=st.selectbox("请选择一种数据",columns[1:])
    s1=df['总价'].values.tolist()
    s2=df[s2_choose].values.tolist()
    data=[]
    for i in range(df.shape[0]):
        data.append({"总价":str(s1[i]),s2_choose:s2[i]})
    line=Plot('line')
    line.set_options({
        "label":{},
        "data":data,
        "xField":"总价",
        "yField":s2_choose,
        "smooth":False,
        })
    line_target=generate_html_target(line)
    
    #柱状图
    column = Plot("Column")
    column.set_options({
    "label":{},
    "data": data,
    "xField": "总价",
    "yField": s2_choose,
    "seriesField": "总价",
    "columnStyle": {
        "radius": [20, 20, 0, 0],
      },
    "slider": {
        "start": 0.0,
        "end": 1.0,
      },
    })

    column_target = generate_html_target(column)

    #条形图
    bar = Plot("Bar")
    bar.set_options({
    "label":{},
    "data": data,
    "xField": s2_choose,
    "yField": "总价",
    "seriesField": "总价",
    "legend": {
        "position": 'bottom',
      },
    "slider": {
        "start": 0.0,
        "end": 1.0,
      },
    })

    bar_target = generate_html_target(bar)


    pie = Plot("Pie")
    pie.set_options({
    "label":{},
    "data": data,
    "angleField": s2_choose,
    "colorField": '总价',
    "radius": 1,
    "innerRadius": 0.5,
    })
    pie_target = generate_html_target(pie)

    rose = Plot("Rose")
    rose.set_options({
    "label":{},
    "data": data,
    "xField": "总价",
    "yField": s2_choose,
    "seriesField": "总价",
      "radius": 0.9,
      #设置 active 状态样式
      "state": {
        "active": {
          "style": {
            "lineWidth": 0,
            "fillOpacity": 0.65,
          },
        },
      },
      "legend": {
        "position": 'bottom',
      },
      "interactions": [{ "type": 'element-active' }]
    })
    rose_target = generate_html_target(rose)

    area = Plot("Area")
    area.set_options({
    "label":{},
    "data": data,
    "xField": "总价",
    "yField": s2_choose,
    "areaStyle": {
          "fill": 'l(270) 0:#ffffff 0.5:#7ec2f3 1:#1890ff',
        },
    "slider": {
        "start": 0.1,
        "end": 0.9,
        "trendCfg": {
          "isArea": True,
        },
      },
    "annotations": [
        {
          "type": 'text',
          "position": ['min', 'median'],
          "content": '中位数',
          "offsetY": 0,
          "style": {
            "textBaseline": 'bottom',
          },
        },
        {
          "type": 'line',
          "start": ['min', 'median'],
          "end": ['max', 'median'],
          "style": {
            "stroke": 'red',
            "lineDash": [2, 2],
          },
        },
      ],

    })
    area_target = generate_html_target(area)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("总价与"+s2_choose+"关系折线图")
        components.html(line_target, height=300)
        components.html("<br>", height=20)
        st.subheader("总价与"+s2_choose+"关系玫瑰图")
        components.html(rose_target, height=400)
    with c2:
        st.subheader("总价与"+s2_choose+"关系柱状图")
        components.html(column_target, height=300)
        components.html("<br>", height=20)
        st.subheader("总价与"+s2_choose+"关系条形图")
        components.html(bar_target, height=300)
    with c3:
        st.subheader("总价与"+s2_choose+"关系饼图")
        components.html(pie_target, height=300)
        components.html("<br>", height=20)
        st.subheader("总价与"+s2_choose+"关系面积图")
        components.html(area_target, height=300)
    




