import re
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Heiti TC']    # 指定默认字体：解决plot不能显示中文问题
plt.rcParams['axes.unicode_minus'] = False           # 解决保存图像是负号'-'显示为方块的问题

book_tag = '文化'
#数据清洗：
def data_sort():
    file_name = './book_list-' + book_tag + '.xlsx'
    df = pd.read_excel(file_name)
    df.sort_values(by='评价人数', ascending=False, inplace=True)
    os.remove(file_name)
    df.loc[:, ['书名', '评分', '评价人数']].to_excel(file_name, index=False)

def data_plot():
    file_name = './book_list-' + book_tag + '.xlsx'
    df = pd.read_excel(file_name)
    x_book_name = df.loc[:, '书名'].values.tolist()[0:165]
    y1 = df.loc[:, '评分'].values.tolist()[0:165]
    y2 = df.loc[:, '评价人数'].values.tolist()[0:165]
    fig, ax1 = plt.subplots()
    fig.autofmt_xdate()
    ax2 = ax1.twinx()
    #ax1.plot(x_book_name, y1, 'g--')
    #ax2.plot(x_book_name, y2, 'b--')
    ax1.plot(x_book_name, y1, 'go')
    ax2.plot(x_book_name, y2, 'bo')
    ax1.set_xlabel('书名')
    ax1.set_ylabel('评分', color='g')
    ax2.set_ylabel('评价人数', color='b')

    plt.savefig('./图书评分情况.jpg')
    plt.show()

def data_plot1():
    x_data = ['9分及以上', '[8,9)', '[7,8)', '[6,7)']
    y_data = [1, 9, 8, 2]
    plt.bar(x_data, y_data)
    plt.xlabel("评分等级")
    plt.ylabel("书本数量")
    plt.show()

def data_plot2():
    x_data = ['9分及以上', '[8,9)', '[7,8)', '[6,7)']
    y_data = [9, 67, 77, 10]
    plt.bar(x_data, y_data)
    plt.xlabel("评分等级")
    plt.ylabel("书本数量")
    plt.show()

def data_plot3():
    file_name = './book_list-' + book_tag + '.xlsx'
    df = pd.read_excel(file_name)
    x_data = df.loc[:, '评分'].values.tolist()[0:165]
    y_data = df.loc[:, '评价人数'].values.tolist()[0:165]
    plt.scatter(x_data, y_data)
    plt.xlabel("评分")
    plt.ylabel("评价数")
    plt.show()

if __name__ == "__main__":
    #data_sort()
    #data_plot()
    #data_plot1()
    #data_plot2()
    #分析评分和评价人数的关系
    data_plot3()
