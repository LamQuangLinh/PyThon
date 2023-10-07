from datetime import datetime
from SinhVien import SinhVien
import datetime

class SinhVienPhiChinhQuy(SinhVien):
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime, trinhdo: str, tgdt: int) -> None:
        super().__init__(maSo, hoTen, ngaySinh)
        self.trinhdo = trinhdo
        self.tgdt = tgdt
        
    def __str__(self) -> str:
        return super().__str__() + f"\t{self.trinhdo}\t{self.tgdt}"