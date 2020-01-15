#include "lock.h"
#include "../common/alloc.h"
#include <pthread.h>

struct lock_struct {
	int* flag;
	int tail;
	int size;
};

__thread int mySlotIndex;

lock_t *lock_init(int nthreads)
{
	lock_t *lock;

	XMALLOC(lock, 1);
	/* other initializations here. */
	lock->size = nthreads;
	XMALLOC(lock->flag, nthreads);
	int i;
	for(i=1; i<nthreads; i++)
		lock->flag[i] = 0;
	lock->flag[0] = 1;
	lock->tail = 0;

	return lock;
}

void lock_free(lock_t *lock)
{
	XFREE(lock);
}

void lock_acquire(lock_t *lock)
{
	int slot = __sync_fetch_and_add(&(lock->tail), 1) % lock->size;
	mySlotIndex = slot;
	while (!lock->flag[slot]){
	}
}

void lock_release(lock_t *lock)
{
	int slot = mySlotIndex;
	lock->flag[slot] = 0;
	lock->flag[(slot+1)%lock->size] = 1;
}
