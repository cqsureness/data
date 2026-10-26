import streamlit as st
import json as _json
import os as _os
from urllib.request import urlopen, Request as _Req
from urllib.error import URLError, HTTPError

st.set_page_config(page_title="经济研究数据导航", layout="wide")
st.title("📊 宏观数据、产业数据、企业数据、金融数据、科技数据、三农数据 - 数据导航")
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
    },

    {
        "name": "cnopendata（中国开放数据平台）",
        "url": "https://www.cnopendata.com/",
        "desc": "覆盖经济、金融、会计。",
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

# ========== 右下角访问量统计 ==========
# 计数语义：每次「新会话」(约等于一次浏览器访问) 计入一次，避免 Streamlit 脚本
# 重跑导致重复 +1。在线计数器优先，失败回退到本地文件(仅兜底，Streamlit Cloud
# 的文件系统不持久，真实计数以在线服务为准)。
_COUNTER_NS = "economic-data-nav"
_COUNTER_KEY = "home-visits"


def _get_visit_count():
    """每个会话只调用一次：先试在线计数器，失败回退本地文件计数。"""
    if "visit_count" in st.session_state:
        return st.session_state.visit_count

    count = None
    # 1) 在线计数器 CountAPI（无需密钥，按 命名空间/键 自动建表并 +1）
    try:
        url = f"https://api.countapi.xyz/hit/{_COUNTER_NS}/{_COUNTER_KEY}"
        req = _Req(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=6) as resp:
            data = _json.loads(resp.read().decode("utf-8"))
        count = int(data.get("value", 0))
    except Exception:
        count = None

    # 2) 回退：本地文件计数（Streamlit Cloud 不持久，仅作兜底）
    if count is None:
        try:
            path = _os.path.join(_os.path.dirname(__file__), "visit_count.json")
            if _os.path.exists(path):
                with open(path, encoding="utf-8") as f:
                    count = _json.load(f).get("count", 0)
            else:
                count = 0
            count += 1
            with open(path, "w", encoding="utf-8") as f:
                _json.dump({"count": count}, f)
        except Exception:
            count = None

    st.session_state.visit_count = count
    return count


def render_visit_counter():
    count = _get_visit_count()
    if count is None:
        return
    st.markdown(
        f"""
        <style>
        .wb-visit-counter {{
            position: fixed;
            right: 14px;
            bottom: 14px;
            z-index: 9999;
            background: rgba(255, 255, 255, 0.95);
            color: #444;
            border: 1px solid #e3e3e3;
            border-radius: 999px;
            padding: 5px 14px;
            font-size: 13px;
            line-height: 1.4;
            box-shadow: 0 1px 6px rgba(0, 0, 0, 0.10);
            font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif;
        }}
        </style>
        <div class="wb-visit-counter">👀 访问量 <b>{count}</b></div>
        """,
        unsafe_allow_html=True,
    )


render_visit_counter()
