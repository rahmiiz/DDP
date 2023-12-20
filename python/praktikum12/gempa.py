class gempa:
    lokasi = ''
    skala = 0

    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            ket = ("Dampak gempa tidak berasa")
        elif self.skala < 2 and self.skala > 4:
            ket = ("Dampak gempa bangunan retak-retak")
        elif self.skala < 4 and self.skala > 6:
            ket = ("Dampak gempa bangunan roboh")
        else:
            ket = ("Dampak gempa bangunan roboh dan berpotensi tsunami")

        print(f'Lokasi:{self.lokasi}')
        print(f'Skala: {self.skala}')
        print(f'Keterangan:{ket}')