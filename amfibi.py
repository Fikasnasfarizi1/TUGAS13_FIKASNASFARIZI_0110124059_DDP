from animal import animal

class amfibi(animal):
    def __init__(self, name, makanan, hidup, berkembangbiak, jenis_air, pernapasan):
        super().__init__(name, makanan, hidup, berkembangbiak)
        self.jenis_air = jenis_air
        self.pernapasan = pernapasan

    def info_amfibi(self):
        super().info_animal(),
        print("jenis air \t\t\t :", self.jenis_air,
            "\npernapasan \t\t\t :", self.pernapasan)
        
amfibi = amfibi("katak", "serangga", "2 alam", "bertelur", "air tawar", "kulit dan paru-paru")
amfibi.info_amfibi()
print("=========================")
def __init__(self, name, makanan, hidup, berkembangbiak, jenis_air, pernapasan):
    super().__init__(name, makanan, hidup, berkembangbiak)
    self.jenis_air = jenis_air
    self.pernapasan = pernapasan
    
    def info_amfibi(self):
        super().info_animal(),
        print("jenis air \t\t\t :", self.jenis_air,
            "\npernapasan \t\t\t :", self.pernapasan)

amfibi = amfibi("salamander", "ikan kecil", "di air dan di darat", "bertelur", "air tawar", "paru-paru dan kulit")
amfibi.info_amfibi()