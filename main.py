# !/usr/bin/env python
# -*- coding:utf-8 -*-　
# Author: leven
# File: main.py
# Date: 2022/1/19 0019

from DataLoad import *

if __name__ == '__main__':
    path = './data/data_format1/'
    train, test, info, log = load(path)
    pre_process(train, test, info, log)