#include <stdio.h>
#include <iostream>
#include <queue>

int cnt = 0;

//example6.1
int n = 4;
int W = 16;
int w[4] = {2,5,10,5};
int p[4] = {40,30,50,10};
int maxprofit = 0;

//exercise6.1
// int n = 5;
// int W = 13;
// int w[5] = {2,5,7,3,1};
// int p[5] = {20,30,35,12,3};
// int maxprofit = 0;

//result => profit: 71, cnt = 6


struct node{
	int level;
	int profit;
	int weight;
	float bound;
};


struct node_cmp{
    bool operator()(const node& a, const node& b) const{
        return a.bound < b.bound;
    }
};

float bound(node u);

int knapsack(int n, const int p[], const int w[], int W, int maxprofit){

	std::priority_queue<node,std::vector<node>,node_cmp> PQ;
	node u,v;

	v.level = -1;
	v.profit = 0;
	v.weight = 0;
	maxprofit = 0;

	v.bound = bound(v);
	PQ.push(v);

	while(!PQ.empty()){
		v = PQ.top();
		printf("\n");
		printf("-------------------------\n");
		printf("node v의 level은 %d입니다.\n", v.level+1);
		printf("node v의 profit은 %d입니다.\n", v.profit);
		printf("node v의 weight은 %d입니다.\n", v.weight);
		printf("node v의 bound은 %2.0f입니다.\n", v.bound);
		printf("maxprofit = %d\n", maxprofit);
		printf("-------------------------\n");
		printf("\n");
		PQ.pop();
		cnt++;
		if(v.bound > maxprofit){
			u.level = v.level + 1;
			u.weight = v.weight + w[u.level];
			u.profit = v.profit + p[u.level];

			if(u.weight <= W && u.profit > maxprofit){
				maxprofit = u.profit;
			}
			u.bound = bound(u);

			//left node
			if(u.bound > maxprofit){
				PQ.push(u);
			}
			u.weight = v.weight;
			u.profit = v.profit;
			u.bound = bound(u);

			//right node
			if(u.bound > maxprofit){
				PQ.push(u);
			}
		}
	}
	return maxprofit;
}

float bound(node u){
	int j,k;
	int totweight;
	float bound;

	if(u.weight >= W){
		return 0;
	}	
	else{
		bound = u.profit;
		j = u.level+1;
		totweight = u.weight;
		while(j < n && ((totweight + w[j]) <= W)){
			totweight += w[j];
			bound += p[j];
			j++;
		}
		k = j;
		if(k < n){
			bound += ((W - totweight) * p[k]/w[k]);
		}
		return bound;
	}
}

int main(){
	

	int answer = knapsack(n, p, w, W, maxprofit);
	printf("cnt = %d\n", cnt);
	printf("maxprofit = %d\n", answer);
}







