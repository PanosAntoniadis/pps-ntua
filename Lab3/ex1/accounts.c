/**
 * A very simple parallel application
 * that handles an array of bank accounts.
 **/
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#include "../common/timer.h"
#include "../common/aff.h"

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
pthread_barrier_t start_barrier;
int time_to_leave;

/**
 * The accounts' array.
 **/
struct {
	unsigned int value;
} accounts[MAX_THREADS];

/**
 * The struct that is passed as an argument to each thread.
**/
typedef struct {
	int tid,
	    cpu;
	unsigned long long ops;

	/* Why do we use padding here? */
	char padding[64 - 2*sizeof(int) - sizeof(unsigned long long)];
} tdata_t;

void *thread_fn(void *targ);

int main()
{
	timer_tt *wall_timer;
	pthread_t threads[MAX_THREADS];
	tdata_t threads_data[MAX_THREADS];
	unsigned int nthreads = 0, *cpus;
	unsigned int i;

	//> Initializations.
	get_mtconf_options(&nthreads, &cpus);
	mt_conf_print(nthreads, cpus);
	if (pthread_barrier_init(&start_barrier, NULL, nthreads+1))
		print_error_and_exit("Failed to initialize start_barrier.\n");
	wall_timer = timer_init();

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

	//> Print results.
	double secs = timer_report_sec(wall_timer);
	double throughout = (double)total_ops / secs / 1000000.0;
	printf("Nthreads: %d  Runtime(sec): %d  Throughput(Mops/sec): %5.2lf\n",
	        nthreads, RUNTIME, throughout);

	return EXIT_SUCCESS;
}

/**
 * This is the function that is executed by each spawned thread.
 **/
void *thread_fn(void *targ)
{
	tdata_t *mydata = targ;
	int i;

	//> Pin thread to the specified cpu.
	setaffinity_oncpu(mydata->cpu);

	//> Wait until master gives the green light!
	pthread_barrier_wait(&start_barrier);

	while (!time_to_leave) {
		for (i=0; i < 1000; i++)
			accounts[mydata->tid].value++;
		mydata->ops += 1000;
	}

	return NULL;
}
