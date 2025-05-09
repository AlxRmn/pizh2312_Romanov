#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Класс Клиент
class Client {
private:
    string name;
    string address;
    string contractNumber;

public:
    // Конструктор по умолчанию
    Client() : name(""), address(""), contractNumber("") {
        cout << "[Client] Вызван конструктор по умолчанию." << endl;
    }

    // Конструктор с параметрами
    Client(string n, string a, string c) : name(n), address(a), contractNumber(c) {
        cout << "[Client] Вызван конструктор с параметрами." << endl;
    }

    // Конструктор копирования
    Client(const Client& other)
        : name(other.name), address(other.address), contractNumber(other.contractNumber) {
        cout << "[Client] Вызван конструктор копирования." << endl;
    }

    // Деструктор
    ~Client() {
        cout << "[Client] Вызван деструктор." << endl;
    }

    // Перегрузка метода для установки данных
    void setClient(string n, string a, string c) {
        name = n;
        address = a;
        contractNumber = c;
    }

    void setClient(string n, string a) {
        name = n;
        address = a;
        contractNumber = "Не указан";
    }

    void setClient(string n) {
        name = n;
        address = "Не указан";
        contractNumber = "Не указан";
    }

    // Метод для отображения информации о клиенте
    void displayClient() const {
        cout << "Имя: " << name << ", Адрес: " << address << ", Номер договора: " << contractNumber << endl;
    }
};

