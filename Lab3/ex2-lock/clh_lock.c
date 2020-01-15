#include "../common/alloc.h"
#include "lock.h"

#define FALSE 0
#define TRUE  1

#define FLAG_ENTRY_SIZE 1

typedef struct {
	char locked; /* FALSE or TRUE. */
	char padding[63];
} clh_node_t;

struct lock_struct {
	clh_node_t *tail;
};

/**
 * These are GCC's magic. Per thread variables.
 * They are initialized to 0 ( = NULL).
 **/
__thread clh_node_t *myNode;
__thread clh_node_t *myPred;

lock_t *lock_init(int nthreads)
{
	lock_t *lock;
	clh_node_t *tail;
	int i;

	XMALLOC(lock, 1);
	XMALLOC(tail, 1);

	lock->tail = tail;
	lock->tail->locked = FALSE;

	return lock;
}

void lock_free(lock_t *lock)
{
	lock_t *l = lock;
	XFREE(l);
}

void lock_acquire(lock_t *lock)
{
	lock_t *l = lock;

	if (!myNode)
		XMALLOC(myNode, 1);

	myNode->locked = TRUE;
	myPred = __sync_lock_test_and_set(&l->tail, myNode);

	while (myPred->locked == TRUE)
		/* do nothing */ ;
}

void lock_release(lock_t *lock)
{
	myNode->locked = FALSE;
	myNode = myPred;
}
