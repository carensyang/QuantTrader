# -*- coding: utf-8 -*-
# version:0.1 整体框架结构设计

from sqlalchemy import create_engine
import pandas as pd

# bundle_data
# data_portal 数据门户：对数据抽象封装，不同数据源获取方式封装，统一输出格式

engine = create_engine('sqlite:////*')


# 数据接口
def get_history_data(index_ids=None, end_date=None):
    """
    读取指数历史数据到指定截止日
    Input:
        index_ids: list of str, 指数代码列表, like ['hs300', 'csi500']
        end_date: datetime.date, 截止日期
    Output:
        data: df(date*, index1, index2, ...), 多个指数的历史收盘价序列
    """
    datas = []
    for code in index_ids:
        sql = 'select  * from stock_info where "index" >= "%s" and \
            "index" <= "%s" and code = "%s"' % ("2018-01-01", end_date, code)
        data = pd.read_sql(sql,engine)
        data = data.loc[:,["index","close"]]
        data["index"] = data["index"].map(sss)
        data.set_index(["index"], inplace=True)
        # 重命名索引名和列名
        data.index.name = 'date'
        data.rename(columns={"close" : code}, inplace=True)
        datas.append(data)
    data = pd.concat(datas, axis=1)
    #pd.set_option('display.max_rows', None)
    return data


def get_price(code, start_date=None, end_date=None, frequency='daily', fields=None):
    """
    获取行情数据
    Parameters
    ----------
    code: string
        标的代码
    start_date: string
        起始时间
    end_date: string
        结束时间
    frequency: string
        日线 or 分钟线
    fields: array
        需要字段
    Returns
    -------
    dataframe
    """

    sql = 'select  * from stock_info where "index" >= "%s" and \
        "index" <= "%s" and code like "%s"' % (start_date, end_date, code)
    data = pd.read_sql(sql,engine)
    return data

stock_price = get_price("159934.XSHE", "2018-01-01 00:00:00", "2022-07-20 00:00:00")
print(stock_price)
