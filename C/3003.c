#include <stdio.h>

int main() {
    int ref[6]={1,1,2,2,2,8};
    int white[6];
    int i;
    
    for(i=0; i<6; i++)
        scanf("%d", &white[i]);
    
    for(i=0; i<6; i++)
        printf("%d", ref[i]-white[i]);
    
    return 0;
}
