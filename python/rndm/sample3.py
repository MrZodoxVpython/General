while True: 
    hariSewa = int(input("Berapa hari sewa kamu?: "))
        
    batasPinjam = 5 #hari
    dendaHarian = 2500 #Rp
    batasDendaTambahan = 10 #hari
    dendaTambahan = 5500 #Rp
    total_denda = 0
    
    if hariSewa > batasPinjam:
        keterlambatan = hariSewa - batasPinjam 
        total_denda += keterlambatan * dendaHarian

        if keterlambatan > batasDendaTambahan:
            tambahanHari = (keterlambatan - batasDendaTambahan +4) // 5
            total_denda += tambahanHari * dendaTambahan

    print(f"Total denda keterlambatan: Rp {total_denda}")

    hitunglagi = input("Mau hitung lagi? (ya/no): ")
    if hitunglagi == 'no':
        print("Program stopped")
        break