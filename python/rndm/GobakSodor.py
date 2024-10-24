jumlah_pemain = int(input("Masukkan jumlah pemain: "))
nama_pemain = []  
posisi_pemain = [0] * jumlah_pemain 
garis_batas = 10  
pemenang = ""

for i in range(jumlah_pemain):
    nama = input(f"Masukkan nama pemain {i + 1}: ")
    nama_pemain.append(nama)

while jumlah_pemain > 0:
    for i in range(len(nama_pemain)):
       
        aksi_pemain = input(f"{nama_pemain[i]}, masukkan aksi (maju/kembali): ")
 
        if aksi_pemain.lower() == "maju":
            posisi_pemain[i] += 1
        elif aksi_pemain.lower() == "kembali":
            posisi_pemain[i] -= 1
      
        if posisi_pemain[i] >= garis_batas:
            pemenang = nama_pemain[i]
            print(f"Pemain {pemenang} Menang!")
            jumlah_pemain -= 1
            break 

if pemenang:
    print("Pemenangnya adalah:", pemenang)
