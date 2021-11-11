# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : label.py
# Time       ：2021/11/3 11:29
# Author     ：Yooha
"""

from show import ShowUtil

class LabelUtil:

    def __init__(self):
        pass

    @classmethod
    def parse_label(cls, value, path):
        '''
        param:   value:AndroidManifest.xml中的label值， path:strings.xml的路径
        return:  返回获取到的labal值
        '''
        if value.find('@string') != -1:
            label = value.split("/")
            tag = label[1]
            return cls.read_label(path, tag)
        else:
            return True, value

    @classmethod
    def parse_error(cls):
        pass

    @classmethod
    def read_label(cls, path, tag):
        label = None
        try:
            with open(path, "r", encoding='utf-8') as files:
                list_xml = files.readlines()
                for xml in list_xml:
                    if xml.find('name="' + tag + '"') != -1:  # 有些tag标签非常短，容易出现匹配错误错误：<string name="s">@string/r</string>
                        label = xml.split('name="' + tag + '"')[1]
                        label = label.split('<')[0]
                        label = label.split('>')[1]
                        break
            if label.find("@string") != -1:
                return cls.read_label(path, label.split('/')[1])
        except Exception as err:
            ShowUtil.error('LabelUtil', 'read_label', tag + ' _ ' + path + ' _ ' + str(err))
            return False, label
        return True, label

 

