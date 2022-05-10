# -*- coding: utf-8 -*-
'''
@Desc   :
'''
import platform
import inspect
import re
import time

if platform.system() == 'Windows':
    import msvcrt

import difflib

# ------------------------------------ Shell ------------------------------------ #


def input_password(info: str = 'password: ') -> tuple:
    """shell密码输入

    按键绑定: 回车确认, 退格删除, Esc退出(返回False)

    :param info: 提示信息, defaults to 'password: '
    :type info: _type_, str
    :return: 信号和密码
    :rtype: tuple
    """
    print(info, end='', flush=True)
    pawd_arr = []
    while True:

        keypad = msvcrt.getch()
        # 回车
        if keypad == b'\r':
            msvcrt.putch(b'\n')
            return True, b''.join(pawd_arr).decode()
        # 退格
        elif keypad == b'\x08':
            if pawd_arr:
                pawd_arr.pop()
                msvcrt.putch(b'\b')
                msvcrt.putch(b' ')
                msvcrt.putch(b'\b')
        # Esc
        elif keypad == b'\x1b':
            msvcrt.putch(b'\n')
            return False, ''
        else:
            pawd_arr.append(keypad)
            msvcrt.putch(b'*')


def format_wait_time(wait: int):
    """ 等待时间输出 """
    sign = 1
    for _ in range(wait * 2):
        wait = wait - 1 if sign % 2 == 1 else wait
        print(f'\r{" "*6}\r{wait}{"."*(sign)}', end='')
        sign = 1 if sign == 4 else sign + 1
        time.sleep(.5)
    print(f'\r{" "*6}\r', end='')

# ------------------------------------ Other ------------------------------------ #


def re_search_one(pattern, string) -> str:
    """ 返回第一个正则匹配的元素 """
    if result := re.search(pattern, string):
        return result.group(1)
    return None


def string_similar(str_1, str_2):
    """ 字符串相似度计算 """
    return difflib.SequenceMatcher(None, str_1, str_2).quick_ratio()


def get_now_funsname():
    """ 获取当前运行函数名 """
    return inspect.stack()[1][3]
