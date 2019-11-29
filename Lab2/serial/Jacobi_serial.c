#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sys/time.h>
#include "utils.h"


void Jacobi(double ** u_previous, double ** u_current, int X_min, int X_max, int Y_min, int Y_max) {
	int i,j;
	for (i=X_min;i<X_max;i++)
		for (j=Y_min;j<Y_max;j++)
			u_current[i][j]=(u_previous[i-1][j]+u_previous[i+1][j]+u_previous[i][j-1]+u_previous[i][j+1])/4.0;
}

int main ( int argc, char ** argv ) {

	int X, Y;                           //2D-domain dimensions
	double ** u_current, ** u_previous;   //2D-domain
	double ** swap;
	struct timeval tts,ttf;
	double time=0;
	int t,converged=0;

	//read 2D-domain dimensions
	if (argc<2) {
		fprintf(stderr,"Usage: ./exec X (Y-optional)");
		exit(-1);
	}
	else if (argc==2) {
		X=atoi(argv[1]);
		Y=X;
	}
	else {
		X=atoi(argv[1]);
		Y=atoi(argv[2]);
	}

	//allocate domain and initialize boundary

	u_current=allocate2d(X,Y);
	u_previous=allocate2d(X,Y);
	init2d(u_current,X,Y);
	init2d(u_previous,X,Y);

	//computational core
	#ifdef TEST_CONV
	for (t=0;t<T && !converged;t++) {
	#endif
	#ifndef TEST_CONV
	#undef T
	#define T 256
	for (t=0;t<T;t++) {
	#endif
		swap=u_previous;
		u_previous=u_current;
		u_current=swap;

		gettimeofday(&tts,NULL);

		Jacobi(u_previous,u_current,1,X-1,1,Y-1);

		gettimeofday(&ttf,NULL);
		time+=(ttf.tv_sec-tts.tv_sec)+(ttf.tv_usec-tts.tv_usec)*0.000001;

		#ifdef TEST_CONV
		if (t%C==0)
			converged=converge(u_previous,u_current,X,Y);
		#endif
	}
	printf("Jacobi X %d Y %d Iter %d Time %lf midpoint %lf\n",X,Y,t-1,time, u_current[X/2][Y/2]);

	#ifdef PRINT_RESULTS
	char * s=malloc(30*sizeof(char));
	sprintf(s,"resJacobiNaive_%dx%d",X,Y);
	fprint2d(s,u_current,X,Y);
	free(s);
	#endif

	return 0;
}
