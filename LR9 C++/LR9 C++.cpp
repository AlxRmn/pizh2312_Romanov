#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <locale>
using namespace std;

class Client {
protected:
    string name;
    string address;
    string contractNumber;

public:
    Client(string n = "", string a = "", string c = "")
        : name(n), address(a), contractNumber(c) {}

    virtual ~Client() {}

    virtual void displayClient() const = 0;

    virtual void save(ostream& out) const {
        out << name << '\n' << address << '\n' << contractNumber << '\n';
    }

    virtual void load(istream& in) {
        getline(in, name);
        getline(in, address);
        getline(in, contractNumber);
    }

    virtual string getType() const = 0;

    friend ostream& operator<<(ostream& out, const Client& c) {
        c.save(out);
        return out;
    }

    friend istream& operator>>(istream& in, Client& c) {
        c.load(in);
        return in;
    }
};

class IndividualClient : public Client {
    string passportNumber;

public:
    IndividualClient(string n = "", string a = "", string c = "", string p = "")
        : Client(n, a, c), passportNumber(p) {}

    void displayClient() const override {
        cout << "=== Частный клиент ===\n"
            << "Имя: " << name << ", Адрес: " << address
            << ", Договор: " << contractNumber << ", Паспорт: " << passportNumber << endl;
    }

    void save(ostream& out) const override {
        out << getType() << '\n';
        Client::save(out);
        out << passportNumber << '\n';
    }

    void load(istream& in) override {
        Client::load(in);
        getline(in, passportNumber);
    }

    string getType() const override {
        return "Individual";
    }
};

class CorporateClient : public Client {
    string companyName;
    string taxID;

public:
    CorporateClient(string n = "", string a = "", string c = "", string company = "", string tin = "")
        : Client(n, a, c), companyName(company), taxID(tin) {}

    void displayClient() const override {
        cout << "=== Корпоративный клиент ===\n"
            << "Имя: " << name << ", Адрес: " << address
            << ", Договор: " << contractNumber
            << ", Компания: " << companyName << ", ИНН: " << taxID << endl;
    }

    void save(ostream& out) const override {
        out << getType() << '\n';
        Client::save(out);
        out << companyName << '\n' << taxID << '\n';
    }

    void load(istream& in) override {
        Client::load(in);
        getline(in, companyName);
        getline(in, taxID);
    }

    string getType() const override {
        return "Corporate";
    }
};

class RegistrationJournal {
    vector<Client*> clients;

public:
    ~RegistrationJournal() {
        for (auto* c : clients) delete c;
    }

    void addClient(Client* c) {
        clients.push_back(c);
    }

    void displayAll() const {
        for (const auto& c : clients) c->displayClient();
    }

    void saveToFile(const string& filename) const {
        ofstream out(filename);
        if (!out) {
            cerr << "Ошибка открытия файла для записи.\n";
            return;
        }

        out << clients.size() << '\n';
        for (const auto& c : clients) {
            c->save(out);
        }

        out.close();
    }

    void loadFromFile(const string& filename) {
        ifstream in(filename);
        if (!in) {
            cerr << "Ошибка открытия файла для чтения.\n";
            return;
        }

        for (auto* c : clients) delete c;
        clients.clear();

        size_t count;
        in >> count;
        in.ignore();

        for (size_t i = 0; i < count; ++i) {
            string type;
            getline(in, type);

            Client* c = nullptr;
            if (type == "Individual") {
                c = new IndividualClient();
            }
            else if (type == "Corporate") {
                c = new CorporateClient();
            }
            else {
                cerr << "Неизвестный тип клиента: " << type << endl;
                continue;
            }

            c->load(in);
            clients.push_back(c);
        }

        in.close();
    }
};

int main() {
    setlocale(LC_ALL, "Russian");

    RegistrationJournal journal;
    journal.addClient(new IndividualClient("Иван Иванов", "Москва", "Д-1", "1234 567890"));
    journal.addClient(new CorporateClient("Петр Петров", "СПб", "Д-2", "ООО Вектор", "1234567890"));

    journal.saveToFile("clients.txt");

    RegistrationJournal loadedJournal;
    loadedJournal.loadFromFile("clients.txt");

    cout << "\nЗагруженные клиенты из файла:\n";
    loadedJournal.displayAll();

    return 0;
}
