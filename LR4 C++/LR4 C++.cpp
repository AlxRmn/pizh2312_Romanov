#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Абстрактный базовый класс Client
class Client {
protected:
    string name;
    string address;
    string contractNumber;

public:
    Client() : name(""), address(""), contractNumber("") {
        cout << "[Client] Конструктор по умолчанию\n";
    }

    Client(string n, string a, string c) : name(n), address(a), contractNumber(c) {
        cout << "[Client] Конструктор с параметрами\n";
    }

    virtual ~Client() {
        cout << "[Client] Деструктор\n";
    }

    virtual void displayClient() const = 0;
};

// Класс-наследник — частное лицо
class IndividualClient : public Client {
private:
    string passportNumber;

public:
    IndividualClient(string n, string a, string c, string p)
        : Client(n, a, c), passportNumber(p) {
        cout << "[IndividualClient] Конструктор\n";
    }

    ~IndividualClient() {
        cout << "[IndividualClient] Деструктор\n";
    }

    void displayClient() const override {
        cout << "=== Частный клиент ===\n";
        cout << "Имя: " << name << ", Адрес: " << address << ", Договор: " << contractNumber
            << ", Паспорт: " << passportNumber << endl;
    }
};