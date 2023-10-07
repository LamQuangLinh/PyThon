from datetime import datetime

class SinhVien:
    truong = "Đại học Đà Lạt"
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh
        
    @property
    def maSo(self):
        return self.__maSo
    
    @maSo.setter
    def maSo(self, maSo):
        if self.laMaSoHopLe(maSo):
            self.__maSo = maSo
            
    @staticmethod
    def laMaSoHopLe(maSo: int):
        return len(str(maSo)) == 7
    
    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    
    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")
        
