# -*- coding: utf-8 -*-
"""
Created on Thu May 12 10:13:22 2022

@author: Administrator
"""
import os

count = 1
for i in range(5):
    os.mkdir(str(count) + '_' + str(count+99))
    for j in range(count,count + 100):
        os.system('mv ' + f'{j} ' + str(count) + '_' + str(count+99))
    count += 100