#include "lock.h"
#include "../common/alloc.h"
#include <pthread.h>

struct lock_struct {
	pthread_spinlock_t pthread_lock;
};

lock_t *lock_init(int nthreads)
{
	lock_t *lock;

	XMALLOC(lock, 1);
	/* other initializations here. */

	/* initialize the pthread spin lock */
	pthread_spin_init(&(lock->pthread_lock), PTHREAD_PROCESS_SHARED); 

	return lock;
}

void lock_free(lock_t *lock)
{
	pthread_spin_destroy(&(lock->pthread_lock));
	XFREE(lock);
}

void lock_acquire(lock_t *lock)
{
	pthread_spin_lock(&(lock->pthread_lock));
}

void lock_release(lock_t *lock)
{
	pthread_spin_unlock(&(lock->pthread_lock));
}
