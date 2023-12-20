class animal:
    def __init__(self, nama, makanan, hidup, berkembangbiak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangbiak = berkembangbiak


class Badak(animal):

    def __init__(self, nama, makanan, hidup, berkembangbiak):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangbiak = berkembangbiak

    def hewan(self):
        print(f"Ini adalah {self.nama} ")
        print(f"Hewan ini memakan {self.makanan}")
        print(f"Hidupnya {self.hidup}")
        print(f"Dan berkembang biaknya dengan cara {self.berkembangbiak}")

class Ikan(animal):

    def __init__(self, nama, makanan, hidup, berkembangbiak):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangbiak = berkembangbiak

    def hewan(self):
        print(f"Ini adalah {self.nama} ")
        print(f"Hewan ini memakan {self.makanan}")
        print(f"Hidupnya {self.hidup}")
        print(f"Dan berkembang biaknya dengan cara {self.berkembangbiak}")

class Ular(animal):

    def __init__(self, nama, makanan, hidup, berkembangbiak):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangbiak = berkembangbiak

    def hewan(self):
        print(f"Ini adalah {self.nama} ")
        print(f"Hewan ini memakan {self.makanan}")
        print(f"Hidupnya {self.hidup}")
        print(f"Dan berkembang biaknya dengan cara {self.berkembangbiak}")


badak = Badak("badak", "rumput", "di daratan", "melahirkan")
ikan = Ikan("ikan paus", "daging", "di air", "melahirkan")
ular = Ular("ular sanca", "daging", "di daratan", "bertelur")

badak.hewan()

print("=================================================")

ikan.hewan()

print("=================================================")

ular.hewan()