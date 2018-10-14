#include <stdio.h>

int* matrix(){
	int a[10];
	for(int i = 0;i <= 10;i++){
		a[i] = i;
	}

	return a;
}

int main(){
	
	int* b = matrix();


	return 0;
}

