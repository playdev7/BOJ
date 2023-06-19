#include <stdio.h>

int main() {
    int count;
    scanf("%d", &count);
    
    for(int i=1; i <= count; i++) {
        for(int space=count; space>i; space--) {
            printf(" ");
        }
        for(int star=0; star<i; star++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}