# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : decompilation.py
# Time       ：2021/11/4 11:29
# Author     ：Yooha
"""

from shell import ShellUtil
from show import ShowUtil
from file import FileUtil
import os

class ApktoolUtil:

    def __init__(self):
        pass

    @classmethod
    def apktool_apk_res(cls, apkpath, output):
        # ShellUtil.execute_cmd('java -jar apktool.jar d ' + apkpath + ' -o ' + output, 200)
        ShellUtil.execute_apktool('java -jar apktool.jar d ' + apkpath + ' -o ' + output) # java -jar apktool.jar d ./apk/CEB02574111F0025A27768A4D9443746.apk -o./apk/123
        if not os.path.exists(output + '/res/values'):
            ShowUtil.error('ApktoolUtil', 'apktool_apk', apkpath + '-' + output + " 文件反编译失败")
            return False
        return True


    @classmethod
    def apktool_error(cls, hash):
        '''
        function: 保存反编译失败的hash
        '''
        FileUtil.write_file('./output/hash_error.txt', hash)


