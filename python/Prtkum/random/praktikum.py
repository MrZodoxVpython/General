nama = "wahyu"
umur = 17
tinggi_badan = 189.9
    #print("nama saya adalah {nama}, umur saya str{umur}, tinggi badan {tinggi_badan}")
    print("nama saya " + nama + ", umur saya" + str(umur) + ", tinggi " + str(tinggi_badan))




penjumlahan = a + b 
pengurangan = a - b 
perkalian = a * b
pembagian = a / b 
pangkat = a ** b 
modulus = a % b
bilangan_bulat = a // b 

print(penjumlahan)
print(pengurangan)
print(pembagian)
print(pangkat)
print(modulus)
print(bilangan_bulat)

x = true 
y = False

hasil_and = x and y
hasil_or = x or y
hasil_not = not x

print(hasil_not)


x = 10
x -= 3

print(x)



x += 5 
x -= 3
x *= 2 
x /= 4

#Operator Himpunan

y = {1,2,3}
o = {3,4,5}

gabungan = y | o 

irisan = y & o 

selisih = y-o

selisih_simetris = y ^ o
print(selisih_simetris)


#Operator Ternary

umur = 18
status = "Dewasa" if umur >= 18 else "Belum Dewasa"
print(status)