import streamlit as st
import requests
import pandas as pd
from PIL import Image
import numpy as np
#import pickle
import pandas as pd
import numpy as np
import sys
import seaborn as sns
import warnings
import math

from sklearn.metrics import *
from sklearn.linear_model import *
from sklearn.neighbors import *
from sklearn.svm import *
from sklearn.neural_network import *
from sklearn.tree import *
from sklearn.ensemble import *
from xgboost import *
import lightgbm as lgb
import tensorflow as tf
from tensorflow.keras import layers
from sklearn.preprocessing import *
from sklearn.ensemble import RandomForestRegressor as RFR
from sklearn.model_selection import *
# 评价指标函数定义，其中R2的指标可以由模型自身得出，后面的score即为R2




#model_st = pickle.load(open('model.pkl', 'rb'))

warnings.filterwarnings("ignore")



def evaluation(model):
    ypred = model.predict(x_test)
    mae = mean_absolute_error(y_test, ypred)
    mse = mean_squared_error(y_test, ypred)
    rmse = math.sqrt(mse)
    print("MAE: %.2f" % mae)
    print("MSE: %.2f" % mse)
    print("RMSE: %.2f" % rmse)
    return ypred
data1 = pd.read_csv('train2.csv', na_values=np.nan)

# 将数据划分输入和结果集
X = data1[data1.columns[1:]]
y_reg = data1[data1.columns[0]]

# 切分训练集和测试集， random_state是切分数据集的随机种子，要想复现本文的结果，随机种子应该一致
x_train, x_test, y_train, y_test = train_test_split(X, y_reg, test_size=0.3, random_state=42)

#随机森林
model_rfr = RandomForestRegressor(random_state=30)
model_rfr.fit(x_train, y_train)


def predict_houseprice(市区, 户型, 面积, 朝向, 装修, 楼层, 建成年份, 楼型):
    int_features = [x for x in [市区, 户型, 面积, 朝向, 装修, 楼层, 建成年份, 楼型]]
    final_features = [np.array(int_features)]
    prediction = model_rfr.predict(final_features)
    prediction = round(prediction[0], 2)
    return prediction


def app():
    # st.write('# Home')#这个#好像是一级标题的意思
    

    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">二手房价格预测</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    st.write("---")
    st.write("###")
    html_temp1 = """
    <br></br>
    <br></br>
    """
    市区 = st.number_input("市区", min_value=0, format="%d")
    户型 = st.number_input("户型", min_value=0, format="%d")
    朝向 = st.number_input("朝向", min_value=0, format="%d")
    装修 = st.number_input("装修", min_value=0, format="%d")
    楼层 = st.number_input("楼层", min_value=0, format="%d")
    建成年份 = st.number_input("建成年份", min_value=0, format="%d")
    楼型 = st.number_input("楼型", min_value=0, format="%d")
    面积 = st.number_input("面积", format="%.2f")
    # 文本输入用st.text_input,输入的是str类型
    result = ""
    if st.button("Predict"):
        result = predict_houseprice(市区, 户型, 面积, 朝向, 装修, 楼层, 建成年份, 楼型)
    st.success('二手房价格：{}'.format(result))
