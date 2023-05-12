#include <stdio.h>

int main() {
	int n;
	
	scanf("%d", &n);

	for(int i=0; i<n; i++) {
		for(int m=0; m!=i; m++){
			printf("*");
		}
		printf("\n");
	}
	

	return 0;
}
