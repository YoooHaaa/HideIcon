# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : time.py
# Time       ：2021/11/2 18:00
# Author     ：Yooha
"""

import datetime
import time

class TimeUtil:


    def __init__(self):
        pass


    @classmethod
    def get_time(cls):
        '''
        function:  将当前时间格式化为字符串
        '''
        now_time = str(datetime.datetime.now())
        now_time = now_time.replace(" ", "-").replace(":", "-")
        now_time = now_time.split('.')[0]
        return now_time

    @classmethod
    def get_now(cls):
        return time.time()