dataCredential = {
    "user": {
        "user1": "pass1",
    },
    "admin": {
        "admin1": "pass1",
    }
}
dataQuiz = {
    "IPA": {
        "Apa fungsi klorofil pada tumbuhan?": "fotosintesis",
        "Apa simbol kimia dari air?": "H2O"
    },
    "Matematika": {
        "Berapakah hasil dari 3 + 5?": "8",
        "Berapakah luas persegi dengan sisi 4 cm?": "16"
    },
    "Agama": {
        "Sebutkan rukun Islam ke-3.": "puasa",
        "Nabi isa dilahirkan dikota?": "madinah"
    },
    "Bahasa": {
        "Apa sinonim dari kata 'cerdas'?": "pintar",
        "Apa antonim dari kata 'kecil'?": "besar"
    }
}

def quiz(kategori, dataQuiz):
    print(f"Quiz {kategori}.")
    if kategori in dataQuiz:
        for pertanyaan, jawaban in dataQuiz[kategori].items():
            jawabanUser = input(f"\n{pertanyaan}\nJawaban: ")
            if jawabanUser == jawaban:                 
                print("\n--=Warning=-> Jawaban kmu benar!")
            else:
                print(f"\n--=Warning=-> Jawabanmu salah. Yang benar adalah ini: {jawaban}")
    else:
        print("\n--=Warning=-> Kategori tidak terdata.")

def userSignUp():
    while True:
        print("\n===Buat akun baru===") 
        user = str(input("Masukkan username: "))
        if user in dataCredential["user"]:
            print("--=Warning=-> Username tidak tersedia. Silakan gunakan username lain.")
        else:
            password = str(input("Masukkan password: "))
            dataCredential["user"][user] = password
            print(f"\n--=Warning=-> {user} berhasil di daftarkan, silahkan Login!")
            menuDashboard()
            break
            
def lihatPengguna():
        print("\nUser credential:")
        user_data = dataCredential["user"].items()
        for username, password in user_data:
            print(f"Username: {username}\nPassword: {password}") 
        print("\nAdmin credential:")
        admin_data = dataCredential["admin"].items()
        for username, password in admin_data:
            print(f"Username: {username}\nPassword: {password}")

def tambahPengguna():
    print("\n=== Tambah Pengguna Baru ===")
    print("1.Tambah pengguna user")
    print("2.Tambah pengguna admin")     
    pilihanPengguna = input("Pilih nomor: ")
    if pilihanPengguna == "1":
        user = input("Masukkan user baru: ")
        if user in dataCredential:
            print("\n--=Warning=-> Username sudah ada. Silakan coba username lain.")
        else:
            password = input("Masukkan password: ")
            dataCredential["user"][user] = password
            print(f"\n--=Warning=-> Pengguna {user} berhasil ditambahkan!")
            menuAdmin()
    elif pilihanPengguna == "2":
        admin = input("Masukkan admin baru: ")
        if admin in dataCredential:
            print("\n--=Warning=-> Username sudah ada. Silakan coba username lain.")
        else:
            password = input("Masukkan password: ")
            dataCredential["admin"][admin] = password
            print(f"\n--=Warning=-> Pengguna {admin} berhasil ditambahkan!")
            menuAdmin()
    else:
        print("\n--=Warning=-> Hanya boleh berupa angka 1/2")

def readQuiz():
    for kategori, pertanyaanJawaban in dataQuiz.items():
        print(f"\nKategori: {kategori}")
        for pertanyaan, jawaban in pertanyaanJawaban.items():
            print(f"  Pertanyaan: {pertanyaan}")
            print(f"  Jawaban: {jawaban}")
    pengaturanQuiz() 

def pengaturanQuiz():
    print("\n=== Pengaturan Quizz ===")
    print("1. Create quiz")
    print("2. Read quiz")
    print("3. Update quiz")
    print("4. Delete quiz")
    print("5. Keluar quiz")
    pQ = input("Masukkan pilihan: ") 
    if pQ == "1":  
        readQuiz()
        kategori = input("Ingin menambahkan quiz ke kategori apa?: ")
        pertanyaan = input("Tambahkan pertanyaan: ")
        jawaban = input("Tambahkan jawaban: ")
        if kategori == "IPA" or kategori == "Matematika" or kategori == "Agama" or kategori == "Bahasa":
            dataQuiz[kategori][pertanyaan] = jawaban
            pengaturanQuiz()
    if pQ == "2":
        readQuiz()
    if pQ == "3": 
        kategori = input("Masukkan kategori yang ingin diperbarui (IPA, Matematika, Agama, Bahasa): ")
        if kategori in dataQuiz:
            pertanyaanList = list(dataQuiz[kategori].keys()) 
            for index, pertanyaan in enumerate(pertanyaanList, 1):
                print(f"{index}. {pertanyaan}") 
            pilihan = int(input("\nPilih nomor pertanyaan yang ingin diubah: "))
            if 1 <= pilihan <= len(pertanyaanList):
                pertanyaanLama = pertanyaanList[pilihan - 1]
            
            pertanyaanBaru = input(f"Masukkan pertanyaan baru untuk menggantikan '{pertanyaanLama}': ")
            jawabanBaru = input("Masukkan jawaban baru: ")
            dataQuiz[kategori][pertanyaanBaru] = dataQuiz[kategori].pop(pertanyaanLama)
            dataQuiz[kategori][pertanyaanBaru] = jawabanBaru
            print("\nPertanyaan dan jawaban berhasil diperbarui.")
            pengaturanQuiz()
        else:
            print("Pilihan tidak valid.")
    if pQ == "4":
        readQuiz()
        kategori = input("Masukkan kategori Quiz yang ingin dihapus?: ")
        del dataQuiz[kategori]
        pengaturanQuiz()
    if pQ == "5":
        exit()

