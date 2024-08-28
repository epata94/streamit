# -*- coding:utf-8 -*-
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import matplotlib.font_manager as fm  # 폰트 관련 용도 as fm


def unique(list):
    x = np.array(list)
    return np.unique(x)


@st.cache_data
def fontRegistered():
    font_dirs = [os.getcwd() + '/customFonts']
    font_files = fm.findSystemFonts(fontpaths=font_dirs)

    for font_file in font_files:
        fm.fontManager.addfont(font_file)
    fm._load_fontmanager(try_read_cache=False)


def main():
    fontRegistered()
    fontNames = [f.name for f in fm.fontManager.ttflist]

    # Default font 설정
    if 'KoreanSNMB' in fontNames:
        default_font = 'KoreanSNMB'
    else:
        default_font = fontNames[0]  # 폰트가 없을 경우 첫번째 폰트 선택

    fontname = st.selectbox("폰트 선택", unique(fontNames), index=fontNames.index(default_font))

    plt.rc('font', family=fontname)
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots()
    sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day')
    ax.set_title("한글 테스트")
    st.pyplot(fig)

    st.dataframe(tips)


if __name__ == "__main__":
    main()
