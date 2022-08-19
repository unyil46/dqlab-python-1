#Encapsulation pada Python – Part 2
#https://academy.dqlab.id/main/livecode/161/302/1362?pr=0
# Definisikan class Karyawan
class Karyawan: 
    nama_perusahaan = 'ABC' 
    __insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan): 
        self.__nama = nama
        self.__usia = usia 
        self.__pendapatan = pendapatan 
        self.__pendapatan_tambahan = 0
    def lembur(self):
        self.__pendapatan_tambahan += self.__insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.__pendapatan_tambahan +=insentif_proyek 
    def total_pendapatan(self):
        return self.__pendapatan + self.__pendapatan_tambahan
# Buat objek karyawan bernama Aksara
aksara = Karyawan('Aksara', 25, 8500000)
# Akses ke attribute class Karyawan
print(aksara.__class__.nama_perusahaan)
# Akan menimbulkan error ketika di run
print(aksara.__nama)

#Inheritance pada Python – Part 1
#https://academy.dqlab.id/main/livecode/161/302/1365?pr=0
#Definisikan class Karyawan (sebagai base class)
class Karyawan: 
    nama_perusahaan = 'ABC' 
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
# Buat class turunan (sebagai inherit class) dari class karyawan, 
# yaitu class AnalisData
class AnalisData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
    # melakukan pemanggilan konstruktur class Karyawan 
        super().__init__(nama, usia, pendapatan)
# Buat kembali class turunan (sebagai inherit class) dari class karyawan,  
# yaitu class IlmuwanData
class IlmuwanData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        # melakukan pemanggilan konstruktur class Karyawan 
        super().__init__(nama, usia, pendapatan)
# Buat objek karyawan yang bekerja sebagai AnalisData
aksara = AnalisData('Aksara', 25, 8500000)
aksara.lembur()
print(aksara.total_pendapatan())
# Buat objek karyawan yang bekerja sebagai IlmuwanData
senja = IlmuwanData('Senja', 28, 13000000)
senja.tambahan_proyek(2000000)
print(senja.total_pendapatan())

#Inheritance pada Python – Part 2
#https://academy.dqlab.id/main/livecode/161/302/1370?pr=0
# Definisikan class Karyawan (sebagai base class)
class Karyawan: 
    nama_perusahaan = 'ABC' 
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
# Buat class turunan (sebagai inherit class) dari class karyawan, 
# yaitu class AnalisData
class AnalisData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
    # melakukan pemanggilan konstruktur class Karyawan 
        super().__init__(nama, usia, pendapatan)
# Buat kembali class turunan (sebagai inherit class) dari class karyawan,  
# yaitu class IlmuwanData
class IlmuwanData(Karyawan):
    # mengubah atribut insentif_lembur yang digunakan pada fungsi lembur()
    insentif_lembur = 500000
    def __init__(self, nama, usia, pendapatan): 
        super().__init__(nama, usia, pendapatan)
# Buat objek karyawan yang bekerja sebagai AnalisData
aksara = AnalisData('Aksara', 25, 8500000)
aksara.lembur()
print(aksara.total_pendapatan())
# Buat objek karyawan yang bekerja sebagai IlmuwanData
senja = IlmuwanData('Senja', 28, 13000000)
senja.lembur()
print(senja.total_pendapatan())
