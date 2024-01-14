import streamlit as st
import pandas as pd
import numpy as np

# 关闭全局 Pyplot 使用警告
st.set_option('deprecation.showPyplotGlobalUse', False)

st.sidebar.title('账户爬虫')

# 添加导航链接
page = st.sidebar.radio('目录', ['**账号**', '**视频**', '**评论**'])
# 根据选择的页面显示不同的内容
if page == '**账号**':
    st.header('**人民日报**')
    st.write('**参与、沟通、记录时代。**')
    st.write('粉丝数：**168,017,122**')
    st.write('总获赞数：**12,221,996,400**')
    st.write('视频数：**6,033**')
    # st.write('ip地址：未知')
    data = pd.read_csv('视频链接.csv')
    data['发布时间'] = pd.to_datetime(data['发布时间'], unit='s')
    new_order = ['发布时间', '名称', '点赞数', '评论数', '收藏数', '转发量', '时长']
    data = data[new_order]
    st.dataframe(data)
elif page == '**视频**':
    video_data = pd.read_csv('视频链接.csv')
    st.title('**视频信息**')
    st.write('')
    st.write("视频总数：<span style='color:red'>**6033**</span>", unsafe_allow_html=True)
    st.write("总获赞数：<span style='color:red'>**12221996400**</span>", unsafe_allow_html=True)
    st.subheader(f"**近七百条视频**")
    st.write(f"平均点赞数 **{int(np.mean(video_data['点赞数'])):,}**，最低点赞数 **{min(video_data['点赞数']):,}**，最高点赞数 **{max(video_data['点赞数']):,}**，点赞量中位数 **{int(np.median(video_data['点赞数'])):,}**")
    st.write("更新频率：**一日多更**")
    st.divider()
    st.header('视频名称词云')
    st.image('词云/视频词云.png')
elif page == '**评论**':
    # 在地图上标记多个点，使用大小信息
    st.title('**评论信息**')
    comment = pd.read_csv('评论信息.csv')['评论内容']
    len_comment = []
    for i in comment:
        len_comment.append(len(str(i)))
    emo_comment = pd.read_csv('情绪/情绪值.csv')['emo_num']
    st.write(f'平均每条评论 **{int(np.mean(len_comment)):,}** 字，最少的一条评论有 **{min(len_comment)}** 个字， 字数最多有 **{max(len_comment):,}** 字，字数中位数为 **{int(np.median(len_comment)):,}** 字。')
    st.write(f'评论平均情绪值 **{np.mean(emo_comment):.4f}** ，评论最低情绪值 **{min(emo_comment):.4f}** ， 最高情绪值 **{max(emo_comment):.4f}**，情绪值中位数 **{np.median(emo_comment):.4f}**')
    st.caption('* 这里的情绪值是0～1 之间的情感倾向置信度 (情感极性 0 为消极，1 为积极)')
    tab_a, tab_b, tab_c = st.tabs(['**评论分布图**', '**评论地址柱状图**', '**评论词云**'])
    with tab_a:
        st.header('评论地址分布')
        st.caption('点的大小呈现了人数的多少')
        d = pd.read_csv('位置信息/location.csv')
        st.map(d, size='size', longitude='lon', latitude='lat', zoom=4)
    # 柱状图
    with tab_b:
        st.header('评论ip地址')
        st.bar_chart(d, x="地名", y='人数')
    # 词云
    with tab_c:
        st.header('评论内容词云')
        st.image('词云/评论词云.png')

    st.caption('* 以上评论信息都是人民日报在近期发布视频中的部分评论')


