// n을 입력하면 n*1 부터 n*9까지 반복하여 출력해주는 프로그램.
// "n * 1 = a" 형태로 줄바꿔가며 출력.

#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    for(int i=1; i<=9; i++) {
        printf("%d * %d = %d\n", n, i, n*i);
    }
    
    return 0;
}