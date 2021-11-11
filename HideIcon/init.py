# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : init.py
# Time       ：2021/11/2 17:33
# Author     ：Yooha
"""

from file import FileUtil
from excel import ExcelUtil

class Init:

    def __init__(self):
        pass
    
    @classmethod
    def init_dir(cls):
        FileUtil.check_dir('apk')
        FileUtil.check_dir('output')
        FileUtil.check_dir('tmp')
        FileUtil.check_dir('output/pic')
        FileUtil.init_file()
        ExcelUtil.init_xlsx()
