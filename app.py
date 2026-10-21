# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:28:09 2026

@author: WSAQ
"""

import streamlit as st

st.set_page_config(page_title="产业研究数据导航台", layout="wide")
st.title("📊 金融数据、宏观数据、产业数据 & 工业机器人研究 - 数据导航")
st.markdown("> 用于定期下载：UNIDO工业统计、IFR工业机器人、世界银行等数据库，点击跳转官网")

# 整理你研究要用的数据源
data_source_list = [
    
    {
        "name": "tushare（实时金融数据）",
        "url": "https://tushare.pro/",
        "desc": "中国上市公司财务报表数据、价格数据、指标数据等",
        "note": "上市公司年度、月度、每日指标"
    },    
    {
        "name": "UNIDO 工业统计数据库",
        "url": "https://stat.unido.org/",
        "desc": "INDSTAT / IDSB / CIP / SDG9；增加值、就业、固定资本形成、进出口（ISIC Rev.4）",
        "note": "免费摘要，细分面板可校内图书馆采购权限导出"
    },
    {
        "name": "IFR 国际机器人联合会",
        "url": "https://ifr.org/",
        "desc": "工业机器人装机量、存量、机器人密度、分行业数据",
        "note": "免费只有年度摘要报告；细分分行业Premium库付费"
    },
    {
        "name": "世界银行公开数据 World Bank",
        "url": "https://data.worldbank.org/",
        "desc": "各国宏观控制变量：人均GDP、制造业占比、开放度等",
        "note": "全部免费公开"
    },
    {
        "name": "OECD 产业统计",
        "url": "https://stats.oecd.org/",
        "desc": "发达国家细分产业、资本投入、劳动数据，适合对比",
        "note": "大部分指标免费"
    },
    {
        "name": "国家统计局（国内工业数据）",
        "url": "https://data.stats.gov.cn/",
        "desc": "中国工业分行业产值、就业、固定资产投资",
        "note": "国内年度、月度工业指标"
    }

]

# 循环渲染每一行
for item in data_source_list:
    with st.container(border=True):
        col1, col2 = st.columns([0.75, 0.25])
        with col1:
            st.subheader(item["name"])
            st.write(item["desc"])
            st.caption(f"备注：{item['note']}")
        with col2:
            # 跳转按钮，新标签页打开官网
            st.link_button("🔗 前往官网下载", item["url"], type="primary")

st.divider()
st.subheader("📌 配套辅助表（你后面会用到）")
st.markdown("- IFR行业 ↔ UNIDO ISIC Rev.4 行业匹配对照表（本地Excel）")
st.markdown("- 指标清单：固定资本形成GFCF、机器人密度、增加值、就业、出口")
