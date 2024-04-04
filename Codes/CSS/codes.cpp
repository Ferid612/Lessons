using namespace std;
#include <iostream>

int main(int argc, char *argv[]) {
   
    int a = 10;
    int b = 15;

    cout << std::boolalpha;

    cout << "a = " << a << ", b = " << b << endl;

    cout << "(a < b):  " << (a < b) << endl;
    cout << "(a > b):  " << (a > b) << endl;
    cout << "(a == b): " << (a == b) << endl;
    cout << "(a != b): " << (a != b) << endl;
    cout << "(a <= b): " << (a <= b) << endl;    // (a < b) || (a == b)
    cout << "(a >= b): " << (a >= b) << endl;

    
}