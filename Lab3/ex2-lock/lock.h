#ifndef LOCK_H
#define LOCK_H

/**
 * Defines the lock API.
 **/

typedef struct lock_struct lock_t;

lock_t *lock_init(int nthreads);
void lock_free(lock_t *lock);

void lock_acquire(lock_t *lock);
void lock_release(lock_t *lock);

#endif /* LOCK_H */
