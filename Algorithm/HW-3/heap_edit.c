#include <stdio.h>
#include <stdlib.h>

typedef struct Heap{
	
	int heapsize;
	int S[9];

}heap;

void siftdown(heap * H, int i){
	int parent, largerchild;
	int siftkey;
	int spotfound;

	siftkey = H->S[i];
	parent = i;
	spotfound = 0;
    while(2 * parent <= H->heapsize && !spotfound){
        if((2 * parent  < H->heapsize) && (H->S[2*parent] < H->S[2*parent +1])){
            largerchild = 2 * parent + 1 ;
        }
        else{
            largerchild = 2 * parent ;
        }
        if(siftkey < H->S[largerchild]){
            H->S[parent] = H->S[largerchild];
            parent = largerchild;
        }
        else{
            spotfound = 1 ;
        }
    }
    H->S[parent] = siftkey;
    for(int j = 1 ; j <= H->heapsize ; j++){
            printf("%d ", H->S[j] );
    }
}

int root(heap *H){
    int keyout;

    keyout = H->S[1];
    H->S[1] = H->S[H->heapsize];
    H->heapsize = H->heapsize - 1;

    siftdown(H,1);
    return keyout;
}

void removekeys(int n, heap *H, int S[]){
    int i;
    for(i = n ; i > 0 ; i--){
        printf("----------------------\n");
        printf("i = %d\n", i);
        printf("s[i] = %d\n", S[i]);

        for(int j = 1 ; j <= n ; j++){
            printf("%d ", S[j] );
        }
        printf("\n");
        printf("\n");

        S[i] = root(H);
        printf("s[i] = %d\n", S[i]);

        for(int j = 1 ; j <= n ; j++){
            printf("%d ", S[j] );
        }
        printf("\n");
        printf("\n");
        printf("\n");
        printf("\n");

    }

}

void makeheap(int n, heap *H){
    int i;
    for(i = n/2 ; i > 0; i--){
        siftdown(H,i);
    }
}

void heapsort(int n, heap *H){
    makeheap(n,H);
    removekeys(n,H,H->S);
}

void printArray(int array[], int size){
    for(int i = 1 ; i <= size ; i++){
        printf("%d ",array[i]);
    }
    printf("\n");
}

int main(){

	int S[9] = {-1,10,3,2,6,5,8,7,9};
    heap *H = malloc(sizeof(heap));;
    H->heapsize = malloc(sizeof(int));
    H->S = malloc(sizeof(int) * 10);
	H->heapsize = 8;
	for(int i = 0; i <= H->heapsize; i++){
		H->S[i] = S[i];
	}

	heapsort(8, H);

	printf("최종\n");
	for(int i = 1; i <= H->heapsize; i++){
		printf("%d ", H->S[i]);
	}
	printf("\n");
	
}







