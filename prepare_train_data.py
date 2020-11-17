#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:fangpf
@time: 2020/11/17
"""
import os

images_path = './Dataset/train/images/'
train_list = './Dataset/train/trainlist.txt'


def process():
    train_file_list = os.listdir(images_path)
    with open(train_list, 'wt') as f:
        for file in train_file_list:
            full_file_path = images_path + file
            f.write(str(full_file_path) + '\n')


if __name__ == '__main__':
    process()
    print('Done!')