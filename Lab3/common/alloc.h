#ifndef ALLOC_H
#define ALLOC_H

#include <stdio.h>
#include <stdlib.h>

/**
 * A pretty malloc() wrapper with error handling.
 **/
#define XMALLOC(var,N) \
	do { \
		(var) = malloc((N) * sizeof(*(var))); \
		if (!(var)) { \
			fprintf(stderr, "Out of memory: %s:%d\n", __FILE__, __LINE__); \
			exit(1); \
		} \
	} while(0)

#define XFREE(var) free(var)

#endif /* ALLOC_H */
