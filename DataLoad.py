# !/usr/bin/env python
# -*- coding:utf-8 -*-　
# Author: leven
# File: DataLoad.py
# Date: 2022/1/19 0019

import numpy as np
import pandas as pd


def load(path):
    df_train = pd.read_csv(path + 'train_format1.csv', sep=',')
    df_test = pd.read_csv(path + 'test_format1.csv', sep=',')

    user_info = pd.read_csv(path + 'user_info_format1.csv', sep=',')
    user_log = pd.read_csv(path + 'user_log_format1.csv', sep=',')

    return df_train, df_test, user_info, user_log


def pre_process(df_train, df_test, user_info, user_log):
    df_train['orign'] = 'train'
    df_test['orign'] = 'test'
    matrix = pd.concat([df_train, df_test], axis=0, ignore_index=True, sort=False)
    matrix.drop(columns='prob', axis=1, inplace=True)
    matrix = matrix.merge(user_info, on='user_id', how='left')
    user_log.rename(colunms={'seller_id': 'merchant_id'}, inplace=True)