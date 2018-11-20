#include <stdio.h>
#include <iostream>
#include <queue>

//count
int cnt = 0;

//example 6.1
int n = 4;
int W = 16;
int w[4] = {2,5,10,5};
int p[4] = {40,30,50,10};
int maxprofit = 0;

//exercise 6.1
// int n = 5;
// int W = 13;
// int w[5] = {2,5,7,3,1};
// int p[5] = {20,30,35,12,3};
// int maxprofit = 0;

struct node{
	int level;
	int profit;
	int weight;
};

float bound(node u);
	
int knapsack(int n, int p[], int w[], int W, int maxprofit){
	std::queue<node> Q;
	node u,v;
	v.level = -1;
	v.profit = 0;
	v.weight = 0;

	maxprofit = 0;
	Q.push(v);
	
	while(!Q.empty()){

		v = Q.front();
		Q.pop();
		cnt++;
		u.level = v.level + 1;
		u.weight = v.weight + w[u.level];
		u.profit = v.profit + p[u.level];

		if(u.weight <= W && u.profit > maxprofit){
			maxprofit = u.profit;
		}
		if(bound(u) > maxprofit){
			Q.push(u);
		}
		u.weight = v.weight;
		u.profit = v.profit;
		if(bound(u) > maxprofit){
			Q.push(u);
		}
	}

	return maxprofit;
}

float bound(node u){
	int j,k;
	int totweight;
	float result;

	if(u.weight >= W){
		return 0;
	}	
	else{
		result = u.profit;
		j = u.level+1;
		totweight = u.weight;
		while(j < n && ((totweight + w[j]) <= W)){
			totweight += w[j];
			result += p[j];
			j++;
		}
		k = j;
		if(k < n){
			result += ((W - totweight) * p[k]/w[k]);
		}
		return result;
	}
}


int main(){

	int answer = knapsack(n, p, w, W, maxprofit);
	printf("cnt = %d\n", cnt);
	printf("maxprofit = %d\n", answer);
}








