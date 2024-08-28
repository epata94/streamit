# -*- coding:utf-8 -*-
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
import urllib.request
import os

def download_font():
    font_url = "https://github.com/naver/nanumfont/blob/master/ttf/NanumGothic.ttf?raw=true"
    font_path = "./NanumGothic.ttf"
    if not os.path.exists(font_path):
        urllib.request.urlretrieve(font_url, font_path)
    return font_path

# 폰트 다운로드 및 설정
font_path = download_font()
font_prop = fm.FontProperties(fname=font_path)
plt.rc('font', family=font_prop.get_name())

def main():
    st.title("Matplotlib와 나눔고딕 한글 폰트 사용 예제")

    # 데이터셋 로드 및 시각화
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots()
    sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day', ax=ax)

    # 한글 제목 설정
    ax.set_title("나눔고딕으로 작성한 그래프 제목", fontproperties=font_prop)

    # 그래프 출력
    st.pyplot(fig)

    # 데이터프레임 출력
    st.dataframe(tips)


if __name__ == "__main__":
    main()
