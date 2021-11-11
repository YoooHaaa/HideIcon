# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : global.py
# Time       ：2021/11/3 18:00
# Author     ：Yooha
"""

import multiprocessing 

class Global:
    global_mutex = multiprocessing.Lock()
    global_futures  = []






