#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#include "../common/aff.h"
#include "../common/timer.h"
#include "ll.h"

#define MAX_THREADS 64
#define RUNTIME 10

#define print_error_and_exit(format...) \
	do { \
		fprintf(stderr, format); \
		exit(EXIT_FAILURE); \
	} while (0)

/**
 * Global data.
**/
ll_t *ll;
unsigned int list_size;
pthread_barrier_t start_barrier;
int time_to_leave;
short contains_pct, add_pct, remove_pct;

/**
 * The struct that is passed as an argument to each thread.
**/
typedef struct {
	int tid,
	    cpu;
	unsigned long long ops;
	char padding[64 - 2*sizeof(int) - sizeof(unsigned long long)];
} tdata_t;

void *thread_fn(void *targ);

int main(int argc, char **argv)
{
	timer_tt *wall_timer;
	pthread_t threads[MAX_THREADS];
	tdata_t threads_data[MAX_THREADS];
	unsigned int nthreads = 0, *cpus;
	unsigned int i;

	//> Initializations.
	if (argc != 5)
		print_error_and_exit("usage: %s <list_size> <contains_pct> <add_pct> "
		                                            "<remove_pct>\n", argv[0]);
	list_size = atoi(argv[1]);
	contains_pct = atoi(argv[2]);
	add_pct = atoi(argv[3]);
	remove_pct = atoi(argv[4]);
	if (contains_pct + add_pct + remove_pct != 100)
		print_error_and_exit("The total percentage of operations is not 100%%!\n");

	get_mtconf_options(&nthreads, &cpus);
	mt_conf_print(nthreads, cpus);

	if (pthread_barrier_init(&start_barrier, NULL, nthreads+1))
		print_error_and_exit("Failed to initialize start_barrier.\n");
	wall_timer = timer_init();

	//> Initialize the linked list.
	ll = ll_new();
	for (i=list_size/2; i > 0; i--)
		ll_add(ll, i);

	//> Spawn threads.
	for (i=0; i < nthreads; i++) {
		threads_data[i].tid = i;
		threads_data[i].cpu = cpus[i];
		threads_data[i].ops = 0;
		if (pthread_create(&threads[i], NULL, thread_fn, &threads_data[i]))
			print_error_and_exit("Error creating thread %d.\n", i);
	}

	//> Signal threads to start computation.
	pthread_barrier_wait(&start_barrier);
	timer_start(wall_timer);

	sleep(RUNTIME);
	time_to_leave = 1;

	//> Wait for threads to complete their execution.
	for (i=0; i < nthreads; i++) {
		if (pthread_join(threads[i], NULL))
			print_error_and_exit("Failure on pthread_join for thread %d.\n", i);
	}

	timer_stop(wall_timer);

	//> How many operations have been performed by all threads?
	unsigned long long total_ops = 0;
	for (i=0; i < nthreads; i++)
		total_ops += threads_data[i].ops;

#ifndef PRINT_RESULTS
	//> Print statistics.
	double secs = timer_report_sec(wall_timer);
	double throughout = (double)total_ops / secs / 1000.0;
	printf("Nthreads: %d  Runtime(sec): %d  Workload: %d/%d/%d  Throughput(Kops/sec): %5.2lf\n",
	        nthreads, RUNTIME, contains_pct, add_pct, remove_pct, throughout);
#endif

#ifdef PRINT_RESULTS
	ll_print(ll);
#endif
	ll_free(ll);
	return EXIT_SUCCESS;
}

/**
 * This is the function that is executed by each spawned thread.
 **/
void *thread_fn(void *targ)
{
	tdata_t *mydata = targ;
	int i;
	struct drand48_data drand_buffer;
	long int drand_res;

	//> Initialize the thread-safe (and scalable) random number generator.
	srand48_r(rand() * mydata->tid, &drand_buffer);

	//> Pin thread to the specified cpu.
	setaffinity_oncpu(mydata->cpu);

	//> Wait until master gives the green light!
	pthread_barrier_wait(&start_barrier);

	while (!time_to_leave) {
		//> Get a random number.
		lrand48_r(&drand_buffer, &drand_res);
		int key = drand_res % (list_size + 1);

		//> Get a random operation.
		lrand48_r(&drand_buffer, &drand_res);
		int op = drand_res % 100;

		if (op < contains_pct)
			ll_contains(ll, key);
		else if (op < contains_pct + add_pct)
			ll_add(ll, key);
		else
			ll_remove(ll, key);

		mydata->ops++;
		for (i=0; i < 200; i++)
			/* do nothing */;
	}

	return NULL;
}
