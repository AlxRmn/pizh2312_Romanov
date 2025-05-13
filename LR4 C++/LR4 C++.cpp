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
// Класс-наследник — корпоративный клиент
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
        cout << "Имя: " << name << ", Адрес: " << address << ", Договор: " << contractNumber
            << ", Компания: " << companyName << ", ИНН: " << taxID << endl;
    }
};

// Основной класс — Журнал регистрации
class RegistrationJournal {
private:
    string organizationName;
    string phoneNumber;
    vector<Client*> clients;

public:
    RegistrationJournal() {
        cout << "[RegistrationJournal] Конструктор по умолчанию\n";
    }

    RegistrationJournal(string orgName, string phone)
        : organizationName(orgName), phoneNumber(phone) {
        cout << "[RegistrationJournal] Конструктор с параметрами\n";
    }

    ~RegistrationJournal() {
        cout << "[RegistrationJournal] Деструктор\n";
        for (auto client : clients) {
            delete client;
        }
    }

    void setOrganizationInfo(string name, string phone) {
        organizationName = name;
        phoneNumber = phone;
    }

    void addClient(Client* client) {
        clients.push_back(client);
    }

    void displayJournal() const {
        cout << "\nЖурнал регистрации — " << organizationName << ", Телефон: " << phoneNumber << endl;
        for (const auto& client : clients) {
            client->displayClient();
        }
    }
};

int main() {
    // Создание массива клиентов базового типа
    vector<Client*> clientArray;

    clientArray.push_back(new IndividualClient("Иван Иванов", "Москва", "Договор #1", "1234 567890"));
    clientArray.push_back(new CorporateClient("Сергей Смирнов", "СПб", "Договор #2", "ООО Ромашка", "7701234567"));

    cout << "\n=== Вывод клиентов из массива ===\n";
    for (auto client : clientArray) {
        client->displayClient();
    }

    // Очистка массива
    for (auto client : clientArray) {
        delete client;
    }
    clientArray.clear();

    // Работа с журналом регистрации
    RegistrationJournal journal("Компания Рога и Копыта", "+7 123 456-7890");

    journal.addClient(new IndividualClient("Петр Петров", "Казань", "Договор #3", "9876 543210"));
    journal.addClient(new CorporateClient("Анна Кузнецова", "Екатеринбург", "Договор #4", "ООО Ландыш", "5509876543"));

    journal.displayJournal();

    return 0;
}