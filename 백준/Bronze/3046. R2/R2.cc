#include <iostream>
using namespace std; // 표준 네임스페이스 사용

int r1, r2, s; // 전역변수 선언

int main() {
    cin >> r1 >> s; // r1 s 입력받기
    r2 = s*2-r1; // r2를 구하는 공식
    
    cout << r2; // r2를 출력
    
    return 0; // 프로그램 종료를 알림.
}