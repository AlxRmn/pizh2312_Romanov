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

private:
    static int objectCount; // счетчик объектов

public:
    Client() : name(""), address(""), contractNumber("") {
        ++objectCount;
        cout << "[Client] Конструктор по умолчанию\n";
    }

    Client(string n, string a, string c) : name(n), address(a), contractNumber(c) {
        ++objectCount;
        cout << "[Client] Конструктор с параметрами\n";
    }

    virtual ~Client() {
        --objectCount;
        cout << "[Client] Деструктор\n";
    }

    static int getObjectCount() {
        return objectCount;
    }

    virtual void displayClient() const = 0;
};

// Инициализация статического члена класса
int Client::objectCount = 0;

// Частный клиент
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
        cout << "Имя: " << name << ", Адрес: " << address
            << ", Договор: " << contractNumber
            << ", Паспорт: " << passportNumber << endl;
    }
};

// Корпоративный клиент
class CorporateClient : public Client {
private:
    string companyName;
    string taxID;

public:
    CorporateClient(string n, string a, string c, string company, string tin)
        : Client(n, a, c), companyName(company), taxID(tin) {
        cout << "[CorporateClient] Конструктор\n";
    }

    ~CorporateClient() {
        cout << "[CorporateClient] Деструктор\n";
    }

    void displayClient() const override {
        cout << "=== Корпоративный клиент ===\n";
        cout << "Имя: " << name << ", Адрес: " << address
            << ", Договор: " << contractNumber
            << ", Компания: " << companyName
            << ", ИНН: " << taxID << endl;
    }
};

// Основной класс
class RegistrationJournal {
private:
    string organizationName;
    string phoneNumber;
    vector<Client*> clients;
    static int internalClientCount;

public:
    RegistrationJournal() {
        cout << "[RegistrationJournal] Конструктор по умолчанию\n";
    }

    RegistrationJournal(string orgName, string phone)
        : organizationName(orgName), phoneNumber(phone) {
        cout << "[RegistrationJournal] Конструктор с параметрами\n";
    }

    ~RegistrationJournal() {
        for (auto client : clients) {
            delete client;
        }
        clients.clear();
        internalClientCount = 0;
        cout << "[RegistrationJournal] Деструктор\n";
    }

    void setOrganizationInfo(string name, string phone) {
        organizationName = name;
        phoneNumber = phone;
    }

    void addClient(Client* client) {
        clients.push_back(client);
        ++internalClientCount;
    }

    void displayJournal() const {
        cout << "\nЖурнал: " << organizationName << ", Телефон: " << phoneNumber << endl;
        for (const auto& client : clients) {
            client->displayClient();
        }
    }

    static int getInternalClientCount() {
        return internalClientCount;
    }
};

// Инициализация статического поля
int RegistrationJournal::internalClientCount = 0;

int main() {
    cout << "Количество объектов Client до создания: " << Client::getObjectCount() << endl;

    // Создание объекта журнала
    RegistrationJournal journal("Компания Вектор", "+7 999 123 4567");

    journal.addClient(new IndividualClient("Иван Иванов", "Москва", "Д-1", "1234 567890"));
    journal.addClient(new CorporateClient("Петр Петров", "СПб", "Д-2", "ООО Вектор", "1234567890"));
    cout << "Количество объектов Client: " << Client::getObjectCount() << endl;
    cout << "Количество клиентов в журнале: " << RegistrationJournal::getInternalClientCount() << endl;

    journal.displayJournal();

    return 0;
}
