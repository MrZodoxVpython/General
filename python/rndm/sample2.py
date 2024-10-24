krakter = input("Masukkan nilai: ")
hasilTerbalik = ""

if krakter.isdigit():
    for iterasi in krakter:
        hasilTerbalik = iterasi + hasilTerbalik
    print(hasilTerbalik)
else:
    print("Input harus bilangan bulat!")