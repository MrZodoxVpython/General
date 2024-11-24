import subprocess
import threading
import json

userData = { 
    "user1": "password1",  
    "user2": "password2"
}
adminData = {
    "admin1": "password1",
    "admin2": "password2"
}
def whoami():
    print("Menu")
    print("1. User Login")
    print("2. Admin Login")
    who = input("Masukkan pilihan: ")
    if who == "1":
        userPrompt()
    if who == "2":
        adminPrompt()
    else:
        print("Not Valid!")
def userPrompt():
    while True:
        if loginUser():
            menu() 
def adminPrompt():
    while True:
        if loginAdmin():
            menuAdmin()
def loginUser():
    print("\n=== Selamat datang di Quiz International ===") 
    print("=== Silahkan Login dulu ===")
    username = input("Username: ")
    password = input("Password: ")
    if username in userData and userData[username] == password:
        print(f"Login berhasil! Selamat datang, {username}")
        return True   
    else:
        print("Username atau password salah. Silakan coba lagi.")
        return False 

def loginAdmin():
    print("=== Admin Login Form! ===")
    username = input("Username: ")
    password = input("Password: ")
    if username in adminData and adminData[username] == password:
        print(f"Login berhasil! Welcome, {username}!")
        return True   
    else:
        print("Username atau password salah. Silakan coba lagi.")
        return False

def tambahPengguna():
    print("\n--- Tambah Pengguna Baru ---")
    username = input("Masukkan username baru: ")

    if username in userData:
        print("Username sudah ada. Silakan coba username lain.")
    else:
        password = input("Masukkan password: ")
        userData[username] = password
        print(f"Pengguna {username} berhasil ditambahkan!")

def menuAdmin():
    while True:
        print("\n--- Menu After Login ---")
        print("1. Lihat Profil")
        print("2. Pengaturan Akun")
        print("3. Kembali ke Menu Login")
        print("4. Masuk Ke Menu Quizz")
        print("5. Tambah New User")
        pilihan = input("Masukkan menu: ")
        if pilihan == "1":
            print("Menampilkan profil pengguna...")
        elif pilihan == "2":
            print("Mengakses pengaturan akun...")
        elif pilihan == "3":
            print("Kembali ke menu utama...")
            break
        elif pilihan == "4":
            menu()
        elif pilihan == "5":
            tambahPengguna()
            break
        else:
            print("Pilihan gk valid. Silakan coba lagi.")

def load_questions():
    with open('data.json', 'r') as file:
        return json.load(file)

def menu():
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


# def menu_quiz():
#     menu()
#     print("\n--- batas waktu ---")
#     menuBerhasil()

# def timeout_function():
#     print("Waktu habis!")
# timer = threading.Timer(30.0, timeout_function)
# timer.start()
# answer = input("Jawaban Anda (30 detik untuk menjawab): ")
# timer.cancel()
# print("Jawaban Anda:", answer)    

whoami()