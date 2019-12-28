#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#include "lock.h"

#define MAX_THREADS 64

#define print_error_and_exit(format...) \
	do { \
		fprintf(stderr, format); \
		exit(EXIT_FAILURE); \
	} while (0)

/**
 * Global data.
 **/
lock_t *lock;
pthread_barrier_t start_barrier;

#define INCS_PER_THREAD 10000

void *thread_fn(void *targ);

int main(int argc, char **argv)
{
	pthread_t threads[MAX_THREADS];
	unsigned int nthreads = 0;
	unsigned int i;
	unsigned long long counter = 0;

	//> Initializations.
	if (argc != 2)
		print_error_and_exit("usage: %s <nthreads>\n", argv[0]);
	nthreads = atoi(argv[1]);

	if (pthread_barrier_init(&start_barrier, NULL, nthreads+1))
		print_error_and_exit("Failed to initialize start_barrier.\n");
	lock = lock_init(nthreads);

	//> Spawn threads.
	for (i=0; i < nthreads; i++) {
		if (pthread_create(&threads[i], NULL, thread_fn, &counter))
			print_error_and_exit("Error creating thread %d.\n", i);
	}

	//> Signal threads to start computation.
	pthread_barrier_wait(&start_barrier);

	//> Wait for threads to complete their execution.
	for (i=0; i < nthreads; i++) {
		if (pthread_join(threads[i], NULL))
			print_error_and_exit("Failure on pthread_join for thread %d.\n", i);
	}

	//> Print results.
	unsigned long long expected = nthreads * INCS_PER_THREAD;
	unsigned long long result = counter;
	int correct = (result == expected);
	if (result == expected)
		printf("%d threads: CORRECT\n", nthreads);
	else
		printf("%d threads: ERROR (expected = %llu, result = %llu)\n",
		       nthreads, expected, result);

	lock_free(lock);
	return EXIT_SUCCESS;
}

/**
 * This is the function that is executed by each spawned thread.
 **/
void *thread_fn(void *targ)
{
	unsigned long long *counter = targ;
	int i;

	//> Wait until master gives the green light!
	pthread_barrier_wait(&start_barrier);

	for (i=0; i < INCS_PER_THREAD; i++) {
		lock_acquire(lock);
		(*counter)++;
		lock_release(lock);
	}

	return NULL;
}
