# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : main.py
# Time       ：2021/11/2 18:02
# Author     ：Yooha
"""

import datetime
import time
import subprocess
from error import ErrorUtil
import chardet
from threading import Timer

class ShellUtil:

    def __init__(self):
        pass

    @classmethod
    def execute_cmd(cls, command, timeout=0):
        '''
        function:  执行单条命令
        '''
        time_start = datetime.datetime.now()
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        while process.poll() is None:  #poll函数返回None 表示在运行
            time.sleep(1) 
            if timeout != 0:  #timeout==0 则默认认为程序不会卡死，必须要等待程序自然结束
                time_now = datetime.datetime.now() #此时间单位为秒
                if (time_now - time_start).seconds > timeout: #执行时间超过timeout，认为进程卡死
                    process.terminate()   #关掉进程
                    time.sleep(1)       #给 1 秒的缓冲时间
                    return  False 
        return True

    @classmethod
    def get_shell(cls, cmd:str) -> (bool, list):
        '''
        function:  执行单条命令，并获取命令行返回值
        '''
        try:
            process = subprocess.Popen(cmd, shell = True, stdin=subprocess.PIPE, stdout=subprocess.PIPE ,stderr=subprocess.PIPE)
        except Exception as err:
            ErrorUtil.error('Shell', 'get_shell', str(err))
            return False, None
        return True, process.stdout.readlines()


    @classmethod
    def kill_popen(cls, process, alive):
        alive['alive'] = False
        process.terminate()   #关掉进程

    @classmethod
    def execute_apktool(cls, command, timeout=120):
        '''
        function:  执行单条命令
        '''
        print("_____________________________________in shell:" + command)
        alive = {'alive': True}
        isfind = False
        retval = False
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        timer = Timer(timeout, cls.kill_popen, [process, alive])
        try:
            timer.start()
            while process.poll() is None:  #poll函数返回None 表示在运行
                print('in poll')
                if isfind:
                    break
                for item in iter(process.stdout.readline,'b'):
                    if  not alive['alive']:
                        ErrorUtil.error('Shell', 'get_shell', 'command:' + command + '_反编译失败')
                        print("_____________________________________out shell:" + command)
                        return False
                    encode_type = chardet.detect(item)
                    if encode_type['encoding'] == 'utf-8':
                        #print('utf-8 : ' + item.decode('utf-8'))
                        if item.decode('utf-8').find('Baksmaling') != -1:
                            process.terminate()   #关掉进程
                            retval = True
                            isfind = True
                            break
                    elif encode_type['encoding'] == 'Windows-1252':
                        #print('windows : ' + item.decode('Windows-1252'))
                        if item.decode('Windows-1252').find('Baksmaling') != -1:
                            process.terminate()   #关掉进程
                            retval = True
                            isfind = True
                            break
                    else:
                        # print('gbk : ' + item.decode('gbk'))
                        if item.decode('gbk').find('Baksmaling') != -1:
                            process.terminate()   #关掉进程
                            retval = True
                            isfind = True
                            break
        except Exception as err:
            if process:
                process.terminate()   #关掉进程
            print(err)
        finally:
            timer.cancel()
        print("_____________________________________out shell:" + command)
        return retval





