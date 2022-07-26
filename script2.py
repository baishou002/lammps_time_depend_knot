# -*- coding: utf-8 -*-
"""
Created on Wed May 11 11:13:32 2022

@author: Administrator
"""
import os
import random as rd

s = 50000
q = 50000000
start = 1
end = 501

in_file = []

for line in open('in2.file','r'):
    values = [str(s) for s in line.split()]
    in_file.append(values)

l = len(in_file)



for i in range(start,end):
    t = rd.randint(1000000,7000000)
    in_file[2][3] = str(t)
    os.mkdir(f'{i}')
    f = open('in.file','w')
    for j in range(l):
        p = len(in_file[j])
        for k in range(p):
            f.write(in_file[j][k] + '  ')
        f.write('\n')
    f.close()
    
    os.system('mv in.file ' + f'{i}')
    os.system('cp data.file ' + f'{i}')
    
    
    
    
    
    