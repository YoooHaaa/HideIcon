# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : download.py
# Time       ：2021/11/2 17:11
# Author     ：Yooha
"""


class ListUtil:

    def __init__(self):
        pass

    @classmethod
    def _unrepeat_list(cls, lists):
        '''
        function: list去重
        '''
        new_list = []
        for item in lists:
            if item not in new_list:
                new_list.append(item)
        return new_list



    @classmethod
    def _strip_list(cls, lists):
        '''
        function: 处理列表中的 \n 和 空行
        '''
        new_list = []
        for item in lists:
            strs = item.strip()
            if strs != "":
                new_list.append(strs)
        return new_list