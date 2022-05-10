# -*- coding: utf-8 -*-
'''
@Desc   :   网络相关工具
'''


import socket


def get_host() -> str:
    """ 获取主机IP """
    return socket.gethostbyname(socket.gethostname())


def check_port_open(host: str = '127.0.0.1', port: int = 80) -> bool:
    """ 检测端口是否开放 """
    with socket.socket() as sock:
        sock.settimeout(2)
        try:
            sock.connect((host, port))
            return True
        except (socket.timeout, ConnectionRefusedError):
            return False