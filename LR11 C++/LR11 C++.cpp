#include <iostream>
#include <vector>
#include <string>
#include <algorithm>  
#include <locale>
using namespace std;

class Service {
protected:
    string serviceName;
    double price;

public:
    Service() : serviceName(""), price(0.0) {}
    Service(string s, double p) : serviceName(s), price(p) {}

    virtual ~Service() {}

    virtual void display() const {
        cout << "Услуга: " << serviceName << ", Цена: " << price << endl;
    }

    virtual bool operator<(const Service& other) const {
        return price < other.price;
    }

    virtual bool operator>(const Service& other) const {
        return price > other.price;
    }
};

class InternetService : public Service {
private:
    int speed;

public:
    InternetService() : Service(), speed(0) {}
    InternetService(string s, double p, int spd) : Service(s, p), speed(spd) {}

    void display() const override {
        cout << "Интернет-услуга: " << serviceName << ", Цена: " << price << ", Скорость: " << speed << " Мбит/с" << endl;
    }

    int getSpeed() const { return speed; }

    bool operator<(const InternetService& other) const {
        return price < other.price;
    }

    bool operator>(const InternetService& other) const {
        return price > other.price;
    }
};

int main() {
    setlocale(LC_ALL, "ru_RU.UTF-8");

    vector<InternetService> services = {
        InternetService("Интернет A", 700, 30),
        InternetService("Интернет B", 1200, 100),
        InternetService("Интернет C", 1600, 200),
        InternetService("Интернет D", 900, 70),
        InternetService("Интернет E", 1100, 50)
    };

    sort(services.begin(), services.end(), [](const InternetService& a, const InternetService& b) {
        return a > b;
        });

    cout << "Контейнер после сортировки по убыванию:" << endl;
    for (const auto& s : services) s.display();

    auto it = find_if(services.begin(), services.end(), [](const InternetService& s) {
        return s.getSpeed() > 50;
        });

    if (it != services.end()) {
        cout << "\nНайден первый элемент с скоростью > 50:" << endl;
        it->display();
    }
    else {
        cout << "\nЭлемент с скоростью > 50 не найден." << endl;
    }

    vector<InternetService> filteredServices;
    auto partitionPoint = partition(services.begin(), services.end(), [](const InternetService& s) {
        return s.getSpeed() <= 50;
        });

    // Копируем удовлетворяющие условию элементы в filteredServices
    copy(partitionPoint, services.end(), back_inserter(filteredServices));
    // Удаляем их из первого контейнера
    services.erase(partitionPoint, services.end());

    cout << "\nВторой контейнер (скорость > 50):" << endl;
    for (const auto& s : filteredServices) s.display();

    sort(services.begin(), services.end(), [](const InternetService& a, const InternetService& b) {
        return a < b;
        });

    sort(filteredServices.begin(), filteredServices.end(), [](const InternetService& a, const InternetService& b) {
        return a < b;
        });

    cout << "\nПервый контейнер после сортировки по возрастанию:" << endl;
    for (const auto& s : services) s.display();

    cout << "\nВторой контейнер после сортировки по возрастанию:" << endl;
    for (const auto& s : filteredServices) s.display();

    return 0;
}
