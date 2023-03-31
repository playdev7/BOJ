#include <stdio.h>

int main() {
	long long a, b, result;
	
	scanf("%lld %lld", &a, &b);

	result = (a+b)*(a-b);

	printf("%lld", result);

	return 0;
}
