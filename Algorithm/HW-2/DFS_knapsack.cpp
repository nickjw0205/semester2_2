#include <stdio.h>
#include <iostream>
#include <queue>

//To count the number of nodes that we visit	
int cnt = 0;

//input size
int n = 4;

// //weight limit
int W = 16;

// //weight for items
int w[4] = {2,5,10,5};

// //profit for items
int p[4] = {40,30,50,10};

//maxprofit
int maxprofit = 0;

int numbest;

// int bestset[4], include[4];
//exercise 6.1
// int n = 5;
// int W = 13;
// int w[5] = {2,5,7,3,1};
// int p[5] = {20,30,35,12,3};
// int maxprofit = 0;
// int numbest;
int bestset[5], include[5];

//cnt = 5, maxprofit = 65

bool promising(int i, int weight, int profit);

//knapsack function
void knapsack(int i, int profit, int weight){
	cnt++;
	if(weight <= W && profit > maxprofit){
		maxprofit = profit;
		numbest = i;
		for(int j = 0; j < n;j++){
			bestset[j] = include[j];
		}
	}

	if(promising(i, weight, profit)){
		include[i+1] = 1; // 1 means "yes"
		knapsack(i + 1, profit + p[i+1], weight + w[i+1]);
		include[i+1] = 0; // 0 means "No"
		knapsack(i+1, profit, weight);
	}
}

//check that node is promising or not
bool promising(int i, int weight, int profit){
	int j, k;
	int totweight;
	float bound;

	if(weight >= W){
		return 0;
	}
	else{
		j = i+1;
		bound = profit;
		totweight = weight;
		while(j < n && (totweight + w[j] <= W)){
			totweight += w[j];
			bound += p[j];
			j++;
		}
		k = j;
		if(k < n){
			bound += ((W - totweight) * (p[k]/w[k]));
		}
		return bound > maxprofit;
	}
}

//main function
int main(){




	numbest = 0;
	maxprofit = 0;
	knapsack(-1,0,0);
	printf("cnt = %d\n", cnt);
	printf("maxprofit = %d\n", maxprofit);
	printf("\n");
}





