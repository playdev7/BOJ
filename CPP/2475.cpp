#include <iostream>
using namespace std;


int main() {
 int a, b, c, d, e, verif;
 cin >> a >> b >> c >> d >> e;
 verif = a+b+c+d+e% 10;

 cout << verif;

 return 0;
}
