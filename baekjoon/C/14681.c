/* 가로축 x 세로축 y
    x,y 모두 양수이면 1사분면
    x음수이고 y양수이면 2사분면
    x,y 모두 음수이면 3사분면
    x양수이고 y음수이면 4사분면
*/

#include <stdio.h>
int main() {
    int x, y;
    scanf("%d %d", &x, &y);
    
    if(0<x && 0<y){
        printf ("1");
    }//1사분
    else if(x<0 && 0<y) {
        printf ("2");
    }//2사분
    else if(x<0 && y<0){
        printf ("3");
    }//3사분
    else if(0<x && y<0){
        printf ("4");
    }//4사분
    else {
        printf("0");
    }//0, 0은 0
        
    return 0;
}
