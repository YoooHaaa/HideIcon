# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : download.py
# Time       ：2021/11/2 17:13
# Author     ：Yooha
"""


import requests
from file import FileUtil
from error import ErrorUtil

class DownloadUtil:
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0', } 

    def __init__(self):
        pass

    @classmethod
    def download_apk(cls, hash):
        '''
        function: 下载apk文件
        '''
        try:
            url = "https://afdfs.avlyun.org/v1/download/sample/"
            requests.packages.urllib3.disable_warnings() # 由于下面禁用了证书认证，所以控制台会弹出警告，本行代码能省略警告
            res = requests.get(url=url + hash, headers=cls.header, verify=False)
            if(res.status_code == 404):
                ErrorUtil.error('DownloadUtil', "download_apk", hash + " 下载出错 ")
                return False
            with open('./apk/' + hash + ".apk", "wb") as apk:
                apk.write(res.content)
        except Exception as err:
            ErrorUtil.error('DownloadUtil', "download_apk", str(err))
            return False
        return True



    @classmethod
    def download_err(cls, hash):
        '''
        function: 保存下载失败的hash
        '''
        FileUtil.write_file('./output/hash_error.txt', hash)



