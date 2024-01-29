import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import collections
from snapshot_phantomjs import snapshot
from pyecharts.render import make_snapshot

plt.rcParams['font.sans-serif'] = ['Heiti TC']    # 指定默认字体：解决plot不能显示中文问题
plt.rcParams['axes.unicode_minus'] = False           # 解决保存图像是负号'-'显示为方块的问题
def data_sort_by_score():
    data = pd.read_csv('豆瓣电影top250.csv')
    df = data.sort_values(by='评分', ascending=True)
    c = (
        Bar()
            .add_xaxis(df['片名'].values.tolist()[-10:])
            .add_yaxis('评分', df['评分'].values.tolist()[-10:])
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title='电影评分'),
            yaxis_opts=opts.AxisOpts(name='片名'),
            xaxis_opts=opts.AxisOpts(name='评分'),
            datazoom_opts=opts.DataZoomOpts(type_='inside'),
        )
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .render('电影评分前十.html')
    )


def data_sort_by_year():
    data = pd.read_csv('豆瓣电影top250.csv')
    year_counts = data['上映年份'].value_counts()
    year_counts.columns = ['上映年份', '数量']
    year_counts = year_counts.sort_index(ascending=False)
    c = (
        Bar()
            .add_xaxis(list(year_counts.index[:10]))
            .add_yaxis('上映数量', year_counts.values.tolist()[:10])
            .set_global_opts(
            title_opts=opts.TitleOpts(title='各年份上映电影数量'),
            yaxis_opts=opts.AxisOpts(name='上映数量'),
            xaxis_opts=opts.AxisOpts(name='上映年份'),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_='inside')], )
            .render('各年份上映电影数量降序.html')
    )

def data_sort_by_judgenumber():
    data = pd.read_csv('豆瓣电影top250.csv')
    df = data.sort_values(by='评价人数', ascending=True)
    c = (
        Bar()
            .add_xaxis(df['片名'].values.tolist()[-10:])
            .add_yaxis('评价人数', df['评价人数'].values.tolist()[-10:])
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title='电影评价人数'),
            yaxis_opts=opts.AxisOpts(name='片名'),
            xaxis_opts=opts.AxisOpts(name='人数'),
            datazoom_opts=opts.DataZoomOpts(type_='inside'),
        )
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .render('电影评价人数前十.html')
    )

def data_sort_by_country():
    data = pd.read_csv('豆瓣电影top250.csv')
    country_counts = data['国家/地区'].value_counts()
    country_counts.columns = ['国家/地区', '数量']
    country_counts = country_counts.sort_values(ascending=True)
    c = (
        Bar()
            .add_xaxis(list(country_counts.index))
            .add_yaxis('地区上映数量', country_counts.values.tolist())
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title='地区上映电影数量'),
            yaxis_opts=opts.AxisOpts(name='国家/地区'),
            xaxis_opts=opts.AxisOpts(name='上映数量'),
        )
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .render('各地区上映电影数量.html')
    )


def data_sort_by_director():
    data = pd.read_csv('new.csv')
    country_counts = data['导演'].value_counts()
    country_counts.columns = ['导演', '数量']
    country_counts = country_counts.sort_values(ascending=False)
    c = (
        Bar()
            .add_xaxis(list(country_counts.index[:10]))
            .add_yaxis('电影数量', country_counts.values.tolist()[:10])
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title='电影数量'),
            yaxis_opts=opts.AxisOpts(name='导演', axislabel_opts={"rotate":45}),
            xaxis_opts=opts.AxisOpts(name='电影数量'),

            )
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .render('各导演指导电影数量.html')
    )


def data_sort_by_director1():
    data = pd.read_csv('new.csv')
    data_list = []
    for value in data['导演']:
        data_list.append(value)
    freq = dict(collections.Counter(data_list))
    # print(freq)
    print(sorted(freq.items(), key=lambda kv:(kv[1], kv[0]), reverse=True))
    #print(data_list)

    wordcloud = WordCloud(background_color="white", max_words=200, font_path="STHeiti Medium.ttc")
    #wordcloud.generate(mytext.lower())
    wordcloud.generate_from_frequencies(freq)
    #wordcloud.generate_from_text(mytext)

    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig('1.svg',dpi=1500,format="svg")
    plt.show()

