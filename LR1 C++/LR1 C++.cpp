#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Client {
private:
    string name;
    string address;
    string contractNumber;

public:
    Client() : name(""), address(""), contractNumber("") {}

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

    void displayClient() const {
        cout << "Имя: " << name << ", Адрес: " << address << ", Номер договора: " << contractNumber << endl;
    }
}; class RegistrationJournal {
private:
    string organizationName;
    string phoneNumber;
    vector<Client> clients; 

public:
   
    void setOrganizationInfo(string name, string phone) {
        organizationName = name;
        phoneNumber = phone;
    }

    void addClient(const Client& client) {
        clients.push_back(client);
    }

    void displayJournal() const {
        cout << "Организация: " << organizationName << endl;
        cout << "Телефон: " << phoneNumber << endl;
        cout << "Клиенты:" << endl;
        for (const auto& client : clients) {
            client.displayClient();
        }
    }
};


int main() {

    RegistrationJournal journal;
    journal.setOrganizationInfo("Компания Рога и Копыта", "+7-123-456-7890");

    Client client1;
    client1.setClient("Иван Иванов", "г. Москва", "Договор №123");

    Client client2;
    client2.setClient("Петр Петров", "г. Санкт-Петербург");

    Client client3;
    client3.setClient("Сидор Сидоров");

    journal.addClient(client1);
    journal.addClient(client2);
    journal.addClient(client3);

    journal.displayJournal();

    return 0;
}