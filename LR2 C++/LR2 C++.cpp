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

class RegistrationJournal {
private:
    string organizationName;
    string phoneNumber;
    vector<Client> clients; // Массив объектов клиентов

public:
    // Конструктор по умолчанию
    RegistrationJournal() {
        cout << "[RegistrationJournal] Вызван конструктор по умолчанию." << endl;
    }

    // Конструктор с параметрами
    RegistrationJournal(string orgName, string phone) : organizationName(orgName), phoneNumber(phone) {
        cout << "[RegistrationJournal] Вызван конструктор с параметрами." << endl;
    }

    // Конструктор копирования
    RegistrationJournal(const RegistrationJournal& other)
        : organizationName(other.organizationName), phoneNumber(other.phoneNumber), clients(other.clients) {
        cout << "[RegistrationJournal] Вызван конструктор копирования." << endl;
    }

    // Деструктор
    ~RegistrationJournal() {
        cout << "[RegistrationJournal] Вызван деструктор." << endl;
    }

    // Метод установки информации об организации
    void setOrganizationInfo(string name, string phone) {
        organizationName = name;
        phoneNumber = phone;
    }

    // Метод добавления клиента
    void addClient(const Client& client) {
        clients.push_back(client);
    }

    // Новый метод: создание клиента через конструктор с параметрами и добавление в массив
    void createAndAddClient(string n, string a, string c) {
        Client newClient(n, a, c); // вызывается конструктор с параметрами
        addClient(newClient);
    }

    // Новый метод: копирование клиента N раз и добавление в массив
    void copyAndAddClient(const Client& client, int count) {
        for (int i = 0; i < count; ++i) {
            Client copiedClient(client); // вызывается конструктор копирования
            addClient(copiedClient);
        }
    }

    // Метод отображения всей информации
    void displayJournal() const {
        cout << "\nОрганизация: " << organizationName << endl;
        cout << "Телефон: " << phoneNumber << endl;
        cout << "Клиенты:" << endl;
        for (const auto& client : clients) {
            client.displayClient();
        }
    }
};
