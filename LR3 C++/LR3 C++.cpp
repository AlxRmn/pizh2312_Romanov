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
    Client() : name(""), address(""), contractNumber("") {
        cout << "[Client] Вызван конструктор по умолчанию." << endl;
    }

    Client(string n, string a, string c) : name(n), address(a), contractNumber(c) {
        cout << "[Client] Вызван конструктор с параметрами." << endl;
    }

    Client(const Client& other)
        : name(other.name), address(other.address), contractNumber(other.contractNumber) {
        cout << "[Client] Вызван конструктор копирования." << endl;
    }

    ~Client() {
        cout << "[Client] Вызван деструктор." << endl;
    }

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
};

// ДОПОЛНИТЕЛЬНЫЙ БАЗОВЫЙ КЛАСС
class Service {
protected:
    string serviceName;
    double price;

public:
    Service() : serviceName(""), price(0.0) {
        cout << "[Service] Конструктор по умолчанию\n";
    }

    Service(string s, double p) : serviceName(s), price(p) {
        cout << "[Service] Конструктор с параметрами\n";
    }

    virtual ~Service() {
        cout << "[Service] Деструктор\n";
    }

    virtual void input() {
        cout << "Введите название услуги: ";
        cin >> serviceName;
        cout << "Введите цену: ";
        cin >> price;
    }

    virtual void display() const {
        cout << "Услуга: " << serviceName << ", Цена: " << price << endl;
    }
};

// Класс-наследник: интернет-услуга
class InternetService : public Service {
private:
    int speed;

public:
    InternetService() : Service(), speed(0) {
        cout << "[InternetService] Конструктор по умолчанию\n";
    }

    InternetService(string s, double p, int spd) : Service(s, p), speed(spd) {
        cout << "[InternetService] Конструктор с параметрами\n";
    }

    ~InternetService() {
        cout << "[InternetService] Деструктор\n";
    }

    void input() override {
        Service::input();
        cout << "Введите скорость интернета (Мбит/с): ";
        cin >> speed;
    }

    void display() const override {
        Service::display();
        cout << "Скорость: " << speed << " Мбит/с" << endl;
    }
};

class PhoneService : public Service {
private:
    int includedMinutes;

public:
    PhoneService() : Service(), includedMinutes(0) {
        cout << "[PhoneService] Конструктор по умолчанию\n";
    }

    PhoneService(string s, double p, int mins) : Service(s, p), includedMinutes(mins) {
        cout << "[PhoneService] Конструктор с параметрами\n";
    }

    ~PhoneService() {
        cout << "[PhoneService] Деструктор\n";
    }

    void input() override {
        Service::input();
        cout << "Введите количество включённых минут: ";
        cin >> includedMinutes;
    }

    void display() const override {
        Service::display();
        cout << "Минут включено: " << includedMinutes << endl;
    }
};

int main() {
    cout << "\n Примеры объектов базового и производных классов" << endl;

    // Объекты базового и производных классов
    Service baseService("Общая услуга", 1500);
    InternetService netService("Домашний интернет", 1000, 100);
    PhoneService phoneService("Мобильная связь", 500, 300);

    baseService.display();
    netService.display();
    phoneService.display();

    cout << "\n Массив объектов базового класса (с наследниками)" << endl;
    vector<Service*> services;
    services.push_back(new Service("Хостинг", 200));
    services.push_back(new InternetService("Интернет 50 Мбит", 800, 50));
    services.push_back(new PhoneService("Звонки Россия", 300, 200));

    for (auto s : services) {
        s->display();
        cout << "------------------------" << endl;
    }

    for (auto s : services) {
        delete s;
    }

    cout << "\n=== Массив объектов одного класса-наследника (InternetService) ===" << endl;
    vector<InternetService> internetPlans = {
        InternetService("Интернет A", 700, 30),
        InternetService("Интернет B", 1200, 100),
        InternetService("Интернет C", 1600, 200)
    };

    for (const auto& plan : internetPlans) {
        plan.display();
        cout << "------------------------" << endl;
    }

    return 0;
}