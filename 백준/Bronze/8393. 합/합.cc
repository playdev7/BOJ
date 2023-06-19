// n이 주어졌을때 1부터 n 까지의 모든 자연수의 합 출력시키기.
// 팩토리얼같은 방식으로 곱셈 말고 덧셈.

#include <stdio.h>

int main() {
    int n, result=0; // for문 위한 변수 0으로 초기화. 메모리에 임의 값 할당되지 않도록.
    scanf("%d", &n);
    
    for(int i=0; i<=n; i++) {
        result += i;
    }// 덧셈 반복. n만큼.
    
    printf("%d", result);
    
    return 0;
}