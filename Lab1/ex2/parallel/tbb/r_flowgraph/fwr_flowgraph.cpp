/*
   Recursive implementation of the Floyd-Warshall algorithm using
	 TBB flow graph.
   command line arguments: N, B
   N = size of graph
   B = size of submatrix when recursion stops
   works only for N, B = 2^k
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <math.h>

#include "tbb/task.h"
#include "tbb/flow_graph.h"
#include "tbb/task_scheduler_init.h"
#include "tbb/tick_count.h"
#include <tbb/task_scheduler_init.h>
#include <iostream>
#include <fstream>

using namespace std;
using namespace tbb::flow;

void print_arr_to_file(string name,int **arr,int N);
int** read_arr_from_file(string name, int N);

inline int min(int a, int b);
void FW_SR (int **A, int arow, int acol,
		int **B, int brow, int bcol,
		int **C, int crow, int ccol,
		int myN, int bsize);


void graph_init_random(int **adjm, int seed, int n,  int m);


int main(int argc, char **argv)
{
	int **A;
	int i;
	struct timeval t1, t2;
	double time;
	int B=16;
	int N=1024;

	if (argc !=4){
		fprintf(stdout, "Usage %s N B threads\n", argv[0]);
		exit(0);
	}

	N=atoi(argv[1]);
	B=atoi(argv[2]);
	const int nthreads = atoi(argv[3]);

	A = (int **) malloc(N*sizeof(int *));
	for(i=0; i<N; i++) A[i] = (int *) malloc(N*sizeof(int));

	graph_init_random(A,-1,N,128*N);
	//A = read_arr_from_file("../cor_input", N);

	tbb::task_scheduler_init init(nthreads);

	gettimeofday(&t1,0);
	FW_SR(A,0,0, A,0,0,A,0,0,N,B);
	gettimeofday(&t2,0);

	time=(double)((t2.tv_sec-t1.tv_sec)*1000000+t2.tv_usec-t1.tv_usec)/1000000;
	printf("FW_SR,%d,%d,%.4f\n", N, B, time);
	//print_arr_to_file("out_r_flowgraph", A, N);
	/*
	   for(i=0; i<N; i++)
	   for(j=0; j<N; j++) fprintf(stdout,"%d\n", A[i][j]);
	 */


	return 0;
}

inline int min(int a, int b)
{
	if(a<=b)return a;
	else return b;
}

void FW_SR (int **A, int arow, int acol,
		int **B, int brow, int bcol,
		int **C, int crow, int ccol,
		int myN, int bsize)
{
	int k,i,j;

	if(myN<=bsize)
		for(k=0; k<myN; k++)
			for(i=0; i<myN; i++)
				for(j=0; j<myN; j++)
					A[arow+i][acol+j]=min(A[arow+i][acol+j], B[brow+i][bcol+k]+C[crow+k][ccol+j]);
	else {
		graph g;
		continue_node <continue_msg> A11(g, [=] (const continue_msg &) {FW_SR(A,arow, acol,B,brow, bcol,C,crow, ccol, myN/2, bsize); });
		continue_node <continue_msg> A12(g, [=] (const continue_msg &) {FW_SR(A,arow, acol+myN/2,B,brow, bcol,C,crow, ccol+myN/2, myN/2, bsize); });
		continue_node <continue_msg> A21(g, [=] (const continue_msg &) {FW_SR(A,arow+myN/2, acol,B,brow+myN/2, bcol,C,crow, ccol, myN/2, bsize); });
		continue_node <continue_msg> A22(g, [=] (const continue_msg &) {FW_SR(A,arow+myN/2, acol+myN/2,B,brow+myN/2, bcol,C,crow, ccol+myN/2, myN/2, bsize); });
		continue_node <continue_msg> A22_(g, [=] (const continue_msg &) {FW_SR(A,arow+myN/2, acol+myN/2,B,brow+myN/2, bcol+myN/2,C,crow+myN/2, ccol+myN/2, myN/2, bsize); });
		continue_node <continue_msg> A21_(g, [=] (const continue_msg &) {FW_SR(A,arow+myN/2, acol,B,brow+myN/2, bcol+myN/2,C,crow+myN/2, ccol, myN/2, bsize); });
		continue_node <continue_msg> A12_(g, [=] (const continue_msg &) {FW_SR(A,arow, acol+myN/2,B,brow, bcol+myN/2,C,crow+myN/2, ccol+myN/2, myN/2, bsize); });
		continue_node <continue_msg> A11_(g, [=] (const continue_msg &) {FW_SR(A,arow, acol,B,brow, bcol+myN/2,C,crow+myN/2, ccol, myN/2, bsize); });

		make_edge(A11,A12);
		make_edge(A11,A21);
		make_edge(A12,A22);
		make_edge(A21,A22);
		make_edge(A22,A22_);
		make_edge(A22_,A12_);
		make_edge(A22_,A21_);
		make_edge(A12_,A11_);
		make_edge(A21_, A11_);

		A11.try_put(continue_msg());
		g.wait_for_all();

	}
}

void graph_init_random(int **adjm, int seed, int n,  int m)
{
     unsigned  int i, j;

     srand48(seed);
     for(i=0; i<n; i++)
        for(j=0; j<n; j++)
           adjm[i][j] = abs((( int)lrand48()) % 1048576);

     for(i=0; i<n; i++)adjm[i][i]=0;
}

void print_arr_to_file(string name,int **arr,int N){
        ofstream myfile (name);
        if (myfile.is_open())
        {
            for(int i = 0; i < N; i++){

                if(i!=0){myfile << "\n";}
                for(int j = 0; j < N; j++){

                   myfile << arr[i][j] << " " ;
                }
            }
            myfile.close();
        }
}

int** read_arr_from_file(string name, int N){
        ifstream myfile(name);
        int **arr;
        arr = (int **) malloc(N*sizeof(int *));
        for(int i=0; i<N; i++) arr[i] = (int *) malloc(N*sizeof(int));

        if (myfile.is_open())
        {
            for (int i=0 ;i<N;i++)
                for (int j=0 ;j<N ; j++)
                        myfile >> arr[i][j];
        }

        myfile.close();
        return arr;
}
