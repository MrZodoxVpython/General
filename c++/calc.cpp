#include <iostream>
using namespace std;

int main() {
    double num1, num2;
    char op;

    // Input dari pengguna
    cout << "Masukkan angka pertama: ";
    cin >> num1;
    cout << "Masukkan operator (+, -, *, /): ";
    cin >> op;
    cout << "Masukkan angka kedua: ";
    cin >> num2;

    // Switch untuk menentukan operasi
    switch(op) {
        case '+':
            cout << "Hasil: " << num1 + num2 << endl;
            break;
        case '-':
            cout << "Hasil: " << num1 - num2 << endl;
            break;
        case '*':
            cout << "Hasil: " << num1 * num2 << endl;
            break;
        case '/':
            if(num2 != 0) {
                cout << "Hasil: " << num1 / num2 << endl;
            } else {
                cout << "Error: Pembagian dengan nol!" << endl;
            }
            break;
        default:
            cout << "Operator tidak valid!" << endl;
    }

    return 0;
}
