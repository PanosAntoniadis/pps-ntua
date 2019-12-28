#include "../common/alloc.h"
#include "lock.h"

typedef enum {
	UNLOCKED = 0,
	LOCKED
} lock_state_t;

struct lock_struct {
	lock_state_t state;
};

lock_t *lock_init(int nthreads)
{
	lock_t *lock;

	XMALLOC(lock, 1);
	lock->state = UNLOCKED;
	return lock;
}

void lock_free(lock_t *lock)
{
	XFREE(lock);
}

void lock_acquire(lock_t *lock)
{
	lock_t *l = lock;

	while (__sync_lock_test_and_set(&l->state, LOCKED) == LOCKED)
		/* do nothing */ ;
}

void lock_release(lock_t *lock)
{
	lock_t *l = lock;

	/* Why not just 'l->state = UNLOCKED' here?? */
	__sync_lock_release(&l->state);
}
