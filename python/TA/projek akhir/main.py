import json
import os
import threading

data = {
    "user": {
        "user1": "pass1",
    },
    "admin": {
        "admin1": "pass1",
    }
}

def logiya():
    while True: 
        if loginUser():
            menuUser()
        else:
            os.system('cls')
            print("Akun yang anda masukkan salah !!")

def loginPrompt(): 
        print("Login Dashboard")
        print("1. Login")
        print("2. SignUp")
        who = input("Masukkan pilihan: ")
        if who == "1":
            logiya()
        if who == "2":
            userSignUp()
        else:
            print("=!= Masukkan (1/2) =!=")
    
def loginUser():
    print("\n=== WELCOME TO CLASH OF CHAMPIONS ===") 
    print("=== Silahkan Login terlebih dahulu ===")
    username = input("Username: ")
    password = input("Password: ")
    if username == "$admin" and password == "$admin":
        if loginAdmin():
            menuAdmin()
    if username in data["user"] and data["user"][username] == password:
        print(f"Login berhasil! Selamat datang, {username}")
        return True   
    else:
        print("Username atau password salah. Silakan coba lagi.")
        return False 

def loginAdmin():
    print("=== Admin Login Form! ===")
    username = input("Username: ")
    password = input("Password: ")
    if username in data["admin"] and data["admin"][username] == password:
        print(f"\nLogin berhasil! Welcome, {username}!")
        return True   
    else:
        print("Username atau password salah. Silakan coba lagi.")
        return False

def menuUser():
    data = load_questions()
    while True:
        print("\nSelamat datang in Quizz")
        print("Pilih Quiz test yang akan anda kerjakan:")
        print("1. Quiz IPA")
        print("2. Quiz Matematika")
        print("3. Quiz Agama")
        print("4. Quiz Bahasa")
        print("5. Exit ke menu after login")
        pilihan = input("Masukkan nomor pilihan: ")
        if pilihan == "1":
            quiz("IPA", data)
        elif pilihan == "2":
            quiz("Matematika", data)
        elif pilihan == "3":
            quiz("Agama", data)
        elif pilihan == "4":
            quiz("Bahasa", data)
        elif pilihan == "5":
            print("All program are used, thanks!")
            break
        else:
            print("Pilihan gak valid, back to menu")
       
def load_questions():
    with open('data.json', 'r') as file:
        return json.load(file)        

def timeout_function():
    print("Waktu habis!")  

def quiz(subject, data):
    print(f"Quiz {subject}.")
    for item in data[subject]:
        question = item["question"]
        answer = item["answer"]

        timer = threading.Timer(15.0, timeout_function)
        timer.start()  
        user_answer = input(f"{question}, 15 detik untuk menjawab!\nJawaban: ")
        timer.cancel()
        if user_answer.lower() == answer.lower():
            print("Benar!")
        else:
            print(f"Salah. Jawaban yang benar adalah: {answer}")

def pengaturanQuiz():
    print("1. Lihat daftar quiz")
    print("2. Tambah daftar quiz")
    print("3. Update quiz")
    print("4. Hapus quiz")
    pQ = input("Masukkan pilihan:") 
    if pQ == "1":
        data = load_questions()
        for kategori, daftar_qa in data.items():
            print(f"Kategori: {kategori}")
            print("-" * 50)
    
            for item in daftar_qa:
                print(f"Pertanyaan: {item['question']}")
                print(f"Jawaban: {item['answer']}")
                print("-" * 20)  
                print("=" * 50)
    if pQ == "2":
        data = load_questions()
        print(data)
        print(data)
        print(data)
        print(data)
        print(data)
        print(data)
        print(data)

def menuAdmin():
    while True:
        print("\n=== Admin Menu ===")
        print("1. Create New User")
        print("2. Read Credential")
        print("3. Pengaturan Quizz")
        print("4. Kembali ke menu login")
        pilihan = input("Masukkan menu: ")
        if pilihan == "1":
            tambahPengguna()
        elif pilihan == "2":
            lihatPengguna()
        elif pilihan == "3":
            pengaturanQuiz()
        elif pilihan == "4":
            break
        else:
            print("Pilihan gk valid. Silakan coba lagi.")

def userSignUp():
        user = input("Masukkan username: ")
        if user in data:
            print("Username sudah ada. Silakan coba username lain.")
        else:
                password = input("Masukkan password: ")
                data["user"][user] = password
                print(f"Akun {user} berhasil di daftarkan!")
                loginPrompt()

def lihatPengguna():
        print("\nUser credential:")
        user_data = data["user"].items()
        for username, password in user_data:
            print(f"Username: {username}\nPassword: {password}") 
        print("\nAdmin credential:")
        admin_data = data["admin"].items()
        for username, password in admin_data:
            print(f"Username: {username}\nPassword: {password}")

def tambahPengguna():
        print("\n--- Tambah Pengguna Baru ---")
        print("1.Tambah pengguna user")
        print("2.Tambah pengguna admin")    
        try:
            pilihanPengguna = int(input("Pilih nomor: ")) 
            if pilihanPengguna == 1:
                user = input("Masukkan user baru: ")
                if user in data:
                    print("Username sudah ada. Silakan coba username lain.")
                else:
                    password = input("Masukkan password: ")
                    data["user"][user] = password
                    print(f"Pengguna {user} berhasil ditambahkan!")
                    menuAdmin()
            if pilihanPengguna == 2:
                admin = input("Masukkan admin baru: ")
                if admin in data:
                   print("Username sudah ada. Silakan coba username lain.")
                else:
                    password = input("Masukkan password: ")
                    data["admin"][admin] = password
                    print(f"Pengguna {admin} berhasil ditambahkan!")
                    menuAdmin()
        except ValueError:
            print("\nHanya boleh berupa angka 1/2")
            tambahPengguna()
loginPrompt()