import requests

# import streamlit as st
# import pandas as pd

# https://zhuanlan.zhihu.com/p/314212747
# 高德 api
# https://lbs.amap.com/api/webservice/guide/api/weatherinfo


def query_data_by_url(adcode):
    KEY = '4ccf8a1be4c87582872c959a3cc79924'
    url = f'https://restapi.amap.com/v3/weather/weatherInfo?city={adcode}&key={KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        # st.write('请求成功')
        data = response.json()

        # 插入数据库
        data = data['lives'][0]
        data['reporttime'] = data['reporttime'].split(" ")[0]
    else:
        # st.write(f'请求失败，状态码：{response.status_code}')
        data = {}

    return data

