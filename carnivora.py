from animal import animal

class carnivora(animal):
    def __init__(self, name, makanan, hidup, berkembangbiak, warnabulu, lamahidup, pernapasan, jenistaring, jeniskuku, kecepatan):
        super().__init__(name, makanan, hidup, berkembangbiak)
        self.warnabulu = warnabulu
        self.lamahidup = lamahidup
        self.pernapasan = pernapasan
        self.jenistaring = jenistaring
        self.jeniskuku = jeniskuku
        self.kecepatan = kecepatan

    def info_carnivora(self):
        super().info_animal(),
        print("warna bulu \t\t\t :", self.warnabulu,
            "\nlama hidup \t\t\t :", self.lamahidup,
            "\npernapasan \t\t\t :", self.pernapasan,
            "\njenis taring \t\t\t :", self.jenistaring,
            "\njenis kuku \t\t\t :", self.jeniskuku,
            "\nkecepatan \t\t\t :", self.kecepatan)

carnivora = carnivora("harimau", "daging", "di darat", "beranak", "coklat", "20 tahun", "paru-paru", "kuat dan tajam", "tajam", "sangat cepat")
carnivora.info_carnivora()

print("===========================")
class carnivora(animal):
    def __init__(self, name, makanan, hidup, berkembangbiak, warnabulu, lamahidup, pernapasan, jenistaring, jeniskuku, kecepatan):
        super().__init__(name, makanan, hidup, berkembangbiak)
        self.warnabulu = warnabulu
        self.lamahidup = lamahidup
        self.pernapasan = pernapasan
        self.jenistaring = jenistaring
        self.jeniskuku = jeniskuku
        self.kecepatan = kecepatan
    def info_carnivora(self):
        super().info_animal(),
        print("warna bulu \t\t\t :", self.warnabulu,
            "\nlama hidup \t\t\t :", self.lamahidup,
            "\npernapasan \t\t\t :", self.pernapasan,
            "\njenis taring \t\t\t :", self.jenistaring,
            "\njenis kuku \t\t\t :", self.jeniskuku,
            "\nkecepatan \t\t\t :", self.kecepatan)
        
carnivora = carnivora("buaya", "daging", "di darat dan di air", "bertelur", "tidak ada", "70 tahun", "paru-paru", "kuat", "bisa merobek dengan cepat", "kurang cepat jika di darat")
carnivora.info_carnivora()