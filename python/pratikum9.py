#no 1
hasil_akhir = [
    {'nama':'Reza', 'nilai':70},
    {'nama':'Ciut', 'nilai':63},
    {'nama':'Dian', 'nilai':80},
    {'nama':'Badu', 'nilai':40}
]

def predikatLulus(data):
    lulus = [mahasiswa['nama']
        for mahasiswa in data
        if mahasiswa['nilai'] > 65]
    return lulus
hasil = predikatLulus(hasil_akhir)
print('siswa yang lulus:', hasil)

#no 2
buah = (['pepaya', 'mangga', 'pisang', 'durian', 'jambu'])

def list_buah(buah):
    list_terbalik = []
    for i in range(len(buah)-1, -1, -1):
        list_terbalik.append(buah[i])
    return list_terbalik
hasil = list_buah(buah)
print('Hasilnya : ', hasil)

#no 3
nama_buah = (['pepaya', 'mangga', 'pisang', 'durian', 'jambu'])

def duplikasi(nama_buah):
    list = []
    for n in nama_buah:
        list.append (n)
        list.append (n)
    return list
hasil = duplikasi(nama_buah)
print('Hasilnya : ', hasil)

#no 4
nama = "NurulFikri"

def konsonan(nama):
    konsonan = ""
    for i in nama:
        if i not in "aiueo":
            konsonan += i
    return konsonan
hasil = konsonan(nama)
print('Huruf konsonan dari Nurul Fikri adalah', hasil)