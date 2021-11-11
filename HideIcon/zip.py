# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : zip.py
# Time       ：2021/11/2 16:29
# Author     ：Yooha
"""

from shell import Shell
from show import ShowUtil
from file import FileUtil

class ZipUtil:

    def __init__(self):
        pass

    @classmethod
    def zip_file(cls, packpath, filepath, output, timeout=10):
        if not Shell.execute_cmd('7z e "' + packpath + '" -o"' + output + '" ' + filepath, timeout): # 单独解压指定文件：7z e 123.apk -o./apk/ AndroidManifest.xml
            ShowUtil.error('ZipUtil', 'zip_file', packpath + '-' + filepath + " 文件解压失败")

    @classmethod
    def zip_pack(cls, packpath, output, timeout=200):
        if not Shell.execute_cmd('7z x "' + packpath + '"  -y -aos -o"' + output + '"', timeout): # 解压包 给3min时间，超时则认为解压失败 
            ShowUtil.error('ZipUtil', 'zip_pack', packpath + " 包解压失败")

    @classmethod
    def zip_error(cls, hash):
        '''
        function: 保存解压失败的hash
        '''
        FileUtil.write_file('./output/hash_error.txt', hash)


