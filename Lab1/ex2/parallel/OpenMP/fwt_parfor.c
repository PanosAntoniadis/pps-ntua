/*
   Tiled version of the Floyd-Warshall algorithm using
	 OpenMP parallel for.
   command-line arguments: N, B
   N = size of graph
   B = size of tile
   works only when N is a multiple of B
 */
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <omp.h>
#include "util.h"

#include <stdlib.h>
#include <stdio.h>

void write_arr_to_file(char *name, int **A, int N);
int** read_arr_from_file(int **A ,char *s , int N);

inline int min(int a, int b);
inline void FW(int **A, int K, int I, int J, int N);
void graph_init_random(int **adjm, int seed, int n,  int m);

int main(int argc, char **argv)
{
	int **A;
	int i,j,k;
	struct timeval t1, t2;
	double time;
	int B=64;
	int N=1024;

	if (argc != 3){
		fprintf(stdout, "Usage %s N B\n", argv[0]);
		exit(0);
	}

	N=atoi(argv[1]);
	B=atoi(argv[2]);

	A=(int **)malloc(N*sizeof(int *));
	for(i=0; i<N; i++)A[i]=(int *)malloc(N*sizeof(int));
  graph_init_random_par(A,-1,N,128*N);
	//A=read_arr_from_file(A, "./cor_input",N);

	gettimeofday(&t1,0);

	for(k=0;k<N;k+=B){
		FW(A,k,k,k,B);
		#pragma omp parallel shared(A, B, k)
		{
			#pragma omp for nowait
			for(i=0; i<k; i+=B)
				FW(A,k,i,k,B);

			#pragma omp for nowait
			for(i=k+B; i<N; i+=B)
				FW(A,k,i,k,B);

			#pragma omp for nowait
			for(j=0; j<k; j+=B)
				FW(A,k,k,j,B);

			#pragma omp for nowait
			for(j=k+B; j<N; j+=B)
				FW(A,k,k,j,B);
		}
		#pragma omp parallel shared(A, B, k)
		{
			#pragma omp for collapse(2) nowait
			for(i=0; i<k; i+=B)
				for(j=0; j<k; j+=B)
					FW(A,k,i,j,B);

			#pragma omp for collapse(2) nowait
			for(i=0; i<k; i+=B)
				for(j=k+B; j<N; j+=B)
					FW(A,k,i,j,B);

			#pragma omp for collapse(2) nowait
			for(i=k+B; i<N; i+=B)
				for(j=0; j<k; j+=B)
					FW(A,k,i,j,B);

			#pragma omp for collapse(2) nowait
			for(i=k+B; i<N; i+=B)
				for(j=k+B; j<N; j+=B)
					FW(A,k,i,j,B);
		}
	}
	gettimeofday(&t2,0);

	time=(double)((t2.tv_sec-t1.tv_sec)*1000000+t2.tv_usec-t1.tv_usec)/1000000;
	printf("FW_TILED,%d,%d,%.4f\n", N,B,time);
	write_arr_to_file("out_t_tasks", A, N);
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

inline void FW(int **A, int K, int I, int J, int N)
{
	int i,j,k;
	for(k=K; k<K+N; k++)
		for(i=I; i<I+N; i++)
			for(j=J; j<J+N; j++)
				A[i][j]=min(A[i][j], A[i][k]+A[k][j]);

}

void write_arr_to_file(char *name, int **A, int N)
{
	FILE *f;

	f = fopen(name, "w");
	int i,j;
	for(i=0; i<N; i++){
		for(j=0; j<N; j++){
			fprintf(f, "%d ", A[i][j]);
		}
		fprintf(f ,"\n");
	}
}

int** read_arr_from_file(int **A ,char *s , int N){

	FILE *myFile;
	myFile = fopen(s, "r");
	A = (int **)malloc(N * sizeof(int *));
	int i,j;
	for(i=0; i<N; i++){
		A[i] = (int *)malloc(N * sizeof(int));
	}
	for( i=0 ;i<N;i++){
		for (j=0 ;j<N;j++){
			fscanf(myFile, "%d", &A[i][j]);
		}
	}
	return A;
}

void graph_init_random(int **adjm, int seed, int n,  int m)
{
     unsigned  int i, j;
		 
     srand48(seed);
     #pragma omp parallel for collapse(2)
     for(i=0; i<n; i++)
        for(j=0; j<n; j++)
           adjm[i][j] = abs((( int)lrand48()) % 1048576);

     for(i=0; i<n; i++)adjm[i][i]=0;
}