def data_sort_by_writer():
    data = pd.read_csv('new1.csv')
    country_counts = data['编剧'].value_counts()
    country_counts.columns = ['编剧', '数量']
    country_counts = country_counts.sort_values(ascending=False)
    c = (
        Bar()
            .add_xaxis(list(country_counts.index[:10]))
            .add_yaxis('电影数量', country_counts.values.tolist()[:10])
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title='电影数量'),
            yaxis_opts=opts.AxisOpts(name='编剧',axislabel_opts={"rotate":45}),
            xaxis_opts=opts.AxisOpts(name='电影数量'),
            )
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .render('各编剧写的电影数量.html')
    )

def data_sort_by_writer1():
    data = pd.read_csv('new1.csv')
    data_list = []
    for value in data['编剧']:
        data_list.append(value)
    freq = dict(collections.Counter(data_list))
    # print(freq)
    print(sorted(freq.items(), key=lambda kv:(kv[1], kv[0]), reverse=True))
    #print(data_list)

    wordcloud = WordCloud(background_color="white", max_words=200, font_path="STHeiti Medium.ttc")
    #wordcloud.generate(mytext.lower())
    wordcloud.generate_from_frequencies(freq)
    #wordcloud.generate_from_text(mytext)
    plt.figure()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def data_sort_by_actor():
    data = pd.read_csv('new2.csv')
    country_counts = data['主演'].value_counts()
    country_counts.columns = ['主演', '数量']
    country_counts = country_counts.sort_values(ascending=False)
    c = (
        Bar()
            .add_xaxis(list(country_counts.index[:10]))
            .add_yaxis('电影数量', country_counts.values.tolist()[:10])
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title='电影数量'),
            yaxis_opts=opts.AxisOpts(name='主演',axislabel_opts={"rotate":45}),
            xaxis_opts=opts.AxisOpts(name='电影数量'),
            )
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .render('主演参与的电影数量.html')
    )

def data_sort_by_actor1():
    data = pd.read_csv('new2.csv')
    data_list = []
    #print(data['主演'],type(data['主演']))
    for value in data['主演']:
        data_list.append(value)
    freq = dict(collections.Counter(data_list))
    # print(freq)
    print(sorted(freq.items(), key=lambda kv:(kv[1], kv[0]), reverse=True))
    #print(data_list)
    # mytext = ','.join(data_list)
    # mytext="a b a a a a a a av v v c c d d d d"
    #print(mytext)
    wordcloud = WordCloud(background_color="white", max_words=200, font_path="STHeiti Medium.ttc")
    #wordcloud.generate(mytext.lower())
    wordcloud.generate_from_frequencies(freq)
    #wordcloud.generate_from_text(mytext)
    plt.figure()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def draw():
    '''画电影评价数量和评分的关系'''
    '''
    data = pd.read_csv('top250.csv', encoding='latin-1')
    c = (
        Scatter()
            .add_xaxis(data['评分'].values.tolist())
            .add_yaxis('评价人数', data['评价人数'].values.tolist())
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Scatter-VisualMap(Size)"),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=150, min_=20),
            )
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .render('电影评分和评价人数的关系.html')
    )
    '''
    data = pd.read_csv('250.csv')
    x_data = data.loc[:, '评分'].values.tolist()
    y_data = data.loc[:, '评价人数'].values.tolist()
    plt.scatter(x_data, y_data)
    plt.xlabel("评分")
    plt.ylabel("评价数")
    plt.show()


if __name__ == '__main__':
    # data_sort_by_score()
    #data_sort_by_year()
    # data_sort_by_judgenumber()
    # data_sort_by_country()
    # data_sort_by_director()
    # data_sort_by_writer()
    # data_sort_by_actor()
    #draw()
    data_sort_by_director1()