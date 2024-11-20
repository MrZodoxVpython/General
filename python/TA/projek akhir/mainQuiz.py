import subprocess
import threading

def timeout_function():
    print("Waktu habis!")
timer = threading.Timer(30.0, timeout_function)
timer.start()
answer = input("Jawaban Anda (30 detik untuk menjawab): ")
timer.cancel()
print("Jawaban Anda:", answer)

userData = { 
    "username1": "password1",  
    "username2": "password2"
}

def loginPrompt():
    while True:
        if loginM():
            menuBerhasil() 
def loginM():
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

def tambahPengguna():
    print("\n--- Tambah Pengguna Baru ---")
    username = input("Masukkan username baru: ")

    if username in userData:
        print("Username sudah ada. Silakan coba username lain.")
    else:
        password = input("Masukkan password: ")
        userData[username] = password
        print(f"Pengguna {username} berhasil ditambahkan!")

def menuBerhasil():
    while True:
        print("\n--- Menu Opsional ---")
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
            menu_quiz()
        elif pilihan == "5":
            tambahPengguna()
            break
        else:
            print("Pilihan gk valid. Silakan coba lagi.")

def menu_quiz():
    print("\n--- Masuk ke Menu Quizz ---")
    menu()

def menu():
    while True:
        print("\nSelamat datang in Quizz")
        print("Pilih Quiz test yang akan anda kerjakan:")
        print("1. Quiz IPA")
        print("2. Quiz Matematika")
        print("3. Quiz Agama")
        print("4. Quiz Bahasa")
        print("5. Keluar")  
        pilihan = input("Masukkan nomor pilihan: ")

        if pilihan == "1":
            ipa()
        elif pilihan == "2":
            matematika()
        elif pilihan == "3":
            agama()
        elif pilihan == "4":
            bahasa()
        elif pilihan == "5":
            print("All program are used, thanks!")
            break
        else:
            print("Pilihan gak valid, back to menu")

def ipa():
    print("Quiz IPA. (Pertanyaan)")

def matematika():
    print("Matematika. (Pertanyaan)")

def agama():
    print("Quiz Agama. (Pertanyaan")

def bahasa():
    print("Quiz Bahasa. (Pertanyaan)")

def menu_quiz():
    menu()
    print("\n--- batas waktu ---")
    timeout_function()
    menuBerhasil()
loginPrompt()