total_orang = 7
orang_pilih = 4

#faktorial hasil kali semua bilangan bulat
faktorial_total = total_orang * 6 * 5 * 4 * 3 * 2 * 1 
faktorial_pilih = orang_pilih * 3 * 2 * 1 
faktorial_selisih = (total_orang - orang_pilih) * 2 * 1
# 5040 // 24 * 6 
# 5040 // 144 = 35
jumlah_cara = faktorial_total // (faktorial_pilih * faktorial_selisih)


print(f"Banyak cara untuk membentuk tim: {jumlah_cara}")