// 직전 문제랑 비슷한데 좀 더 간지나게
// T 만큼 테스트 진행
// 자연수 2개 입력 받고,
// 출력은 "Case #x: A + B = C\n" 형태로 반복.
// 이것도 Case #1 부터 시작.

#include <stdio.h>

int main() {
    int a, b, T;
    scanf("%d", &T);
    
    for(int i=1; i<=T; i++) {
        scanf("%d %d", &a, &b);
        printf("Case #%d: %d + %d = %d\n", i, a, b, a+b);
    }// Case #1 부터 Case#T 까지 반복.
    
    return 0;
}