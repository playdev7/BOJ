#include <stdio.h>

int main() {
    //실수 표현 해야하므로 double 형
    double A, B;
    
    //입력도 Long Float
    scanf("%lf", &A);
    scanf("%lf", &B);
    
    double result = A/B;
    
    //소수점 이하 12자리 출력
    printf("%.12lf", result);
    
    return 0;
}
