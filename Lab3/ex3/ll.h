#ifndef LL_H
#define LL_H

/**
 * Defines the linked list API.
 **/

typedef struct linked_list ll_t;

/**
 * Create a new linked list and free it.
 **/
ll_t *ll_new();
void ll_free(ll_t *);

/**
 * Search, insert and remove a key from the linked list.
 **/
int ll_contains(ll_t *ll, int key);
int ll_add(ll_t *ll, int key);
int ll_remove(ll_t *ll, int key);

/**
 * Print a linked list (only for debugging).
 **/
void ll_print(ll_t *ll);

#endif /* LL_H */
