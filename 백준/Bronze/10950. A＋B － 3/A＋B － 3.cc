#include <stdio.h>

int main() {
    int howmany, a, b;
    
    scanf("%d", &howmany);
    
    for(int i=0; i!=howmany; i++) {
        scanf("%d %d", &a, &b);
        printf("%d\n", a+b);
    }
    
    return 0;
}