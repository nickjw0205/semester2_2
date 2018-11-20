#include <cstdlib>
#include <utility>
#include <time.h>
#include <ctime>
#include <stdio.h>
#include <iostream>
#include <queue>

using namespace std;

int cnt = 0;
int n = 5;
int W = 20;
float w[5];
float p[5];
int maxprofit1;
int numbest;
int bestset[5], include[5];

struct Breadth_node{
	int level;
	int profit;
	int weight;
};

struct Best_node{
	int level;
	int profit;
	int weight;
	float bound;
};

struct node_cmp{
    bool operator()(const Best_node& a, const Best_node& b) const{
        return a.bound < b.bound;
    }
};

bool DFS_promising(int i, int weight, int profit);
float Best_bound(Best_node u);
float Breadth_bound(Breadth_node u);

//knapsack function
int DFS_knapsack(int i, int profit, int weight){
	cnt++;
	if(weight <= W && profit > maxprofit1){
		maxprofit1 = profit;
		numbest = i;
		for(int j = 0; j < n;j++){
			bestset[j] = include[j];
		}
	}

	if(DFS_promising(i, weight, profit)){
		include[i+1] = 1; // 1 means "yes"
		DFS_knapsack(i + 1, profit + p[i+1], weight + w[i+1]);
		include[i+1] = 0; // 0 means "No"
		DFS_knapsack(i+1, profit, weight);
	}
	return maxprofit1;
}

bool DFS_promising(int i, int weight, int profit){
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
		return bound > maxprofit1;
	}
}


int Breadth_knapsack(int n, float p[], float w[], int W, int maxprofit){
	std::queue<Breadth_node> Q;
	Breadth_node u,v;
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
		if(Breadth_bound(u) > maxprofit){
			Q.push(u);
		}
		u.weight = v.weight;
		u.profit = v.profit;
		if(Breadth_bound(u) > maxprofit){
			Q.push(u);
		}
	}

	return maxprofit;
}

int Best_knapsack(int n, const float p[], const float w[], int W, int maxprofit){

	std::priority_queue<Best_node,std::vector<Best_node>,node_cmp> PQ;
	Best_node u,v;

	v.level = -1;
	v.profit = 0;
	v.weight = 0;
	maxprofit = 0;

	v.bound = Best_bound(v);
	PQ.push(v);

	while(!PQ.empty()){
		v = PQ.top();
		PQ.pop();
		cnt++;
		if(v.bound > maxprofit){
			u.level = v.level + 1;
			u.weight = v.weight + w[u.level];
			u.profit = v.profit + p[u.level];

			if(u.weight <= W && u.profit > maxprofit){
				maxprofit = u.profit;
			}
			u.bound = Best_bound(u);

			//left node
			if(u.bound > maxprofit){
				PQ.push(u);
			}
			u.weight = v.weight;
			u.profit = v.profit;
			u.bound = Best_bound(u);

			//right node
			if(u.bound > maxprofit){
				PQ.push(u);
			}
		}
	}
	return maxprofit;
}

float Best_bound(Best_node u){
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

float Breadth_bound(Breadth_node u){
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

bool desc(pair <float,float> a,pair <float,float> b){
	return a.first/a.second > b.first / b.second;
}

int main(){

	//for while-loop
	int z = 0;

	//result of nodes that each search function visits
	int cnt_result[3];

	//result of each search function 
	int Best_answer;
	int DFS_answer;
	int Breadth_answer;

	// maxprofit
	int maxprofit = 0;

	//for insert weight and profit
	float w1 = 0, p1 = 0;

	//for use random function
	srand((unsigned int)time(NULL) + rand());	

	//do 100000 cases
	int num = 0;
	int c = 0;
	printf("Best is slowest.\n");
	int count_depth = 0;
	int count_best_than_depth = 0;
	int count_breadth_than_depth = 0;
	while(z != 100000000 && num != 20){		
		vector<pair<float,float> > v;

		//choose weight and profit randomly until profit is bigger than weight.
		for(int i = 0; i < n; i++){
			if(i == 1){
				w1 = v[0].second;
				p1 = v[0].first;
			}
			else{
				w1= (float)(rand() % 10) + 1;
				p1 = (float)(rand() % 100) + 1;
				while(w1 >= p1){
					p1 = (float)(rand() % 100) + 1;
				}
			}
			v.push_back(pair<float,float>(p1,w1));
		}

		//sort the p/w array
		sort(v.begin(),v.end(),desc);	

		for(int i = 0; i < n; i++){
			p[i] = v[i].first;
			w[i] = v[i].second;
		}

		//do best-first-search, reset the number of nodes
		cnt = 0;
		Best_answer = Best_knapsack(n, p, w, W, maxprofit);
		cnt_result[0] = cnt;

		//reset the number of nodes, maxprofit, numbest
		cnt = 0;
		maxprofit1 = 0;
		numbest = 0;

		//do depth-first-search
		DFS_answer = DFS_knapsack(-1,0,0);
		cnt_result[1] = cnt;

		//the number of nodes, do breadth-first-search
		cnt = 0;
		Breadth_answer = Breadth_knapsack(n, p, w, W, maxprofit);
		cnt_result[2] = cnt;

		//for stop loop
		z++;

		// when depth is faster than best
		if(cnt_result[0] > cnt_result[1]){
			printf(" Depth = %.0d || Best = %.0d || Breath = %.0d\n", cnt_result[1], cnt_result[0], cnt_result[2]);
			printf(" Item = p[i]  w[i]  p[i]/w[i]\n");
			for(int i = 0; i < n; i++){
				printf("   I%2.0d =  %2.0f    %2.0f    %5.1f\n", i+1, p[i],w[i],p[i]/w[i]);
			}
			printf("\n");
			num++;
		}
	}
}
