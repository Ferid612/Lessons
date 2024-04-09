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


int main() {
    int n,m; cin>>n; m=n; 
    int t =0;
    int k =1;
    while(n!=0){
        t +=1;
        k*=10;
        n=n/10;
    }
    k/=10;
    string poli = "YES";
    for(int i=0; i<t/2 ; i++ ){
        if (m%10 != m/k){
            poli="NO";
            break;
        }
    }
    
    
    cout<<poli;
    return 0;
}




int main() {
    int k;  cin>>k;
    for (int i =1; i< k; i++){
        bool bolunurmu = true;
        int t = i;
        while(t!=0){
            int d= t%10;
            if (d== 0 || i % d !=0){
                bolunurmu = false;
                break;
            }
            t/=10;
        }
        if (bolunurmu){
        cout<<i<<" ";
        }
    }
        
    return 0;
}


int main() {
    int n,k=1,m=k+1;cin>>n;
    string mumkun = "NO";
    for (int i=1;i*i<n; i++){
        for (int j=i+1; j*j<n; j++){
            if (i*i + j*j ==n){
                mumkun="YES";
            }
        }     
    }
    cout<<mumkun;
    return 0;
}


optimize 56
int main() {
    int n;cin>>n;
    for (int i=1; i*i+ 4 <n;i++){
    for (int j=i+1; (i*i + j*j)<=n ;j++){
        if (i*i + j*j <=n)
        cout << i << "^2" <<" + " << j <<"^2" << " = "<<i*i + j*j<<endl;     
    }   
        
    }
    return 0;
}

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    
    int n,k; cin >>n; k=n;
    
    for(int i=n-1;1<=i; i--){
    int t=i;
        for (int j=2;j<t;j++){
            cout<<j;
            if (t%j==0){
                t=t/j;
                
            }
        }
        k=k*t;
        cout<<" K: " <<k <<endl;
    }
    cout<<k; 
    return 0;
}
