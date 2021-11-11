# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : main.py
# Time       ：2021/11/2 18:23
# Author     ：Yooha
"""
import os
from list import ListUtil
from download import DownloadUtil
from init import Init
from file import FileUtil
from show import ShowUtil
from parse import ParseXMLUtil
from error import ErrorUtil
from timeutil import TimeUtil
from globalutil import Global
import concurrent
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
from apktool import ApktoolUtil
from label import LabelUtil
from icon import IconUtil
from excel import ExcelUtil
from error import ErrorUtil

def parse(hash) -> (bool, str):
    alias = False
    try:
        if not DownloadUtil.download_apk(hash):  #下载样本
            DownloadUtil.download_err(hash)
        else:
            os.mkdir('./apk/' + hash)
            ret, info = ParseXMLUtil.parse_AndroidManifest('./apk/' + hash + '.apk', './apk/' + hash + '/AndroidManifest.xml') # aapt解析出来的AndroidManifest 格式与 apktool解析出来的不一样
            if ret:
                xml = ParseXMLUtil.read_alias('./apk/' + hash + '/AndroidManifest.xml')
                for line in xml:  
                    if line.find("activity-alias") != -1:
                        if line.find("android:label") != -1 and line.find("android:icon") != -1: # 入口必须要有icon和label
                            ShowUtil.warning('', 'hash', hash)
                            FileUtil.update_output(hash)  
                            alias = True
                            break
            else:
                ParseXMLUtil.parse_error(hash)
            FileUtil.rmtree('./apk/' + hash)
            if not alias:
                FileUtil.delete_file('./apk/' + hash + '.apk') # 多入口apk文件暂时不删，留着进行精筛
    except Exception as err:
        FileUtil.rmtree('./apk/' + hash)
        FileUtil.delete_file('./apk/' + hash + '.apk')
        ErrorUtil.error('main', 'parse', str(err))
        FileUtil.write_file('./output/hash_error.txt', hash)
    return alias, hash
    

def save_hash(result):
    ret, hash = result.result()
    if ret:
        Global.global_hash.append(hash)


def filtter(hash):
    print(hash + '------------------ in in in')
    label_hide = False
    info = None
    try:
        if os.path.exists('./apk/' + hash + '.apk'):
            if ApktoolUtil.apktool_apk_res('./apk/' + hash + '.apk', './apk/' + hash):
                list_hide = ParseXMLUtil.read_hide('./apk/' + hash + '/AndroidManifest.xml')
                print(list_hide)
                if len(list_hide) == 0:
                    FileUtil.delete_file('./apk/' + hash + '.apk')
                    FileUtil.delete_folder('./apk/' + hash, './tmp')
                else:
                    for hide in list_hide:
                        ret, label = LabelUtil.parse_label(hide['label'], './apk/' + hash + '/res/values/strings.xml')
                        if ret:
                            label_hide = True
                            info = {'hash':hash, 'label':label, 'icon':hide['icon']}
                            print('info_____________' + str(info))
                            if not ExcelUtil.write(info):
                                ErrorUtil.error('写入xlsx失败：', '', info)
                            print('write info over _____________' + str(info))
                        else:
                            ShowUtil.error(hash, 'label解析失败')
            else:
                FileUtil.write_file('./output/hash_error.txt', hash)
        else:
            FileUtil.write_file('./output/hash_error.txt', hash)
    except Exception as err:
        pass
    FileUtil.delete_folder('./apk/' + hash, './tmp')
    FileUtil.delete_file('./apk/' + hash + '.apk')
    FileUtil.rmtree('./tmp')
    print(hash + '------------------ out out out')
    return label_hide, info



def main():
    begin = TimeUtil.get_now()
    Init.init_dir()
    hash_list = []
    with open('hash.txt') as files:
        hash_list = ListUtil._strip_list(files.readlines())
        hash_list = ListUtil._unrepeat_list(hash_list)
    pool_alias=ProcessPoolExecutor(multiprocessing.cpu_count())
    for hash in hash_list: 
        future=pool_alias.submit(parse, hash)
        # future.add_done_callback(show)
    pool_alias.shutdown(wait=True)
    count = TimeUtil.get_now() - begin
    ShowUtil.info("本次初筛耗时：" + str(round(float(count)/float(60), 3)) + "分钟" , '', '')  # 结果保留3位有效数
    ShowUtil.info("平均每个样本耗时：" + str(round(float(count)/float(len(hash_list)), 3)) + " 秒" , '', '')  

    begin = TimeUtil.get_now()
    pool_hide=ProcessPoolExecutor(multiprocessing.cpu_count())
    with open('./output/output.txt') as files:
        hash_list = ListUtil._strip_list(files.readlines())[3:]
        hash_list = ListUtil._unrepeat_list(hash_list)
    for hash in hash_list:
        future=pool_hide.submit(filtter, hash)
    pool_hide.shutdown(wait=True)
    count = TimeUtil.get_now() - begin
    ShowUtil.info("本次复筛耗时：" + str(round(float(count)/float(60), 3)) + "分钟" , '', '')  # 结果保留3位有效数
    ShowUtil.info("平均每个样本耗时：" + str(round(float(count)/float(len(hash_list)), 3)) + " 秒" , '', '')  



if __name__ == "__main__":
    main()

# 200个hash共耗时：