siswa = {
    "nama" : "Budi",
    "umur" : 17,
    "kelas" : "10A",
    "FavoriteColor" : ["Yellow","Red","Blue"],
    "ppp" : True
}
print("")
print(siswa)
print(siswa["FavoriteColor"][0])
siswa["kelas"] = "11B"
print(siswa["kelas"])

#insert data
siswa["sekolah"] = "Sman 1 mjokerto"
print(siswa["sekolah"])

#deleted elemen
del siswa ["ppp"]
print(siswa)

#dictionary bersarang
siswa1 = {
     "nama" : "alam",
     "umur" : 16,
     "nilai" : {
         "Matematika" : 80,
         }

}


print(siswa1["nilai"]["Matematika"])



#------
siswa1["nilai"]["mipa"] = 30
print(siswa1)


#set
buah = {"apel","Jeruk","mangga",True, 12, 183.38}
print("")
print(buah)
buah.add("HII")
print(buah)
buah.remove("HII")
print(buah)


buah.update(





