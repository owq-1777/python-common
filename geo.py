from coord_convert.transform import (bd2gcj, bd2wgs, gcj2bd, gcj2wgs, wgs2bd, wgs2gcj)


def geo2all(type: str, lon: float, lat: float) -> dict:
    """地理坐标系转换, 默认保留6位小数

    :param type: 传入坐标系类型
        - WGS84: 为一种大地坐标系,也是目前广泛使用的GPS全球卫星定位系统使用的坐标系。
        - GCJ02: 又称火星坐标系,是由中国国家测绘局制定的地理坐标系统,是由WGS84加密后得到的坐标系。
        - BD09: 为百度坐标系,在GCJ02坐标系基础上再次加密。
    :param lon: 径度
    :param lat: 纬度
    :raises TypeError: _description_
    :return: 所有坐标类型对象
    """
    """地理坐标系转换, 保留6位小数

    Args:
        type (str): 传入坐标系类型
            - WGS84: 为一种大地坐标系,也是目前广泛使用的GPS全球卫星定位系统使用的坐标系。
            - GCJ02: 又称火星坐标系,是由中国国家测绘局制定的地理坐标系统,是由WGS84加密后得到的坐标系。
            - BD09: 为百度坐标系,在GCJ02坐标系基础上再次加密。
        lon (float): 径度
        lat (float): 纬度
    """

    if type.upper() == 'WGS84':
        wgslon, wgslat = lon, lat
        gcjlon, gcjlat = wgs2gcj(lon, lat)
        bdlon, bdlat = wgs2bd(lon, lat)
    elif type.upper() == 'GCJ02':
        wgslon, wgslat = gcj2wgs(lon, lat)
        gcjlon, gcjlat = lon, lat
        bdlon, bdlat = gcj2bd(lon, lat)
    elif type.upper() == 'BD09':
        wgslon, wgslat = bd2wgs(lon, lat)
        gcjlon, gcjlat = bd2gcj(lon, lat)
        bdlon, bdlat = lon, lat
    else:
        raise TypeError

    geo = {
        'geoPointWGS84': {'lon': float(f'{wgslon:.6f}'), 'lat': float(f'{wgslat:.6f}')},
        'geoPointGCJ02': {'lon': float(f'{gcjlon:.6f}'), 'lat': float(f'{gcjlat:.6f}')},
        'geoPointBD09': {'lon': float(f'{bdlon:.6f}'), 'lat': float(f'{bdlat:.6f}')},
    }
    return geo
