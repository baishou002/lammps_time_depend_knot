# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:44:34 2021

@author: Administrator
"""
import glob
import os
import sys


nk = int(sys.argv[1])
outer_path = str(sys.argv[2])
file_list = os.listdir(outer_path)


for folder in file_list:
    inner_path = os.path.join(outer_path, folder)
#    filelist = os.listdir(inner_path)
    temp = str(inner_path)
    txt_path = glob.glob(temp + '/dump.lammpstrj')



    t = temp +  '/newknot' + '.txt'
    f = open(t,'w')
#    print(t)
    po = []
    
    for line in open(txt_path[0],'r'):
        values = [str(s) for s in line.split()]
        if values[0] == f'{nk}' and len(values) == 1:
            f.write(values[0] + '\n')
        if len(values) == 6 and values[3] != 'ff':
            temp = [float(t) for t in values]
            po.append(temp)
            if len(po) == nk:
                po.sort()
                for i in range(len(po)):
                    f.write(str(po[i][3]) + '     ' + str(po[i][4]) + '     ' + str(po[i][5]) + '\n')
                po = []
            
    f.close()