# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:30:26 2022

@author: Administrator
"""
import glob
import os
from itertools import islice


outer_path = '/share/home/yhliu/nxl/lammps/test/time_depend/dsDNA/chian_1000/401_500/'
file_list = os.listdir(outer_path)

count = 0

n,x,l = 7,1001,500
dp = [[[0]*n for i in range(x)] for j in range(l)]
for folder in file_list:
    k = 0
    inner_path = os.path.join(outer_path, folder)  #文件夹名字
#    filelist = os.listdir(inner_path)#当前文件夹下所有文件名
    temp = str(inner_path)
    bu_files = glob.glob(temp+'/BU*.txt')
    input_file = open(bu_files[0])
    
    
#    print(input_file)
    for line in islice(input_file,3, None):
        values = [str(s) for s in line.split()]
        for i in range(n):
            dp[count][k][i] = values[i]
        k += 1
    count += 1

f = open('time_dep_knot_lk.txt','w')

time_depend_lk = []
for i in range(x):
    l_knot = 0
    count_knot = 0
    for j in range(l):
        if dp[j][i][6] != '-1':
            l_knot += float(dp[j][i][6])
            count_knot += 1
    if count_knot == 0:        
        time_depend_lk.append(l_knot/1)
    else:
        time_depend_lk.append(l_knot/count_knot)


for i in range(len(time_depend_lk)):
    f.write(str(i) + '     ' + str(time_depend_lk[i]) + '\n')
f.close()
    
    
    
    
    
    
    
    
    