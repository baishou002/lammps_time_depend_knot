# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 16:10:16 2022

@author: Administrator
"""
import numpy as np
import random as rd

def distance(posr1,posr2):
    t_dis = np.sqrt((posr1[0]-posr2[0])**2 + (posr1[1]-posr2[1])**2 + (posr1[2]-posr2[2])**2)
    return t_dis
    

def geng_sp_point(init_x,init_y,init_z,r,box_s):
    
    while True:
        while True:
            x1 = rd.uniform(-r, r)
            x2 = rd.uniform(-r, r)
            if (x1**2 + x2**2 < r):
                break
        x = 2*x1*np.sqrt(r-x1**2-x2**2) + init_x
        y = 2*x2*np.sqrt(r-x1**2-x2**2) + init_y
        z = r-2*(x1**2+x2**2) + init_z
        
        if np.abs(x) < box_s-2.5 and np.abs(y) < box_s-2.5 and np.abs(z) < box_s-2.5:
            break
    return x,y,z


box_size = 40
posr = []
nk = 2000
dis = 2.5
ix,iy,iz = rd.uniform(-box_size+10, box_size-10),rd.uniform(-box_size+10, box_size-10),rd.uniform(-box_size+10, box_size-10)
posr.append([ix,iy,iz])
f = open('chian.txt','w')

while len(posr) < nk:
    
    while True:
        td = 10000
        end_index = len(posr) - 1
        posr_x,posr_y,posr_z = geng_sp_point(posr[end_index][0],posr[end_index][1],posr[end_index][2],dis,box_size)
        temp_list = [posr_x,posr_y,posr_z]
        if len(posr) - 2 > 0:
            for i in range(len(posr)-2):
                td = distance(posr[i],temp_list)
                if td < dis:
                    break
        if td < dis:
            continue
        elif td >= dis:
            break
        
    posr.append([posr_x,posr_y,posr_z])
    print(len(posr))
f.write('LAMMPS Description' + '\n' + '\n' + str(nk) + ' atoms' + '\n' + str(nk-1) + ' bonds' + '\n' + str(nk-2) + ' angles'+ '\n' + '\n')
f.write('1 atom types' + '\n' + '1 bond types' + '\n' + '1 angle types' + '\n' + '\n')
f.write('-40 40 xlo xhi' + '\n' + '-40 40 ylo yhi' + '\n' + '-40 40 zlo zhi' + '\n' + '\n' + 'Atoms # id mol type xu yu zu' + '\n' + '\n')


    
for i in range(len(posr)):
    f.write(str(i+1) + ' ' + str(1) + ' ' + str(1) + ' ' + str(posr[i][0]) + ' ' + str(posr[i][1]) + ' ' + str(posr[i][2]) + '\n')

f.write('\n' + 'Bonds' + '\n' + '\n')

for i in range(len(posr) - 1):
    f.write(str(i+1) + ' ' + str(1) + ' ' + str(i+1) + ' ' + str(i+2) + '\n')

f.write('\n' + 'Angles' + '\n' + '\n')
for i in range(len(posr) - 2):
    f.write(str(i+1) + ' ' + str(1) + ' ' + str(i+1) + ' ' + str(i+2) + ' ' + str(i+3) + '\n')

f.close()
        



















f = open('rdsp.txt','w')

r = 2.5
init_x = 33
init_y = 25
init_z = 15

for i in range(1000):
    while True:
        x1 = rd.uniform(-r, r)
        x2 = rd.uniform(-r, r)
        if (x1**2 + x2**2 < r):
            break
    x = 2*x1*np.sqrt(r-x1**2-x2**2) + init_x
    y = 2*x2*np.sqrt(r-x1**2-x2**2) + init_y
    z = r-2*(x1**2+x2**2) + init_z
    
    f.write(str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
    
f.close()