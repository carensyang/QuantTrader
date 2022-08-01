# -*- coding: utf-8 -*-
# version:0.1 整体框架结构设计

# bundle_data

# data_portal 数据门户：对数据抽象封装，不同数据源获取方式封装，统一输出格式

def get_history_window():
        """
        返回历史k线数据
        Parameters
        ----------
        assets : 客户资产对象
        bar_count: int
            请求行数
        frequency: string
            "1d" or "1m"
        field: string
            所需字段
        data_frequency: string
            查询数据评论
        ffill: boolean
            Forward-fill missing values. Only has effect if field
            is 'price'.
        Returns
        -------
        A dataframe containing the requested data.
        """
