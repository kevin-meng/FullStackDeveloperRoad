import streamlit as st
import pandas as pd
import requests


st.title("文章简介")


num = st.selectbox("请选择一个帖子", [1, 2, 3, 4, 5])
# 测试使用接口
url = f'http://jsonplaceholder.typicode.com/posts/{num}'

if st.button("点击获取"):
    response = requests.get(url)

    if response.status_code == 200:
        # st.write('请求成功')
        data = response.json()
        # st.write(data)
        # 数据展示
        st.write("---")
        st.write(f"#### {data['title']}")
        st.write(f"{data['body']}")

    else:
        st.write(f'请求失败，状态码：{response.status_code}')




