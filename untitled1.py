#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 20:20:24 2020

@author: marcellinoenriquesuprapto
"""

print('Halo selamat datang! ini siapa ya?')

nama = input('masukkin dong nama kamu disini : ')
nama_asli = 'gloria'
if nama == nama_asli :
    print('halo', nama_asli,'!!')
else:
    print('gaush bohong dehhh. aku tau kamu tuh gloria kann')

print('kenalin, aku program sederhana yang dibuat secret admirermu, karena dia pengen nyampein sesuatu ke kamu')

print('')
print('')

umur = int(input('umur kamu berapa?'))
umur_asli = '20'

while umur != umur_asli :
    umur = input('boong lagi nihhhh, yang bener umur kamu adalah : ')

ultah = input('hariini lagi ultah yaa? (yes/no) : ')

while ultah != 'yes':
    ultah = input('boong mulu. aku taanya lagi nihhhh. hari ini ultah kamu kannn? (yes/no) : ')

print('kalo gitu, happy birthday queen of this day, wish you all the best ')

banyak=int(input('kamu mau diucapin berapa kali?'))
while banyak<=0 : 
     banyak=int('serius. mau diucapin berapa kaliii?')
for i in range (banyak):
    print ('HAPPY BIRTHDAY GLORIAAA! <3 <3')
    
while True :
    pass