#include <iostream>
#include <vector>
#include <string>
#include <locale>
#include <stdexcept>
using namespace std;

class Client {
protected:
    string name;
    string address;
    string contractNumber;

private:
    static int objectCount;

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

int Client::objectCount = 0;

class IndividualClient : public Client {
private:
    string passportNumber;

public:
    IndividualClient() : Client(), passportNumber("0000 000000") {
        cout << "[IndividualClient] Конструктор по умолчанию\n";
    }

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

class CorporateClient : public Client {
private:
    string companyName;
    string taxID;

public:
    CorporateClient() : Client(), companyName("Компания"), taxID("0000000000") {
        cout << "[CorporateClient] Конструктор по умолчанию\n";
    }

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

class RegistrationJournal {
private:
    string organizationName;
    string phoneNumber;
    vector<Client*> clients;
    static int internalClientCount;

public:
    RegistrationJournal() {}

    RegistrationJournal(string orgName, string phone)
        : organizationName(orgName), phoneNumber(phone) {}

    ~RegistrationJournal() {
        for (auto client : clients) {
            delete client;
        }
        clients.clear();
        internalClientCount = 0;
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

    RegistrationJournal& operator+(Client* client) {
        addClient(client);
        return *this;
    }

    RegistrationJournal& operator++() {
        addClient(new IndividualClient());
        return *this;
    }

    RegistrationJournal operator++(int) {
        RegistrationJournal temp = *this;
        addClient(new CorporateClient());
        return temp;
    }

    Client* operator[](size_t index) {
        if (index < clients.size()) {
            return clients[index];
        }
        else {
            throw out_of_range("Индекс вне диапазона");
        }
    }

    friend ostream& operator<<(ostream& os, const RegistrationJournal& journal);
};

int RegistrationJournal::internalClientCount = 0;

ostream& operator<<(ostream& os, const RegistrationJournal& journal) {
    os << "\n[Вывод через оператор <<] Журнал организации: " << journal.organizationName
        << ", Телефон: " << journal.phoneNumber << "\n";
    for (const auto& client : journal.clients) {
        client->displayClient();
    }
    return os;
}

int main() {
    setlocale(LC_ALL, "Russian");
    cout << "Количество объектов Client до создания: " << Client::getObjectCount() << endl;

    RegistrationJournal journal("Компания Вектор", "+7 999 123 4567");

    journal + new IndividualClient("Иван Иванов", "Москва", "Д-1", "1234 567890");
    journal + new CorporateClient("Петр Петров", "СПб", "Д-2", "ООО Вектор", "1234567890");

    ++journal;
    journal++;

    try {
        cout << "\n[Доступ по индексу 1]\n";
        journal[1]->displayClient();
    }
    catch (const exception& e) {
        cerr << "Ошибка: " << e.what() << endl;
    }

    cout << journal;

    cout << "Объектов Client: " << Client::getObjectCount() << endl;
    cout << "Клиентов в журнале: " << RegistrationJournal::getInternalClientCount() << endl;

    return 0;
}
