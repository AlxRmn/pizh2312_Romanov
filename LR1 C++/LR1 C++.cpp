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
};