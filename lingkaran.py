import math
print("PROGRAM MENGHITUNG LINGKARAN")
print("1. keliling lingkaran")
print("2. luas lingkaran")
pilihan = int(input("masukkan pilihan(1/2): "))
r = float(input("masukkan jari-jari: "))
if pilihan == 1:
    keliling = 2 * math.pi * r
    print("keliling lingkaran =", keliling)
elif pilihan == 2:
    luas = math.pi * r * r
    print("Luas lingkaran =", luas)
else:
    print("pilihan tidak tersedia!")        

