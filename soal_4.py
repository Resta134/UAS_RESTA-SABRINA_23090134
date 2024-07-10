class Buah:
    def __init__(self, nama, warna, rasa):
        self.__nama = nama
        self.__warna = warna
        self.__rasa = rasa
    
    def get_nama(self):
        return self.__nama
    
    def get_warna(self):
        return self.__warna
    
    def get_rasa(self):
        return self.__rasa
    
    def set_nama(self, nama): 
        self.__nama = nama

    def set_warna(self, warna): 
        self.__warna = warna

    def set_rasa(self, rasa): 
        self.__rasa = rasa
    
    def info_Buah(self):
        return f'Nama : {self.get_nama()}, Warna : {self.get_warna()}, Rasa : {self.get_rasa()}'
    
class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.__vitamin = vitamin
    
    def get_vitamin(self):
        return self.__vitamin
    
    def set_vitamin(self, vitamin): 
        self.__vitamin = vitamin

    def info_mangga(self):
        return f'Vitamin : {self.get_vitamin()}'

object = Buah('Mangga', 'Hijau', 'Asam')
object_mangga = Mangga('Mangga Manis', 'Kuning', 'Manis', 'Vitamin C')

print(object.info_Buah())
print(object_mangga.info_Buah(), object_mangga.info_mangga())
