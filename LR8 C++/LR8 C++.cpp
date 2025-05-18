#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>
#include <locale>

using namespace std;

class MyLogicError : public logic_error {
public:
    MyLogicError(const string& msg) : logic_error(msg) {}
};

class MyRuntimeError : public runtime_error {
public:
    MyRuntimeError(const string& msg) : runtime_error(msg) {}
};

class Client {
protected:
    string name;
    string address;
    string contractNumber;

public:
    Client(string n = "", string a = "", string c = "") : name(n), address(a), contractNumber(c) {}
    virtual ~Client() {}
    virtual void displayClient() const = 0;
};

class IndividualClient : public Client {
private:
    string passportNumber;

public:
    IndividualClient(string n, string a, string c, string p)
        : Client(n, a, c), passportNumber(p) {
        if (p.empty()) throw invalid_argument("Паспорт не может быть пустым");
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
    CorporateClient(string n, string a, string c, string comp, string tin)
        : Client(n, a, c), companyName(comp), taxID(tin) {
        if (taxID.length() != 10)
            throw length_error("ИНН должен содержать 10 символов");
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
    vector<Client*> clients;

public:
    RegistrationJournal(string org = "") : organizationName(org) {}

    ~RegistrationJournal() {
        for (auto c : clients) delete c;
        clients.clear();
    }

    void addClient(Client* c) {
        if (!c) throw MyRuntimeError("Попытка добавить null-клиента!");
        clients.push_back(c);
    }

    Client* getClient(size_t index) {
        if (index >= clients.size()) throw out_of_range("Индекс вне границ в журнале");
        return clients[index];
    }

    void displayJournal() {
        try {
            if (clients.empty()) throw MyLogicError("Журнал пуст, нечего отображать");
            for (auto c : clients) c->displayClient();
        }
        catch (const MyLogicError& e) {
            cout << "[Локальная обработка] Ошибка: " << e.what() << endl;
        }
    }
};

void nestedCallThrow() {
    throw string("Вложенная строковая ошибка");
}

void anotherNested() {
    throw 42;  
}

int main() {
    setlocale(LC_ALL, "Russian");

    RegistrationJournal journal("Компания Тест");

    try {
        try {
            journal.addClient(new IndividualClient("Иван", "Москва", "Д-1", "1234 567890"));
            journal.addClient(new CorporateClient("Петр", "СПб", "Д-2", "ООО Альфа", "123456789")); // Ошибка длины
        }
        catch (const length_error& le) {
            cout << "[Поймано] std::length_error: " << le.what() << endl;
        }

        try {
            journal.getClient(10)->displayClient(); // Ошибка диапазона
        }
        catch (const out_of_range& e) {
            cout << "[Поймано] std::out_of_range: " << e.what() << endl;
        }

        journal.displayJournal();

        try {
            nestedCallThrow();
        }
        catch (const string& s) {
            cout << "[Поймано] Исключение string: " << s << endl;
        }

        try {
            anotherNested();
        }
        catch (int code) {
            cout << "[Поймано] Исключение int: " << code << endl;
        }

        journal.addClient(nullptr); // Собственное исключение
    }
    catch (const MyRuntimeError& e) {
        cout << "[Поймано] MyRuntimeError: " << e.what() << endl;
    }
    catch (const exception& e) {
        cout << "[Поймано] Стандартное исключение: " << e.what() << endl;
    }
    catch (...) {
        cout << "[Поймано] Неизвестное исключение (catch(...))\n";
    }

    return 0;
}