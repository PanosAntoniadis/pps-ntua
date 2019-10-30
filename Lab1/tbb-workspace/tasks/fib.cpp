/**
 * @file
 * Task execution demo program
 */ 
#include <cstdlib>
#include <iostream>

#include "tbb/task.h"
#include "tbb/task_group.h"
#include "tbb/task_scheduler_init.h"
#include "tbb/tick_count.h"

long SerialFib(long n)
{
    if ( n < 2 )
        return n;
    else
        return SerialFib(n-1) + SerialFib (n-2);
}

/**
 * Fibonacci task class
 */ 
class FibTask: public tbb::task {
    public:
        const long n;
        long * const sum;

        // constructor
        FibTask(long n_, long *sum_): n(n_), sum(sum_) {}

        // every task subclass must define the execute function
        task* execute() {

            if ( n < 16 ) {
                *sum = SerialFib(n);
            } else {
                long x,y;

                // allocate children tasks, a and b
                FibTask& a = *new(allocate_child() ) FibTask(n-1,&x);
                FibTask& b = *new(allocate_child() ) FibTask(n-2,&y);
                set_ref_count(3); // set ref_count to #children + 1

                // Spawn b
                tbb::task::spawn(b);

                // Spawn a and wait for all children (a and b)
                tbb::task::spawn_and_wait_for_all(a);

                *sum = x+y;
            }
            return NULL;
        }
};

/**
 * Driver function for task-based parallel implementation 
 * @param n Fibonacci number to compute
 * @return Fibonacci result
 */ 
long ParallelFibTask(long n)
{
    long sum;

    // create and spawn root task
    FibTask& a = *new(tbb::task::allocate_root()) FibTask(n,&sum);
    tbb::task::spawn_root_and_wait(a);

    return sum;
}
 
#ifdef USE_LAMBDAS

/**
 * Parallel Fibonacci implementation based on task groups
 * and Lambda expressions.
 * @param n Fibonacci number to compute
 * @return Fibonacci result
 */ 
long ParallelFibTG(long n) 
{
    if ( n < 16 )
        return SerialFib(n);
    else {
        int x, y;
        tbb::task_group g;
        g.run( [&]{ x = ParallelFibTG(n-1);} );
        g.run( [&]{ y = ParallelFibTG(n-2);} );
        g.wait();
        return x+y;
    }
}

#endif


/**
 * @param argv[1] Fibonacci number to compute
 * @param argv[2] number of threads
 */ 
int main(int argc, char *argv[]) 
{
    long serial_result, parallel_result;
    const int input = atoi(argv[1]);
    const int nthreads = atoi(argv[2]);

    tbb::tick_count tic, toc; 
    tic = tbb::tick_count::now ();
    serial_result = SerialFib(input);
    toc = tbb::tick_count::now ();
    std::cerr << "Serial : " <<  (toc-tic).seconds () 
              << " seconds" << std::endl;
    std::cerr << "result: " << serial_result << std::endl;
  
    tbb::task_scheduler_init init(nthreads);

    tic = tbb::tick_count::now ();
    parallel_result = ParallelFibTask(input);
    toc = tbb::tick_count::now ();
    std::cerr << "Parallel task : " <<  (toc-tic).seconds () 
              << " seconds" << std::endl;
    std::cerr << "result: " << parallel_result << std::endl;

#ifdef USE_LAMBDAS 
    tic = tbb::tick_count::now ();
    parallel_result = ParallelFibTG(input);
    toc = tbb::tick_count::now ();
    std::cerr << "Parallel task group : " <<  (toc-tic).seconds () 
              << " seconds" << std::endl;
    std::cerr << "result: " << parallel_result << std::endl;
#endif

   


    return 0;
}
