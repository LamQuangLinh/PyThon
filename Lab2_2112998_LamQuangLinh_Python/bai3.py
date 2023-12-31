# bài 3:
class PhanSo:
    def __init__(self, tu_so: int, mau_so: int) -> None:
        self.tu_so = tu_so
        self.mau_so = mau_so

    def rutGon(self):
        ucln = math.gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln

    def __add__(self, other):
        new_tu_so = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        new_mau_so = self.mau_so * other.mau_so
        return PhanSo(new_tu_so, new_mau_so)

    def __sub__(self, other):
        new_tu_so = self.tu_so * other.mau_so - other.tu_so * self.mau_so
        new_mau_so = self.mau_so * other.mau_so
        return PhanSo(new_tu_so, new_mau_so)

    def __mul__(self, other):
        new_tu_so = self.tu_so * other.tu_so
        new_mau_so = self.mau_so * other.mau_so
        return PhanSo(new_tu_so, new_mau_so)

    def __truediv__(self, other):
        new_tu_so = self.tu_so * other.mau_so
        new_mau_so = self.mau_so * other.tu_so
        return PhanSo(new_tu_so, new_mau_so)

    def __str__(self):
        return f"{self.tu_so}/{self.mau_so}"

a = PhanSo(2,3)
b = PhanSo(3,5)
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")

