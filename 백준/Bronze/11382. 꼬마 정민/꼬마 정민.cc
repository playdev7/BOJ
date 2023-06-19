#include <stdio.h>
// 10^12 범위 -> long long 자료형 사용.
int main() {
    long long a, b, c;
    scanf("%lld %lld %lld", &a, &b, &c);
    printf("%lld", a+b+c);
    
    return 0;
}