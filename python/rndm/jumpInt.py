krakter = input("Mau membalikkan apa?: ") 
hasilTerbalik = ""


if krakter[0] == '-':
   
    krakter = krakter[1:]  
    for iterasi in krakter:
        hasilTerbalik = iterasi + hasilTerbalik
    hasilTerbalik = '-' + hasilTerbalik  

print(hasilTerbalik)