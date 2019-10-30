/**
 * @file
 * parallel_for simple demo program
 */

#include <cstdlib>
#include <iostream>

#include "tbb/blocked_range.h"
#include "tbb/parallel_for.h"
#include "tbb/parallel_invoke.h"
#include "tbb/task_scheduler_init.h"
#include "tbb/tick_count.h"

#ifdef DEBUG
#include <sys/syscall.h>
#endif

/**
 * Dummy work on a float
 *
 */
void Foo(float &x)
{
    x = x + 2.2;
    x = x / 3.3;
    x = x * 4.4;
    x = x / 5.5;
    x = x * 6.6;
    x = x / 7.7;
}

/**
 * Applies serially Foo on an float array
 * @param a float array
 * @param n size of array
 */  
void SerialApplyFoo(float *a, size_t n) 
{
    for ( size_t i = 0; i != n; i++ )
        Foo(a[i]);
}


/**
 * Class for function object that describes 
 * work to be performed on a blocked range 
 */ 
class ApplyFoo {
        float * const my_a;

    public:
        void operator()(const tbb::blocked_range<size_t>& r) const {
            float *a = my_a;

#ifdef DEBUG
            std::cerr << "Worker thread " << (pid_t)syscall(SYS_gettid)
                      << ": [" << r.begin() 
                      << "," << r.end() 
                      << ")" << std::endl; 
#endif

            for ( size_t i = r.begin(); i != r.end(); i++ ) 
                Foo(a[i]);
            
        }

        // constructor
        ApplyFoo(float *a) : my_a(a) {}
};

/**
 * Executes in parallel Foo on a float array. 
 * Uses functor inside parallel_for (the standard way)
 * @param a float array
 * @param n size of array
 */  
void ParallelApplyFooStandard(float *a, size_t n)
{
    tbb::parallel_for( tbb::blocked_range<size_t>(0,n), 
                        ApplyFoo(a),
                        tbb::auto_partitioner()
                    // or: tbb::simple_partitioner()
                    // or: tbb::affinity_partitioner()
                );
}

#ifdef USE_LAMBDAS

/**
 * Executes in parallel Foo on a float array.
 * Uses lambda expression (C++11 feature), compiles with gcc4.5 or newer.
 * @param a float array
 * @param n size of array
 */  
void ParallelApplyFooLambda(float *a, size_t n)
{
    tbb::parallel_for( 
            tbb::blocked_range<size_t>(0,n), 
            [=](const tbb::blocked_range<size_t>& r) {
                for ( size_t i = r.begin(); i != r.end(); ++i )
                    Foo(a[i]);
            } 
            );
}


/**
 * Executes in parallel Foo on a float array.
 * Uses nested parallelism, combining parallel_invoke and parallel_forlambda expression (C++11 feature), compiles with gcc4.5 or newer.
 * @param a float array
 * @param n size of array
 */  
void ParallelApplyFooNested(float *a, size_t n)
{
    tbb::parallel_invoke( 
            [=]() {
            tbb::parallel_for( 
                tbb::blocked_range<size_t>(0,n/2), 
                [=](const tbb::blocked_range<size_t>& r) {
                for ( size_t i = r.begin(); i != r.end(); ++i )
                Foo(a[i]);
                } 
                );
            }, 

            [=]() {
            tbb::parallel_for( 
                tbb::blocked_range<size_t>(n/2,n), 
                [=](const tbb::blocked_range<size_t>& r) {
                for ( size_t i = r.begin(); i != r.end(); ++i )
                Foo(a[i]);
                } 
                );
            } );
}


#if 0
/**
 * Executes in parallel Foo on a float array.
 * Uses lambda expression and "compact" form of parallel_for (i.e. operates
 * over a range of consequtive integers, does not need a blocked_range object)
 * @param a float array
 * @param n size of array
 */  
void ParallelApplyFooLambdaCompact(float *a, size_t n)
{
    tbb::parallel_for( size_t(0), n, 
            [=](size_t i) { 
            Foo(a[i]); 
         } ); 
}
#endif

#endif // !USE_LAMBDAS



/**
 * @param argv[1] number of threads
 * @param argv[2] size of array
 */  
int main(int argc, char **argv)
{
    const int nthreads = atoi(argv[1]);
    const int size = atoi(argv[2]);

    tbb::task_scheduler_init init(nthreads); 

    float *b = new float [size];
    
    for ( int i = 0; i < size; i++ ) b[i] = 0.0;

    tbb::tick_count tic,toc; 

    tic = tbb::tick_count::now();
    SerialApplyFoo(b, size);
    toc = tbb::tick_count::now();
    std::cout << "Serial : " << (toc-tic).seconds() 
              << " seconds" << std::endl;

    for ( int i = 0; i < size; i++ ) b[i] = 0.0;
    tic = tbb::tick_count::now();
    ParallelApplyFooStandard(b, size);
    toc = tbb::tick_count::now();
    std::cout << "Parallel standard : " << (toc-tic).seconds() 
              << " seconds" << std::endl;

#ifdef USE_LAMBDAS
    for ( int i = 0; i < size; i++ ) b[i] = 0.0;
    tic = tbb::tick_count::now();
    ParallelApplyFooLambda(b, size);
    toc = tbb::tick_count::now();
    std::cout << "Parallel lambda : " << (toc-tic).seconds() 
              << " seconds" << std::endl;

    for ( int i = 0; i < size; i++ ) b[i] = 0.0;
    tic = tbb::tick_count::now();
    ParallelApplyFooNested(b, size);
    toc = tbb::tick_count::now();
    std::cout << "Parallel nested : " << (toc-tic).seconds() 
              << " seconds" << std::endl;

#endif

    delete [] b;

    return 0;
}
