#include <stdio.h>
    
int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    
    if (a>b) {
      printf(">\n");  
    }
    else if (a<b) {
      printf("<");
    }
    else if (a==b) {
        printf("==");
    }
    else {
        return 0;
    }
    
    return 0;
}
