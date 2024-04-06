#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n; cin>>n; 
    int a = n / 100;
    int b = n %100;
    b = (b%10)*10 + b/10;
    a == b ? cout << "Palindrome" :  cout<< "Not Palindrome";
    return 0;
}


// polindrom




// 18. Digit Sum Difference

int main() {
    int n; cin>>n;
    int a = n / 1000;
    int sum_a = a%10 + a/10;
    int b = n % 100;
    int sum_b = b%10 + b/10;
    cout<< sum_a - sum_b;
    
    return 0;
}
