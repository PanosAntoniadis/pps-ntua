#include "../common/alloc.h"
#include "lock.h"

struct lock_struct {
	/* Nothing useful here, just a placeholder. */
	int dummy;
};

lock_t *lock_init(int nthreads)
{
	/* do nothing */
	return NULL;
}

void lock_free(lock_t *lock)
{
	/* do nothing */
}

void lock_acquire(lock_t *lock)
{
	/* do nothing */
}

void lock_release(lock_t *lock)
{
	/* do nothing */
}
