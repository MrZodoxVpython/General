dataKaryawan = []
tuple = ("anjayani")
def addKaryawan(nip,nama,alamat,departemen,jabatan):
    dataKaryawan.append(nip)
    dataKaryawan.append(nama)
    dataKaryawan.append(alamat)
    dataKaryawan.append(departemen)
    dataKaryawan.append(jabatan)
    print("Data success added")
    print(dataKaryawan)
    print(dataKaryawan[1])
def readKaryawan():
    pass
def __main__():
    while True:
        print("===== Penambahakan data karyawan baru =====")        
        print("1. Create data karyawan")
        print("2. Read data karyawan") 
        print("3. Update data karyawan")
        print("4. Delete data karyawan")
        print("5. Searching data karyawan")
        print("6. Exit")
        administrator = int(input("Choose options: "))
        if administrator == "1":
            nip = int(input("Masukkan nip: "))
            nama = str(input("Masukkan nama: "))
            alamat = str(input("Masukkan alamat: "))
            departemen = str(input("Masukkan departemen: "))
            jabatan = str(input("Masukkan jabatan: "))
            addKaryawan(nip,nama,alamat,departemen,jabatan)
        if administrator == "2":
            readKaryawan()
__main__()