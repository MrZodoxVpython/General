#rumus beda suku deret
#Un=a+(n−1)d 
#n=posisi suku 
U5 = 11  #representasi deret dari a + 4d
suku_ke_8_dan_suku_ke_12 = 52  #representasi deret dari a + 7d dan a + 11d
n = 8

# menghitung total kontribusi suku yang terlibat(mencari selisih posisi)
# U8​+U12−2U5​=(2a+18d)−(2a+8d)= 10d 

#menghitung untuk beda deret
# 52 - 22 / 10 = 3
d = (suku_ke_8_dan_suku_ke_12 - 2 * U5) / 10
#mencari nilai suku pertama
# 11 - 12 = -1
a = U5 - 4 * d
#substitusi nilai
#(8/2=4) * (2*-1=-2 + 7*3=21 = 19)
jumlah_8_suku = (n / 2) * (2 * a + (n - 1) * d)


print(f"Jumlah dari 8 suku pertama adalah {jumlah_8_suku}")