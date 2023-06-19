// 첫 번째 입력은 토탈 금액 X
// 두 번째 입력은 구매한 상품 수 N
// 세 번째 부터는 구매한 상품수 만큼 1개당 가격 a, 수량 b
/* 예시
X = 260000
N = 4
a0, b0 = 20000 5
a1, b1 = 30000 2
a2, b2 = 10000 6
a3, b3 = 5000 8
*/ 
// 세번째부터 받은 품목과 가격의 합이 첫번째 값과
// 일치하면 Yes, 아니면 No 출력.


#include <stdio.h>

int main() {
    int X, N, a, b, total=0;
    
    scanf("%d", &X);
    scanf("%d", &N);
    
    for(int i=0; i<N; i++) {
        scanf("%d %d", &a, &b);
        total += a*b;
    } // N 입력한 만큼 반복해서 품목 및 가격 반복 연산.
    
    if(total==X) {
        printf("Yes");
    }
    else {
        printf("No");
    } // X랑 Total 맞으면 Yes, 아니면 No 출력.
    
    return 0;
}