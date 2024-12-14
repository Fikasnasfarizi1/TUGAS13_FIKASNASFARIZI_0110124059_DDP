from animal import animal

class mamalia(animal):
    def __init__(self, name, makanan, hidup, berkembangbiak, warna_bulu, lama_hidup, pernapasan):
        super().__init__(name, makanan, hidup, berkembangbiak)
        self.warna_bulu = warna_bulu
        self.lama_hidup = lama_hidup
        self.pernapasan = pernapasan

    def info_mamalia(self):
        super().info_animal(),
        print("warna bulu \t\t\t :", self.warna_bulu,
            "\nlama hidup \t\t\t :", self.lama_hidup,
            "\npernapasan \t\t\t :", self.pernapasan)

mamalia = mamalia("Anjing", "tulang", "di darat", "beranak", "putih, hitam, dan coklat", "13 sampai 20 tahun", "paru-paru")
mamalia.info_mamalia()
print("======================")
class mamalia(animal):
    def __init__(self, name, makanan, hidup, berkembangbiak, warna_bulu, lama_hidup, pernapasan):
        super().__init__(name, makanan, hidup, berkembangbiak)
        self.warna_bulu = warna_bulu
        self.lama_hidup = lama_hidup
        self.pernapasan = pernapasan
    
    def info_mamalia(self):
        super().info_animal(),
        print("warna bulu \t\t\t :", self.warna_bulu,
            "\nlama hidup \t\t\t :", self.lama_hidup,
            "\npernapasan \t\t\t :", self.pernapasan)

mamalia = mamalia("kucing", "ikan", "di darat", "beranak", "putih, hitam, dan cokelat", "13 sampai 20 tahun", "paru-paru")
mamalia.info_mamalia()