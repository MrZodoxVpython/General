import json

data = {
    "user": {
        "user1": "password1",
        "user2": "password2"
    },
    "admin": {
        "admin1": "password1",
        "admin2": "password2"
    }
}

def loginPrompt(): 
        print("Menu")
        print("1. User Login")
        print("2. Admin Login")
        who = input("Masukkan pilihan: ")
        if who == "1":
            while True:
                if loginUser():
                    menuQuiz()
        if who == "2":
            while True:
                if loginAdmin():
                    menuAdmin()
        else:
            print("=!= Masukkan (1/2) =!=")
    
def loginUser():
    print("\n=== Selamat datang di Quiz International ===") 
    print("=== Silahkan Login dulu ===")
    username = input("Username: ")
    password = input("Password: ")
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
        print(f"Login berhasil! Welcome, {username}!")
        return True   
    else:
        print("Username atau password salah. Silakan coba lagi.")
        return False

def load_questions():
    with open('data.json', 'r') as file:
        return json.load(file)

def menuQuiz():
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

def quiz(subject, data):
    print(f"Quiz {subject}.")
    for item in data[subject]:
        question = item["question"]
        answer = item["answer"]
        user_answer = input(f"{question}\nJawaban: ")
        if user_answer.lower() == answer.lower():
            print("Benar!")
        else:
            print(f"Salah. Jawaban yang benar adalah: {answer}")

def menuAdmin():
    while True:
        print("\n=== Admin Menu ===")
        print("1. Create New User")
        print("2. Read Credential")
        print("3. Masuk Ke Menu Quizz")
        print("4. Kembali ke menu login")
        pilihan = input("Masukkan menu: ")
        if pilihan == "1":
            tambahPengguna()
        elif pilihan == "2":
            lihatPengguna()
        elif pilihan == "3":
            menuQuiz()
        elif pilihan == "4":
            break
        else:
            print("Pilihan gk valid. Silakan coba lagi.")
def lihatPengguna():
        print("\nUser credential:")
        user_data = data["user"].items()
        for username, password in user_data:
            print(f"Username: {username}, Password: {password}") 
            print("\nAdmin credential:")
        admin_data = data["admin"].items()
        for username, password in admin_data:
            print(f"Username: {username}, Password: {password}")
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
            
# def timeout_function():
#     print("Waktu habis!")
# timer = threading.Timer(30.0, timeout_function)
# timer.start()
# answer = input("Jawaban Anda (30 detik untuk menjawab): ")
# timer.cancel()
# print("Jawaban Anda:", answer)    

loginPrompt()