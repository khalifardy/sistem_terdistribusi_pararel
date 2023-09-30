#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import math

#MEMBUAT CLASS LINGKARAN
class lingkaran:
    #MEMBUAT FUNGSI CONSTRUCTOR UNTUK MEMASUKKAN JARI-JARI LINGKARAN
    def __init__(self,radius):
        self.radius = radius 
    
    #MEMBUAT FUNGSI UNTUK MENAMPILKAN JARI-JARI LINGKARAN
    def cetak_jari_jari(self):
        print(f"Jari-jari lingkaran: {self.radius}")
    
    #MEMBUAT FUNGSI UNTUK MENGHITUNG LUAS LINGKARAN
    def luas_lingkaran(self):
        hasil = math.pi * (self.radius**2)
        print(f"Luas Lingkaran : {hasil}")

#MENJALANKAN FUNGSI DALAM CLASS
jari_jari = float(input("masukan jari-jari: "))
hitung = lingkaran(jari_jari)
hitung.cetak_jari_jari()
hitung.luas_lingkaran()


# In[ ]:




