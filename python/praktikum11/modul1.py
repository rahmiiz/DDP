def persegi(sisi):
    luas = sisi*sisi
    keliling = 4*sisi
    print("Luas Persegi", luas)
    print("Keliling Persegi", keliling)

def persegi_panjang(p, l):
    luas = p*l
    keliling = 2*(p+l)
    print("Luas Persegi Panjang", luas)
    print("Keliling Persegi Panjang", keliling)

def segitiga(a,t,sisi1,sisi2,sisi3):
    luas = 0.5*a*t
    keliling = sisi1+sisi2+sisi3
    print("Luas Segitiga", "alasnya",a, "tingginya",t, "adalah",luas)
    print("Keliling Segitiga", sisi1,sisi2,sisi3,"adalah",keliling)

def jajar_genjang(a,t,s1,s2,s3,s4):
    luas = a*t
    keliling = s1+s2+s3+s4
    print("Luas Jajar Genjang","alasnya",a,"tingginya",t, "adalah",luas)
    print("Keliling Jajar Genjang", "sisi1",s1,"sisi2",s2,"sisi3",s3,"sisi4",s4, "adalah", keliling)

def belah_ketupat(diagonal1,diagonal2,s1,s2,s3,s4):
    luas = 0.5*diagonal1*diagonal2
    keliling = s1+s2+s3+s4
    print("Luas Belah Ketupat","diagonal1",diagonal1,"diagonal2",diagonal2, "adalah", luas)
    print("Keliling Belah Ketupat", "sisi1",s1,"sisi2",s2,"sisi3",s3,"sisi4",s4, "adalah", keliling)

def layang_layang(diagonal1,diagonal2,s1,s2,s3,s4):
    luas = 0.5*diagonal1*diagonal2
    keliling = s1+s2+s3+s4
    print("Luas Layang-Layang","diagonal 1",diagonal1,"diagonal 2",diagonal2, "adalah", luas)
    print("Keliling Layang-Layang", "sisi1",s1,"sisi2",s2,"sisi3",s3,"sisi4",s4, "adalah", keliling)

def lingkaran(r):
    luas = 3.14*r*r
    keliling = 2*3.14*r
    print("Luas Lingkaran adalah", luas)
    print("Keliling Lingkaran adalah", keliling)