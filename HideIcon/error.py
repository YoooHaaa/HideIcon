# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : error.py
# Time       ：2021/11/2 18:02
# Author     ：Yooha
"""

from timeutil import TimeUtil
from show import ShowUtil
from globalutil import Global

class ErrorUtil:

    def __init__(self):
        pass

    @classmethod
    def error(cls, claz, func, err):
        ShowUtil.error(claz, func, err)
        cls.write_error(claz, func, err)

    @classmethod
    def write_error(cls, claz, func, err):
        Global.global_mutex.acquire()
        with open("./output/err.txt", "a", encoding='utf-8') as files:
            files.write("********************************************************************************\n")
            files.write(TimeUtil.get_time())
            files.write("\n")
            files.write(claz + ' -> ' + func)
            files.write("\n")
            files.write(err)
            files.write("\n")
        Global.global_mutex.release()
        return   