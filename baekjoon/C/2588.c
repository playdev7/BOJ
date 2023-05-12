#include <stdio.h>

int main() {
	int a, b;
	scanf("%d %d", &a, &b);	

	int three = a*(b%10);
	int four = a*((b%100-b%10)/10);
	int five = a*(b/100);
	int total = a*b;
	
	printf("%d\n", three);
    	printf("%d\n", four);
	printf("%d\n", five);
	printf("%d\n", total);
	
	return 0;
}
