CC = gcc
CFLAGS = -Wall -Wextra -pthread -O0

## Remove some warnings.
CFLAGS += -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function

all: linked_list_nosync test_nosync linked_list_pthread test_pthread linked_list_tas test_tas linked_list_ttas test_ttas linked_list_array test_array linked_list_clh test_clh

## Additional source files
SRC_FILES = ../common/aff.c

linked_list_nosync: main.c nosync_lock.c $(SRC_FILES) 
	$(CC) $(CFLAGS) $^ -o $@

test_nosync: test.c nosync_lock.c $(SRC_FILES)
	$(CC) $(CFLAGS) $^ -o $@

linked_list_pthread: main.c pthread_lock.c $(SRC_FILES)
	$(CC) $(CFLAGS) $^ -o $@

test_pthread: test.c pthread_lock.c $(SRC_FILES)	
	$(CC) $(CFLAGS) $^ -o $@

linked_list_tas: main.c tas_lock.c $(SRC_FILES)
	$(CC) $(CFLAGS) $^ -o $@

test_tas: test.c tas_lock.c $(SRC_FILES)
	$(CC) $(CFLAGS) $^ -o $@

linked_list_ttas: main.c ttas_lock.c $(SRC_FILES)
	$(CC) $(CFLAGS) $^ -o $@

test_ttas: test.c ttas_lock.c $(SRC_FILES)
	$(CC) $(CFLAGS) $^ -o $@

linked_list_array: main.c array_lock.c $(SRC_FILES)
	$(CC) $(CFLAGS) $^ -o $@

test_array: test.c array_lock.c $(SRC_FILES)
	$(CC) $(CFLAGS) $^ -o $@

linked_list_clh: main.c clh_lock.c $(SRC_FILES)
	$(CC) $(CFLAGS) $^ -o $@

test_clh: test.c clh_lock.c $(SRC_FILES)
	$(CC) $(CFLAGS) $^ -o $@



clean:
	rm -f linked_list_nosync test_nosync linked_list_pthread test_pthread linked_list_tas test_tas linked_list_ttas test_ttas linked_list_array test_array linked_list_clh test_clh
