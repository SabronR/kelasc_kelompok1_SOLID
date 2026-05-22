from abc import ABC, abstractmethod

class BisaMakan(ABC):
    @abstractmethod
    def makan(self):
        pass

class BisaBergerak(ABC):
    @abstractmethod
    def bergerak(self):
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
        print(f"(self.nama) sedang makan.")
        
class Kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

class PerawatanKandang:
    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")

class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang()

class PerawatanHewan:
    def __init__(self, kandang):
        self.kandang = kandang
    
    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            hewan.bergerak()
        
