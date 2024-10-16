waktuTempuhSaya = 0
waktuTotalKeKampus = 50
waktuMakan = 10
waktuMandi = 15
waktuMotor = 15
waktuJalanKaki = 30
print("SELAMAT DATANG DI SEMANGAT NGAMPUS CODE!!!!")

cek = input("Apakah kamu sudah makan atau mandi hari ini? (yes/no): ")
saya = "mahasiswa"

if cek == 'no':
    waktuTotalKeKampus -= waktuMakan
    waktuTotalKeKampus -= waktuMandi
    totalWaktu = waktuTotalKeKampus
    print(f"Waktu ke kampus anda hilang {waktuMakan} menit untuk makan dlu")
    print(f"Waktu ke kampus anda hilang {waktuMandi} menit untuk mandi dulu")
    print(f"Anda punya sisa waktu ke kampus {totalWaktu}")
    trans = input("Mau naik apa ke kampus? (motor/jalanKaki): ")
    if trans == 'motor':
        waktuTotalKeKampus -= waktuMotor
    else:
        waktuTotalKeKampus -= waktuJalanKaki
if cek == 'yes':
    sports = str(input("Mau naik transportasi apa?(motor/jalanKaki): "))    
    if sports == 'motor':
        waktuTotalKeKampus -= waktuMotor
    else:
        waktuTotalKeKampus -= waktuJalanKaki
if waktuTotalKeKampus >= 1:
    print(f"anda punya waktu {waktuTotalKeKampus}, selamat anda ngampus tepat waktu")
else:
        print("Anda tidak tepat waktu ke kampus")