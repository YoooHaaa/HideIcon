# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : show.py
# Time       ：2021/11/2 17:31
# Author     ：Yooha
"""


import click

class ShowUtil:
    
    def __init__(self):
        pass

    # blue  green   white  red   yellow
    @classmethod
    def error(cls, clsz, func, err):
        click.secho('%-30s%-30s%-20s' %(clsz, func, err), fg='red')


    @classmethod
    def warning(cls, clsz, func, war):
        click.secho('%-30s%-30s%-20s' %(clsz, func, war), fg='yellow')


    @classmethod
    def info(cls, clsz, func, inf):
        click.secho('%-30s%-30s%-20s' %(clsz, func, inf), fg='white')

