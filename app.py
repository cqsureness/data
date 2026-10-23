import streamlit as st

st.set_page_config(page_title="经济研究数据导航", layout="wide")
st.title("📊 宏观数据、产业数据、企业数据、金融数据、科技数据、三农数据 & 工业机器人研究 - 数据导航")
st.markdown("> 用于定期下载：UNIDO工业统计、IFR工业机器人、世界银行等数据库，点击跳转官网")

# 整理你研究要用的数据源
data_source_list = [
    {
        "name": "期刊数据库入口",
        "url": "https://lib.swu.edu.cn/libweb/digitalDatabase/",
        "desc": "CNKI,EBSCO,Elsevier, Web of Science, Wiley",
        "note": "各类主要期刊数据库"
    },    
    {
        "name": "tushare（实时金融数据）",
        "url": "https://tushare.pro/",
        "desc": "中国上市公司财务报表数据、价格数据、指标数据等",
        "note": "上市公司年度、月度、每日指标"
    },
    {
        "name": "CSMAR（金融研究数据）",
        "url": "https://data.csmar.com/",
        "desc": "中国宏观经济、产业经济和企业微观数据平台",
        "note": "国内年度、月度工业指标"
    },    
    {
        "name": "EPS数据平台",
        "url": "https://olap.epsnet.com.cn/",
        "desc": "中国社会经济研究基础平台：农业数据、三农数据、科技数据、旅游数据、",
        "note": "免费摘要，细分面板可校内图书馆采购权限导出"
    },    
    {
        "name": "国家统计局（国内工业数据）",
        "url": "https://data.stats.gov.cn/",
        "desc": "中国工业分行业产值、就业、固定资产投资",
        "note": "国内年度、月度工业指标"
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
        "desc": "经济合作组织中国家的细分产业、资本投入、劳动数据，适合对比",
        "note": "大部分指标免费"
    },

    {
        "name": "ADB MRIO（亚洲开发银行多区域投入产出）",
        "url": "https://data.adb.org/",
        "desc": "亚行数据库是亚行所有公共数据门户。",
        "note": "国年度、月度数据指标"
    }
    
    
    
    
]

# ========== 三列布局核心代码 ==========
# 每一行生成3张卡片，自动换行
for i in range(0, len(data_source_list), 3):
    # 创建一行三列，宽度均等
    cols = st.columns(3, vertical_alignment="top")
    # 遍历当前行的3个位置
    for j in range(3):
        idx = i + j
        if idx < len(data_source_list):
            item = data_source_list[idx]
            with cols[j]:
                with st.container(border=True):
                    # 卡片内部依然保持文字+按钮两栏布局
                    col_text, col_btn = st.columns([0.75, 0.25])
                    with col_text:
                        st.subheader(item["name"])
                        st.write(item["desc"])
                        st.caption(f"备注：{item['note']}")
                    with col_btn:
                        st.link_button("🔗 前往官网下载", item["url"], type="primary")

st.divider()
st.subheader("📌 配套辅助表（你后面会用到）")
st.markdown("- IFR行业 ↔ UNIDO ISIC Rev.4 行业匹配对照表（本地Excel）")
st.markdown("- 指标清单：固定资本形成GFCF、机器人密度、增加值、就业、出口")
