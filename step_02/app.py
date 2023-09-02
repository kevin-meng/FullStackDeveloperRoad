import os
import requests

import streamlit as st
import pandas as pd

from db import create_database, insert_data, query_data_by_adcode
from api import query_data_by_url

# 缓存数据提高访问速度
@st.cache()
def load_city_adcode():
    df = pd.read_excel("./data/AMap_adcode_citycode_20210406.xlsx")
    cities = df['中文名'].unique().tolist()
    adcode_dict = df.set_index('中文名')['adcode'].to_dict()
    return cities, adcode_dict


st.title("天气查询")
if not os.path.exists("./data/data.db"):
    create_database()

today = pd.datetime.now().strftime("%Y-%m-%d")
st.write(today)


cities, adcode_dict = load_city_adcode()
city = st.selectbox("请输入城市", cities[1:])
adcode = adcode_dict[city]


if st.button("点击查询"):
    # 查询数据库
    out = query_data_by_adcode(adcode,today)
    print(out)
    if len(out)!= 0:
        st.write("查询数据库")
        st.write(out)
    else:
        st.write("查询接口")
        # 查询接口
        out = query_data_by_url(adcode)
        if len(out)!= 0:
            st.write(out)
            # 插入数据库
            st.write("插入数据库")
            insert_data(out)

    # 美化 页面
    st.write("---")
    st.info(f"**{out['province']} - {out['city']}**")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("温度(℃)", f"{out['temperature']} ")
    col2.metric("天气", out['weather'])
    col3.metric("风向", f"{out['winddirection']} ")
    col4.metric("风速", f"{out['windpower']} ")

    st.write("---")


