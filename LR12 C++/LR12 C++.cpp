#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <locale>
using namespace std;

class Client {
private:
    string name;
    string address;
    string contractNumber;

public:
    Client() : name(""), address(""), contractNumber("") {}
    Client(string n, string a, string c) : name(n), address(a), contractNumber(c) {}
    Client(const Client& other)
        : name(other.name), address(other.address), contractNumber(other.contractNumber) {}

    void setClient(string n, string a, string c) {
        name = n; address = a; contractNumber = c;
    }

    void displayClient() const {
        cout << "Имя: " << name << ", Адрес: " << address << ", Договор: " << contractNumber << endl;
    }

    string getName() const { return name; }
    string getAddress() const { return address; }
    string getContractNumber() const { return contractNumber; }
};

int main() {
    setlocale(LC_ALL, "Russian");

    vector<Client> clients = {
        Client("Иван Иванов", "Москва", "Д-1"),
        Client("Пётр Петров", "СПб", "Д-3"),
        Client("Алексей Смирнов", "Новосибирск", "Д-2"),
        Client("Мария Иванова", "Екатеринбург", "Д-4"),
        Client("Ольга Кузнецова", "Казань", "Д-5")
    };

    sort(clients.begin(), clients.end(), [](const Client& a, const Client& b) {
        return a.getName() > b.getName();
        });

    cout << "Клиенты отсортированы по убыванию имени:\n";
    for (const auto& client : clients) client.displayClient();

    auto it = find_if(clients.begin(), clients.end(), [](const Client& c) {
        return c.getAddress() == "СПб";
        });

    if (it != clients.end()) {
        cout << "\nНайден клиент с адресом СПб:\n";
        it->displayClient();
    }

    vector<Client> filteredClients;
    auto new_end = remove_copy_if(clients.begin(), clients.end(), back_inserter(filteredClients), [](const Client& c) {
        return c.getName().empty() || c.getName()[0] != 'И';
        });

    clients.erase(remove_if(clients.begin(), clients.end(), [](const Client& c) {
        return !c.getName().empty() && c.getName()[0] == 'И';
        }), clients.end());

    cout << "\nОтфильтрованные клиенты (имя начинается с 'И'):\n";
    for (const auto& client : filteredClients) client.displayClient();

    sort(clients.begin(), clients.end(), [](const Client& a, const Client& b) {
        return a.getName() < b.getName();
        });

    sort(filteredClients.begin(), filteredClients.end(), [](const Client& a, const Client& b) {
        return a.getName() < b.getName();
        });

    cout << "\nОставшиеся клиенты, отсортированные по возрастанию имени:\n";
    for (const auto& client : clients) client.displayClient();

    cout << "\nФильтрованные клиенты, отсортированные по возрастанию имени:\n";
    for (const auto& client : filteredClients) client.displayClient();

    return 0;
}
