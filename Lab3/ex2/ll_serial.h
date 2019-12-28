#ifndef LL_SERIAL_H
#define LL_SERIAL_H

#include <stdio.h>
#include <limits.h>

#include "../common/alloc.h"

typedef struct ll_node {
	int key;
	struct ll_node *next;
} ll_node_t;

typedef struct {
	ll_node_t *head;
} ll_t;

/**
 * Create a new linked list node.
 **/
static ll_node_t *ll_node_new(int key)
{
	ll_node_t *ret;

	XMALLOC(ret, 1);
	ret->key = key;
	ret->next = NULL;

	return ret;
}

/**
 * Free a linked list node.
 **/
static void ll_node_free(ll_node_t *ll_node)
{
	XFREE(ll_node);
}

/**
 * Create a new empty linked list.
 **/
static ll_t *ll_new()
{
	ll_t *ret;

	XMALLOC(ret, 1);
	ret->head = ll_node_new(-1);
	ret->head->next = ll_node_new(INT_MAX);
	ret->head->next->next = NULL;

	return ret;
}

/**
 * Free a linked list and all its contained nodes.
 **/
static void ll_free(ll_t *ll)
{
	ll_node_t *next, *curr = ll->head;
	while (curr) {
		next = curr->next;
		ll_node_free(curr);
		curr = next;
	}
	XFREE(ll);
}

/**
 * Search for a given key in a linked list.
 **/
static int ll_contains(ll_t *ll, int key)
{
	ll_node_t *curr = ll->head;
	int ret = 0;
	
	while (curr->key < key)
		curr = curr->next;

	ret = (key == curr->key);
	return ret;
}

/**
 * Insert a key in the linked list, if not already there.
 **/
static int ll_add(ll_t *ll, int key)
{
	int ret = 0;
	ll_node_t *curr, *next;
	ll_node_t *new_node;

	curr = ll->head;
	next = curr->next;

	while (next->key < key) {
		curr = next;
		next = curr->next;
	}

	if (key != next->key) {
		ret = 1;
		new_node = ll_node_new(key);
		new_node->next = next;
		curr->next = new_node;
	}

	return ret;
}

/**
 * Remove a key from a linked list.
 **/
static int ll_remove(ll_t *ll, int key)
{
	int ret = 0;
	ll_node_t *curr, *next;

	curr = ll->head;
	next = curr->next;

	while (next->key < key) {
		curr = next;
		next = curr->next;
	}

	if (key == next->key) {
		ret = 1;
		curr->next = next->next;
		ll_node_free(next);
	}

	return ret;
}

/**
 * Print a linked list.
 **/
static void ll_print(ll_t *ll)
{
	ll_node_t *curr = ll->head;
	printf("LIST [");
	while (curr) {
		if (curr->key == INT_MAX)
			printf(" -> MAX");
		else
			printf(" -> %d", curr->key);
		curr = curr->next;
	}
	printf(" ]\n");
}

#endif /* LL_SERIAL_H */
