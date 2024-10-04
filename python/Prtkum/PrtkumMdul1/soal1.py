panjang = 20
lebar = 13    
diameter = 14
luasSelimut = 440
tinggibalok = 7
phi = 22/7
jariJari = diameter / 2

#rumus t=LS/(2 * phi * r)
#440 / 44 = 10
tinggi_tabung = luasSelimut / (2 * phi * jariJari)  
#20 * 13 * 10 = 2600
volume_balok = panjang * lebar * tinggibalok
#rumus V=phi * r2 * t
# 22/7 * 49 * 10 = 1540
volume_tabung = phi * (jariJari ** 2) * tinggi_tabung

print(f"Hasil volume celengan balok adalah: {volume_balok}")
print(f"Hasil volume celengan tabung adalah: {volume_tabung}")