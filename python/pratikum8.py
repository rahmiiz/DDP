#no.1
def profil(nama, alamat, gender, umur, hobi):
    print("Nama saya adalah", nama)
    print("Alamat rumah saya", alamat)
    print("Jenis Kelamin saya", gender)
    print("Umur saya", umur)
    print("Saya memiliki Hobi yaitu", hobi)

profil("Rahmi Izzati", "Jl. Damai Ujung", "Perempuan", "18 Tahun", "Membaca")

#no.2
def kelulusan(nilai):
   if nilai <= 60:
       return "Tidak Lulus"
   elif 61 <= nilai <= 70:
       return "Baik"
   elif 71 <= nilai <= 80:
       return "Sangat Baik"
   elif 81 <= nilai <= 100:
       return "Istimewa"
   else:
       return "Nilai tidak valid"

nilai_siswa = float(input("Masukan Nilai Siswa :"))

hasil = kelulusan(nilai_siswa)
print("Nilai Kelulusan", hasil)

#no.3
def bilangan_ganjil(n):
    for i in range(1, n+1, 2):
        print(i)

bilangan_ganjil(100)