# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : file.py
# Time       ：2021/11/2 17:04
# Author     ：Yooha
"""
 
import os
from show import ShowUtil
import shutil
from shell import ShellUtil
from timeutil import TimeUtil
from globalutil import Global
import openpyxl

class FileUtil:

    def __init__(self):
        pass


    @classmethod
    def init_file(cls):
        with open("./output/output.txt", "w", encoding='utf-8') as out:
            out.write('*******************************************************\n')
            out.write(TimeUtil.get_time())
            out.write('\n*******************************************************\n')
        with open("./output/hash_error.txt", "w", encoding='utf-8') as out:
            out.write('*******************************************************\n')
            out.write(TimeUtil.get_time())
            out.write('\n*******************************************************\n')
        cls.delete_file('out.xlsx')
        hash_excel = openpyxl.Workbook("out.xlsx")
        hash_sheel = hash_excel.create_sheet("hash")
        hash_excel.save("out.xlsx")
        return

    @classmethod
    def write_file(cls, path, info):
        Global.global_mutex.acquire()
        with open(path, "a", encoding='utf-8') as files:
            files.write(info)
            files.write('\n')
        Global.global_mutex.release()
        return


    @classmethod
    def check_dir(cls, path):
        if not os.path.exists(path):
            os.mkdir(path)
        return

    @classmethod
    def check_file(cls, file):
        if not os.path.exists(file):
            with open(file) as file:
                pass
        return

    @classmethod
    def update_output(cls, info):
        Global.global_mutex.acquire()
        with open("./output/output.txt", "a", encoding='utf-8') as out:
            out.write(info)
            out.write('\n')
        Global.global_mutex.release()
        return

    @classmethod
    def rmtree(cls,path):
        '''
        function: 删除文件夹
        '''
        if os.path.exists(path):
            try:
                shutil.rmtree(path, ignore_errors=True)
            except Exception as err:
                ShowUtil.error("FileUtil", "rmtree", path + " 删除失败:" + str(err))
                return False
            return True
        return False


    @classmethod
    def delete_file(cls, path):
        '''
        function: 删除单文件
        '''
        if os.path.exists(path):
            try:
                if os.path.exists(path):  
                    os.remove(path)     # 删除文件
            except Exception as err:
                ShowUtil.error("FileUtil", "delete_file", str(err))
        return

    @classmethod
    def delete_folder(cls, path, temp):
        '''
        function: 整体、彻底、删除文件夹及其子文件,需要Robocopy支持
        '''
        if os.path.exists(path):  
            cls.rmtree(path)
            if os.path.exists(path):  # 如果文件夹还存在，说明存在部分文件无法删除，使用Robocopy来删
                command = "Robocopy /MIR " + temp + " " + path
                if ShellUtil.execute_cmd(command, 30):   
                    cls.rmtree(path)
                else:
                    ShowUtil.error("FileUtil", "delete_folder", path + " 删除失败")
        return

 

