#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    int n,k;
    cin >> n;
    k=n;
    int count = 0;
    int max = 1;

    while (n > 0)
    {

        int tail = n % 10;
        if (max < tail)
            max = tail;

        n = n / 10;
    }
    cout << "max: " << max<<endl;
    while (k > 0)
    {
        int tail = k % 10;
        if (max == tail)
            count = count + 1;

        k = k / 10;

    }

    cout << count << endl;
}

// int main()
// {
//     int n;
//     cin >> n;

//     float matrix[n][n];

//     for (int i = 0; i < n; i++)
//     {
//         for (int j = 0; j < n; j++)
//         {
//             cin >> matrix[i][j];
//         }
//     }
//     for (int i = 0; i < n; i++)
//     {
//         bool isas_or_isdesc = true;
//         int d = matrix[i][1] - matrix[i][0];
//         for (int j = 1; j < n - 1; j++)
//         {
//             if (d > 0 && matrix[i][j] - matrix[i][j - 1] <= 0)
//             {
//                 isas_or_isdesc = false;
//                 break;
//             }
//             if (d < 0 && matrix[i][j] - matrix[i][j + 1] >= 0)
//             {
//                 isas_or_isdesc = false;
//                 break;
//             }
//         }
//         if (isas_or_isdesc)
//         {
//             cout << i + 1 << " ";
//         }
//     }
// }
// void degree()
// {
//     int f = n;
//     for (int i = 0; i < n / 2; i++)
//     {
//         int b = f - 1;
//         int t f - 1;
//         for (int j = 1; j < f1; j++)
//         {
//             int a = matr[i][j];
//             matr[i][j] = matr[b][i];
//             matr[b][i] = matr[t][b];
//             matr[t][b] = matr[j][t];
//             matr[j][t] = a;
//             b--;
//         }
//         f--;
//     }
//     for (int i = 0; i < n; i++)
//     {
//         for (int j = 0; j < n; j++)
//         {
//             cout >> matr[i][j] << " ";
//         }
//         cout << endl;
//     }
// }

// int main() {
//     char a,b; cin>>a>>b;
//     a = a+b;
//     b = a-b;
//     a = a-b;
//     cout << a <<b;
//     return 0;
// }
// int main() {
//     int n; cin>>n;
//     int a = n/ 10000;
//     int b = n/1000%10;
//     int c = n/100%10;
//     int d = n/10%10;
//     int e = n%10;

//     cout << a <<b<<c<<d<<e<<t<<endl;
//     if (a<=b and b<=c and c<=d and d<=e){
//         cout << "Ascending";
//     }else{
//         cout<<"Not Ascending";
//     }
//     return 0;
// }

// int main() {
//     int n; cin>>n;
//     int a = n/ 10000;
//     int b = n/1000%10;
//     int c = n/100%10;
//     int d = n/10%10;
//     int e = n%10;
//     if (a==b || a==c || a==d || a==e || b ==c || b==d ||  b==e  || c ==d || c==e || d==e){
//         cout<<"Identical Digits Found";
//     }else{
//         cout<<"No Identical Digits";
//     }
//     return 0;
// }

// int main() {
//     int n; cin>>n;
//     int a = n / 100;
//     int b = n %100;
//     b = (b%10)*10 + b/10;
//     a == b ? cout << "Palindrome" :  cout<< "Not Palindrome"<<endl<<endl;
//     return 0;
// }

// polindrom

// 18. Digit Sum Difference

// int main() {
//     int n; cin>>n;
//     int a = n / 1000;
//     int sum_a = a%10 + a/10;
//     int b = n % 100;
//     int sum_b = b%10 + b/10;
//     cout<< sum_a - sum_b;

//     return 0;
// }

// int main() {
//     int n,m; cin>>n; m=n;
//     int t =0;
//     int k =1;
//     while(n!=0){
//         t +=1;
//         k*=10;
//         n=n/10;
//     }
//     k/=10;
//     string poli = "YES";
//     for(int i=0; i<t/2 ; i++ ){
//         if (m%10 != m/k){
//             poli="NO";
//             break;
//         }
//     }

//     cout<<poli;
//     return 0;
// }

// int main() {
//     int k;  cin>>k;
//     for (int i =1; i< k; i++){
//         bool bolunurmu = true;
//         int t = i;
//         while(t!=0){
//             int d= t%10;
//             if (d== 0 || i % d !=0){
//                 bolunurmu = false;
//                 break;
//             }
//             t/=10;
//         }
//         if (bolunurmu){
//         cout<<i<<" ";
//         }
//     }

//     return 0;
// }

// int main() {
//     int n,k=1,m=k+1;cin>>n;
//     string mumkun = "NO";
//     for (int i=1;i*i<n; i++){
//         for (int j=i+1; j*j<n; j++){
//             if (i*i + j*j ==n){
//                 mumkun="YES";
//             }
//         }
//     }
//     cout<<mumkun;
//     return 0;
// }

// optimize 56
// int main() {
//     int n;cin>>n;
//     for (int i=1; i*i+ 4 <n;i++){
//     for (int j=i+1; (i*i + j*j)<=n ;j++){
//         if (i*i + j*j <=n)
//         cout << i << "^2" <<" + " << j <<"^2" << " = "<<i*i + j*j<<endl;
//     }

//     }
//     return 0;
// }

// #include <cmath>
// #include <cstdio>
// #include <vector>
// #include <iostream>
// #include <algorithm>
// using namespace std;

// int main() {

//     int n,k; cin >>n; k=n;

//     for(int i=n-1;1<=i; i--){
//     int t=i;
//         for (int j=2;j<t;j++){
//             cout<<j;
//             if (t%j==0){
//                 t=t/j;

//             }
//         }
//         k=k*t;
//         cout<<" K: " <<k <<endl;
//     }
//     cout<<k;
//     return 0;
// }
//     return 0;
// }
// int main() {
//         /* Enter your code here. Read input from STDIN. Print output to STDOUT */
//         float a,b,c,d; cin>>a>>b>>c>>d;
//         if (a < b && b< c && c< d){
//             cout<< a<<" "<<b<<" " <<c<<" "<<d;
//         }else if(a >= b && b>= c && c>= d){
//             float max_t = a>b?a:b;
//             max_t = max_t>c?max_t:c;
//             max_t = max_t>d?max_t:d;

//             cout<< max_t<<" "<<max_t<<" " <<max_t<<" "<<max_t;

//         }else{
//             cout<< a*a<<" "<<b*b<<" "<<c*c<<" "<<d*d;
//         }
//         return 0;
//     }

// float a,b,c,d; cin>>a>>b>>c>>d;
// float max_t = a>b?a>c?a>d?a:d:c>d?c:d:b>c?b>d?b:d:c>d?c:d;
