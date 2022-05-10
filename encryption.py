# -*- coding: utf-8 -*-
'''
@Desc   :   加密算法
'''

import base64
import hashlib


def create_md5(string: str, encoding='utf-8'):
    """ Generate MD5 encryption. """
    hl = hashlib.md5(string.encode(encoding=encoding))
    return hl.hexdigest()


def encode_base64(string: str, encoding='ascii'):
    base64_byte = base64.b64encode(string.encode(encoding))
    return base64_byte.decode(encoding)


def decode_base64(string: str, encoding='ascii'):
    origin_byte = base64.b64decode(string.encode(encoding))
    return origin_byte.decode(encoding)


def img2base64(img_path):
    """ 获取图片base64编码 """
    with open(img_path, 'rb') as f:
        return base64.b64encode(f.read())