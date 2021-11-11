# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : icon.py
# Time       ：2021/11/4 10:00
# Author     ：Yooha
"""

import shutil 
import os
import random
from error import ErrorUtil

class IconUtil:

    def __init__(self):
        pass

    @classmethod
    def copy_icon(cls, value, hash):
        try:
            list_dir = []
            icon = value.split('/')
            file = icon[0][1:]
            name = icon[1]
            for dir in os.listdir("./apk/" + hash + '/res'):
                if dir.find(file) != -1:
                    if os.path.isdir('./apk/' + hash + '/red/' + dir):
                        list_dir.append('./apk/' + hash + '/red/' + dir)
            for dir in list_dir:
                list_icon = os.listdir(dir)
                for ic in list_icon:
                    if ic.find(name) != -1:
                        print("copyfile: ./apk/" + hash + '/res/' + file + '/' + ic + ' ./output/pic/' + hash + '_' + str(random.randint(1, 99)) + '_' + ic)
                        shutil.copyfile("./apk/" + hash + '/res/' + file + '/' + ic, './output/pic/' + hash + '_' + str(random.randint(1, 99)) + '_' + ic)
                        return
        except Exception as err:
            ErrorUtil.error("IconUtil", "copy_icon", hash + ' -> ' + str(err))
        


    @classmethod
    def parse_error(cls):
        pass







