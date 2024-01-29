import pandas as pd
import numpy as np
import json
import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="STHeiti Medium.ttc")
plt.rcParams['font.sans-serif'] = ['Heiti TC']    # 指定默认字体：解决plot不能显示中文问题
plt.rcParams['axes.unicode_minus'] = False           # 解决保存图像是负号'-'显示为方块的问题

df = pd.read_json('./movie_item.json', lines=True)
df = df.dropna()
# print(df)
# print('电影数目：',df.shape[0])
df['movie_id'] = df['movie_id'].apply(lambda x: int(x[0][3:]))
df['comment_num'] = df['comment_num'].apply(lambda x: int(x[2:-1]))
df['question_num'] = df['question_num'].apply(lambda x: int(x[2:-1]))
df['rating_num'] = df['rating_num'].apply(lambda x: float(x[0]))
df['rating_per_stars1'] = df['rating_per_stars1'].apply(lambda x: float(x[:-1]))
df['rating_per_stars2'] = df['rating_per_stars2'].apply(lambda x: float(x[:-1]))
df['rating_per_stars3'] = df['rating_per_stars3'].apply(lambda x: float(x[:-1]))
df['rating_per_stars4'] = df['rating_per_stars4'].apply(lambda x: float(x[:-1]))
df['rating_per_stars5'] = df['rating_per_stars5'].apply(lambda x: float(x[:-1]))
df['release_date'] = df['release_date'].apply(lambda x: int(x[0][1:-1]))
df['vote_num'] = df['vote_num'].apply(lambda x: int(x[0]))
df['movie_title'] = df['movie_title'].apply(lambda x: (x[0]))
pattern = '\d+'
import re
df['runtime'] = df['runtime'].apply(lambda x: (x[0]))
df['runtime'] = df['runtime'].str.findall(pattern,flags=re.IGNORECASE).apply(lambda x: int(x[0]))
#print(df['runtime'].max(),df['runtime'].min(),df['runtime'].mean())
'''
print(df['rating_per_stars1'].describe())
print(df['rating_per_stars2'].describe())
print(df['rating_per_stars3'].describe())
print(df['rating_per_stars4'].describe())
print(df['rating_per_stars5'].describe())
# print(df.info())

# print(df.sort_values('rating_num', ascending=False)[['movie_title', 'rating_num']].head(10))
# df.to_csv('data.csv', encoding='utf_8_sig')
'''
def deal_data():
    fig_path='./1.png'
    sns.set(font_scale=0.7)
    scatter_fig = sns.jointplot(x="comment_num", y="vote_num", data=df, kind='reg')
    #scatter_fig.ax_joint.set_xlabel('评论数')
    scatter_fig.set_axis_labels('评论人数', '评分人数', fontproperties=my_font, fontweight='bold',fontsize='14')

    #scatter_fig.savefig(fig_path, dpi=400)
    plt.show()
def draw1():
    fig_path = './2.png'
    sns.kdeplot(df.rating_per_stars5, bw=2, label="5星的比例", cut=1)
    sns.kdeplot(df.rating_per_stars4, bw=2, label="4星的比例", cut=1)
    sns.kdeplot(df.rating_per_stars3, bw=2, label="3星的比例", cut=1)
    sns.kdeplot(df.rating_per_stars2, bw=2, label="2星的比例", cut=1)
    sns.kdeplot(df.rating_per_stars1, bw=2, label="1星的比例", cut=1)
    plt.yscale('log')
    plt.title('1-5星占比', fontproperties=my_font)
    plt.xlabel('每种评星级别的比例', fontproperties=my_font)
    plt.ylabel('密度', fontproperties=my_font)
    plt.legend(prop=my_font)
    plt.show()
def draw2():
    sns.set(font_scale=0.7)
    scatter_fig = sns.jointplot(x="comment_num", y="rating_num", data=df, kind='reg')
    #scatter_fig.ax_joint.set_xlabel('评论数')
    scatter_fig.set_axis_labels('评论人数', '评分', fontproperties=my_font, fontweight='bold',fontsize='14')

    #scatter_fig.savefig(fig_path, dpi=400)
    plt.show()

def draw3():
    sns.set(font_scale=1)
    sns.histplot(x="runtime", data=df, bins=10)
    plt.xlabel('电影时长', fontproperties=my_font, fontsize=15)
    plt.ylabel('电影数量', fontproperties=my_font, fontsize=15)
    plt.show()
if __name__ == '__main__':
    #deal_data()
    # draw1()
    #draw2() # 分析评分与评论人数的关系
    draw3() # 条形图：分析电影时常分布、电影时常和评分的关系
    print("do nothing")

