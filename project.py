from abc import ABC, abstractmethod

class BisaMakan(ABC):
    @abstractmethod
    def makan(self):
        pass

class BisaBergerak(ABC):
    @abstractmethod
    def bergerak(self):
        pass

class KandangInterface(ABC):
    @abstractmethod
    def tambah_hewan(self, hewan):
        pass
    
    @abstractmethod
    def ambil_semua_hewan(self) -> list:
        pass

class PerawatanKandangInterface(ABC):
    @abstractmethod
    def bersihkan(self):
        pass

class HewanTerbang(BisaMakan, BisaBergerak):
    def __init__(self, nama):
        self.nama = nama

    def bergerak(self):
        print(f"{self.nama} sedang terbang.")

    def makan(self):
        print(f"{self.nama} sedang makan.")

class HewanDarat(BisaMakan, BisaBergerak):
    def __init__(self, nama):
        self.nama = nama

    def bergerak(self):
        print(f"{self.nama} sedang berjalan.")
        
    def makan(self):
        print(f"{self.nama} sedang makan.")
        
class Kandang(KandangInterface):
    def __init__(self):
        self.__hewan_list = []

    def tambah_hewan(self, hewan):
        self.__hewan_list.append(hewan)

    def ambil_semua_hewan(self) -> list:
        return list(self.__hewan_list)

class PerawatanKandang(PerawatanKandangInterface):
    def bersihkan(self):
        print("Kandang dibersihkan.")

class KebunBinatang:
    def __init__(self, kandang: KandangInterface, perawatan_kandang: PerawatanKandangInterface):
        self.kandang = kandang
        self.perawatan_kandang = perawatan_kandang
        self.perawatan_hewan = PerawatanHewan(kandang)
    def operasional_harian(self):
        print("=== Operasional Harian Kebun Binatang ===")
        self.perawatan_kandang.bersihkan()
        self.perawatan_hewan.rawat_semua_hewan()
class PerawatanHewan:
    def __init__(self, kandang : KandangInterface):
        self.kandang = kandang
    
    def rawat_semua_hewan(self):
        for hewan in self.kandang.ambil_semua_hewan():
            hewan.makan()
            hewan.bergerak()
            print("---")
kandang = Kandang()
perawatan_kandang = PerawatanKandang()

kandang.tambah_hewan(HewanTerbang("Wyvern"))
kandang.tambah_hewan(HewanTerbang("Griffin"))
kandang.tambah_hewan(HewanDarat("Beruang"))
kandang.tambah_hewan(HewanDarat("Singa"))

kebun = KebunBinatang(kandang, perawatan_kandang)
kebun.operasional_harian()