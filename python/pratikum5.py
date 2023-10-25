kendaraan = ['PCX', 'Motor', '156cc', 'hitam', '2roda']
print(kendaraan)

kendaraan.append('30jt')
kendaraan.append('160 CBS')
print(kendaraan)

kendaraan.insert(2,"PCX")
print(kendaraan)

ket = '''selamat datang di aplikasi menghitung luas bangun datar 
masukan pilihan:
1. untuk menghitung luas persegi
2. untuk menghitung luas lingkaran 
3. untuk menghutung luas segitiga
'''

pilih = input(ket)

match pilih: 
  case '1':
    print('kamu milih 1 untuk menghitung luas persegi')
    sisi = int(input('masukan sisi?'))
    luasP = sisi*sisi
    print('luas persegi yang sisinya', sisi,'adalah',luasP)

  case '2':
    print('kamu memilih 2 untuk menghitung luas lingkaran')
    jari2 = float(input('masukan jari-jari?'))
    luasL = 3.14 * jari2 * jari2
    print('luas lingkaran yang jari-jarinya', jari2,'adalah', int(luasL))
    
  case '3':
    print('kamu memilih 3 untuk menghitung luas segitiga')
    alas = int(input ('masukan alas?'))
    tinggi = int(input('masukan tinggi?'))
    luasS = 0.5 * alas * tinggi
    print = ('luas segitiga yang alasnya', alas, 'dari tingginya', tinggi, 'adalah', int(luasS))
    
  case _:
    print('salah memilih pilihan')