def menuUser():
    while True:
        print("\n=== WELCOME TO CLASH OF CHAMPIONS ===") 
        print("Daftar Quiz Tersedia:")
        print("1. Quiz IPA")
        print("2. Quiz Matematika")
        print("3. Quiz Agama")
        print("4. Quiz Bahasa")
        print("5. Keluar")
        pilihan = input("Masukkan nomor: ")
        if pilihan == "1":
            quiz("Ipa", dataQuiz)
        elif pilihan == "2":
            quiz("Matematika", dataQuiz)
        elif pilihan == "3":
            quiz("Agama", dataQuiz)
        elif pilihan == "4":
            quiz("Bahasa", dataQuiz)
        elif pilihan == "5":
            break
        else:
            print("\n--=Warning=-> Pilihan gak valid, pilih berdasarkan nomor!")

def perbaruiPengguna():
    lihatPengguna()
    userOrAdmin = input("\nPerbarui credential 'user' atau 'admin'?: ")
    if userOrAdmin == "user" or userOrAdmin == "admin":
        usernameOrPassword = input(f"Perbarui 'username' atau 'password'?: ") 
        if usernameOrPassword == "username":
            userLama = input(f"Masukkan username '{userOrAdmin}' yang ingin diperbarui: ")
            userBaru = input("Ingin diubah ke apa?: ")
            dataCredential[userOrAdmin][userBaru] = dataCredential[userOrAdmin].pop(userLama)
            print(f"\nCredential {userOrAdmin} dengan username '{userLama}' berhasil diperbarui menjadi '{userBaru}'")
        elif usernameOrPassword == "password":
            pwLama = input(f"Masukkan password '{userOrAdmin}' yang ingin diperbarui: ")
            pwBaru = input("Ingin diubah ke apa?: ")
            dataCredential[userOrAdmin][pwBaru] = pwLama
            print(f"\nCredential '{userOrAdmin}' dengan password '{pwLama}' berhasil diperbarui menjadi '{pwBaru}'")
        else:
            print("\n--=Warning=-> Terdeteksi typo.")
    else:
        print("\n--=Warning=-> Input tidak valid")
        
def hapusPengguna():
    while True:
        lihatPengguna()
        userOrAdmin = input("Ingin menghapus credential 'user' atau 'admin'?: ")
        dilit = input(f"Masukkan username '{userOrAdmin}' yang ingin dihapus: ")
        if dilit in dataCredential[userOrAdmin]:
            del dataCredential[userOrAdmin][dilit]
            print(f"\n --=Warning=-> Credential {userOrAdmin} dengan username {dilit} berhasil dihapus.")
            break
        else: 
            print("--=Warning-=> Inpot tidak valid.")
            hapusPengguna()

def menuAdmin():
    while True:
        print("\n=== Admin Menu ===")
        print("1. Create New User")
        print("2. Read Credential Akun")
        print("3. Update Credential")
        print("4. Delete Credential")
        print("5. Pengaturan Quiz")
        print("6. Exit")
        pilihan = input("Masukkan menu: ")
        if pilihan == "1":
            tambahPengguna()
        elif pilihan == "2":
            lihatPengguna()
        elif pilihan == "3":
            perbaruiPengguna()
        elif pilihan == "4":
            hapusPengguna()
        elif pilihan == "5":
            pengaturanQuiz()
        elif pilihan == "6":
            exit()
        else:
            print("\n--=Warning=-> Pilihan gk valid. Silakan coba lagi.")

def loginAdmin():
    print("\n=== Admin Login Form! ===")
    username = input("Username: ")
    password = input("Password: ")
    if username in dataCredential["admin"] and dataCredential["admin"][username] == password:
        print(f"\n--=Warning=-> Login berhasil! Welcome, {username}!")
        return True   
    else:
        return False

def loginUser():
    print("\n=== CLASH OF CHAMPIONS USER LOGIN ===") 
    print("=== Silahkan Login terlebih dahulu ===")
    username = input("Username: ")
    password = input("Password: ")
    if username == "$admin" and password == "$admin":
        if loginAdmin():
            menuAdmin()
    if username in dataCredential["user"] and dataCredential["user"][username] == password:
        print(f"\n--=Warning=-> Login berhasil! Selamat datang, {username} :D")
        return True  
    else:
        return False 

def loginVerification():
    while True: 
        if loginUser():
            menuUser()
            break
        else:
            print("\n--=Warning=-> Akun yang anda masukkan salah.")

def menuDashboard(): 
    while True:
        print("\nMenu Dashboard")
        print("1. Login")
        print("2. SignUp")
        who = input("Masukkan pilihan: ")
        if who == "1":
            loginVerification()
            break
        elif who == "2":
            userSignUp()
            break
        else:
            print("\n--=Warning=-> Masukkan (1/2)!\n")

menuDashboard()