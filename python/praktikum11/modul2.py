import math
def tambah(bil1,bil2):
    hasil = bil1+bil2
    print("hasil tambah dari",bil1,"+",bil2,"=",hasil)
def kurang(bil1,bil2):
    hasil = bil1-bil2
    print("hasil pengurangan dari",bil1,"-",bil2,"=",hasil)
def kali(bil1,bil2):
    hasil = bil1 * bil2
    print("hasil perkalian dari",bil1,"*",bil2,"=",hasil)
def bagi(bil1,bil2):
    hasil = bil1 / bil2
    print("hasil pembagian dari",bil1,"/",bil2,"=",hasil)
def pangkat(bil1, bil2):
    hasil = math.pow(bil1, bil2)
    print("hasil pemangkatan dari",bil1,"^",bil2,"=",hasil)
def akar(bil):
    hasil = math.sqrt(bil)
    print("hasil akar dari =",hasil)
def tan(bil):
    hasil = math.tan(bil)
    print("hasil tan dari =",hasil)
def cos(bil):
    hasil = math.cos(bil)
    print("hasil cos dari =",hasil)
def log(bil):
    hasil = math.log(bil)
    print("hasil log dari =",hasil)
def sin(bil):
    hasil = math.sin(bil)
    print("hasil sin dari =",hasil)