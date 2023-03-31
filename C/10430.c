#include <stdio.h>

int main() {
	int a, b, c;

	scanf("%d %d %d", &a, &b, &c);
	
	int p1 = (a+b)%c;
	int p2 = ((a%c)+(b%c))%c;
	int p3 = (a*b)%c;
	int p4 = ((a%c)*(b%c))%c;

	printf("%d\n", p1);
	printf("%d\n", p2);
	printf("%d\n", p3);
	printf("%d\n", p4);
	
	return 0;
}
