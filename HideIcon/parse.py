# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : parse.py
# Time       ：2021/11/2 17:44
# Author     ：Yooha
"""
from shell import ShellUtil
from error import ErrorUtil
from globalutil import Global
try: 
    import xml.etree.cElementTree as ET 
except ImportError: 
    import xml.etree.ElementTree as ET 




class ParseXMLUtil:

    def __init__(self):
        pass

    @classmethod
    def parse_AndroidManifest(cls, apkpath, output) -> (bool, list):
        '''
        function: 用aapt解析出树形结构的AndroidManifest.xml文件
        '''
        try:
            return ShellUtil.get_shell('aapt dump xmltree ' + apkpath + " AndroidManifest.xml > " + output)
        except Exception as err:
            ErrorUtil.error("ParseXMLUtil", "parse_AndroidManifest", str(err))
            return False, None


    @classmethod
    def parse_error(cls, hash):
        Global.global_mutex.acquire()
        with open('./output/hash_error.txt', 'a', encoding='utf-8') as files:
            files.write(hash)
            files.write("\n")
        Global.global_mutex.release()


    @classmethod
    def read_alias(cls, path) -> list:
        xml = None
        out = []
        tmp = ''
        begin = False
        with open(path, 'r', encoding='utf-8') as files:
            xml = files.readlines()
        for line in xml:
            if line.find('activity-alias') != -1:
                begin = True
                tmp = line.strip()
            else:
                if begin:
                    if line.find(' A: ') != -1:
                        tmp = tmp + ' ' + line.strip()
                    else:
                        begin = False
                        out.append(tmp)
        return out

    @classmethod
    def read_hide(cls, path) -> list:
        '''
        function: 从正常AndroidManifest.xml文件中解析出 label和icon
        '''
        try:
            ET.register_namespace('android', "http://schemas.android.com/apk/res/android")
            list_hide = []
            tree = ET.parse(path) 
            root = tree.getroot()
            for child in root.findall('application')[0].findall('activity-alias'):
                icon = None
                label = None
                for key in child.keys():
                    if key.find('icon') != -1:
                        icon = child.attrib[key]
                    elif key.find('label') != -1:
                        label = child.attrib[key]
                if icon != None and label != None:
                    list_hide.append({'icon':icon, 'label':label})
        except Exception as err:
            ErrorUtil.error("ParseXMLUtil", "read_hide", path + '_' + str(err))
        return list_hide
        


            