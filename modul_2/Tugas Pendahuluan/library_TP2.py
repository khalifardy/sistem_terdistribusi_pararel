class KalkulatorSederhana:

    def __init__(self,angka1,angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def tambah(self):
        return self.angka1 + self.angka2
    
    def kurang(self):
        return self.angka1 - self.angka2
    
    def kali(self):
        return self.angka1 * self.angka2
    
    def bagi(self):
        try:
            return self.angka1/self.angka2
        except ZeroDivisionError:
            print("Pembagian dengan nol tidak dijinkan")

