from SinhVien import SinhVien
from SinhVienChinhQuy import SinhVienChinhQuy
from SinhVienPhiChinhQuy import SinhVienPhiChinhQuy
import datetime

class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []
        
    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)
        
    def xuat(self):
        for sv in self.dssv:
            print(sv)
            
    def timSVTheoMSSV(self, mssv: int):
        return [sv for sv in self.dssv if sv.mssv == mssv]

    def timVTSVTheoMSSV(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
            else:
                return -1
    
    def xoaSVTheoMSSV(self, maSo: int) -> bool:
        vt = self.timVTSVTheoMSSV(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
        
    def timSVTheoTen(self, hoTen: str):
        return [sv for sv in self.dssv if sv.hoTen == hoTen]
    
    def timSVSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngaySinh - ngay < 0]
    
    def DocTuFile(self, tenFile):
        with open(tenFile, 'r', encoding='utf-8') as f:
            for hang in f:
                dl = hang.split('*')
                ms = int(dl[0])
                ht = dl[1]
                ns = datetime.strptime(dl[2], "%d/%m/%Y")
                sv = SinhVien(ms, ht, ns)
                self.themSinhVien(sv)
    
    def SapXepTangTheoTen(self):
        return self.dssv.sort(key = lambda x: x.__hoTen, reverse=False)
    
    def SapXepGiamTheoTen(self):
        return self.dssv.sort(key = lambda x: x.__hoTen, reverse=True)
    
    def TimSinhVienTheoLoai(self, loai: str):
        if loai == "chinhquy":
            return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
        else:
            return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiChinhQuy)]
        
    def TimSinhVien_DiemRL(self, diemRL):
        # for sv in self.dssv:
        #     if isinstance(sv, SinhVienChinhQuy) and sv.diemRL > diemRL:
        #         print(sv)
        return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy) and sv.diemRL > diemRL]
    
    # def TimSinhVienTheo_ThoiGian(self, daySV: datetime):
    #     # daySV = datetime.datetime.strptime(daySV, "%d/%m/%y")
    #     for sv in self.dssv:
    #         if isinstance (sv, SinhVienPhiChinhQuy):
    #             if sv.__ngaySinh.year < daySV.datetime.year:
    #                 print(sv)
    #             elif sv.__ngaySinh.year == daySV.datetime.year:
    #                 if sv.__ngaySinh.month < daySV.datetime.month:
    #                     print(sv)
    #                 elif sv.__ngaySinh.month == daySV.datetime.month:
    #                     if sv.__ngaySinh.day < daySV.datetime.month:
    #                         print(sv)
                    

ds = DanhSachSV()
# ds.DocTuFile('DSSV.txt')
svcq1 = SinhVienChinhQuy(2111982, "Đinh Đặng Đình", datetime.datetime(2000, 8, 18), 79)
svcq2 = SinhVienChinhQuy(2111983, "Nguyễn Đức Đại Lộc", datetime.datetime(2001, 9, 11), 81)
svpcq1 = SinhVienPhiChinhQuy(2110282, "Lâm Lệ Lạnh", datetime.datetime(1999, 8, 14), "Tiểu học", 5)
sv1 = SinhVien(2115232, "Lâm Quang Linh", datetime.datetime(2003, 2, 15))
ds.themSinhVien(sv1)
ds.themSinhVien(svcq1)
ds.themSinhVien(svcq2)
ds.themSinhVien(svpcq1)
ds.xuat()
loai = str(input("Nhập loại muốn tìm (chinhquy / kochinhquy): "))
kq = ds.TimSinhVienTheoLoai(loai)
for i in kq:
    print(i)
diemRL = int(input("Mời nhập điểm RL: "))
kq2 = ds.TimSinhVien_DiemRL(diemRL)
for a in kq2:
    print(i)
    
d1 = str(input("Mời nhập thời gian muốn tìm (day / month/ year): "))
daySV = datetime.datetime.strptime(d1, "%d/%m/%y")
ds.TimSinhVienTheo_ThoiGian(daySV)

# ds.xuat()
# ds.SapXepTangTheoTen()
# mssv = str(input("Mời nhập mã số muốn tìm: "))
# ds.timSVTheoMSSV(mssv)
# ds.SapXepTangTheoTen()