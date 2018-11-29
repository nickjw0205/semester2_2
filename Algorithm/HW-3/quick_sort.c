#include <stdio.h>

int partition(int S[], int low, int high, int pivotpoint){
    int i, j ;
    int pivotItem, temp ;

    pivotItem = S[low];
    j = low ;

    for(i = low + 1 ; i <= high ; i++){
        if(S[i] < pivotItem){
            j++;
            temp = S[i];
            S[i] = S[j];
            S[j] = temp ;
        }
    }

    pivotpoint = j ;
    temp = S[low];
    S[low] = S[pivotpoint];
    S[pivotpoint] = temp ;

    return pivotpoint ;
}

void quicksort(int S[], int low, int high){
	if(high > low){
		int pivotpoint = partition(S, low, high, 0);
		quicksort(S,low,pivotpoint-1);
		quicksort(S,pivotpoint+1,high);
	}
}

void printArray(int array[], int size){
    for(int i = 0 ; i < size ; i++){
        printf("%d ",array[i]);
    }
   	printf("\n");
}

int main(){
	
    int S[8] = {15,22,13,27,12,10,20,25};
    quicksort(S,0,7);

    printArray(S,8);
}