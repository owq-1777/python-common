# -*- coding: utf-8 -*-
'''
@Desc   :   格式转换
'''


import time

# ------------------------------------ Time ------------------------------------ #


def unixtime2str(unixtime: float, time_zone: int = 8, time_format='%Y-%m-%d %H:%M:%S') -> str:
    """
    Convert Unix time (UTC seconds) to time string with given time zone.

    1620481024 -> '2021-05-08 21:37:04

    @param unixtime: UTC seconds.
    @param time_zone: the time zone of returned time, the range [-12, 12].
    @param time_format: the time format of returned time.
    @return: time string
    """
    unixtime += time_zone * 3600
    return time.strftime(time_format, time.gmtime(unixtime))


# ------------------------------------ list ------------------------------------ #

def split_list(list_obj: list, split_len: int) -> list:
    """ 分割list为小list

    :param cnt 分割最大列表长度
    :return [] -> [[],[]]
    """
    return [list_obj[i:i + split_len] for i in range(0, len(list_obj), split_len)]