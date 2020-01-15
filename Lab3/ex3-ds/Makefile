CC = gcc
CFLAGS = -Wall -Wextra -pthread

## Remove some warnings.
CFLAGS += -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function

## For testing
RES=-DPRINT_RESULTS

all: linked_list_serial linked_list_fgl linked_list_opt linked_list_lazy

## Additional source files
SRC_FILES = ../common/aff.c

linked_list_serial: main.c ll_serial.c ${SRC_FILES}
	$(CC) $(CFLAGS)  $^ -o $@

linked_list_fgl: main.c ll_fgl.c ${SRC_FILES}
	$(CC) $(CFLAGS) $(RES) $^ -o $@

linked_list_opt: main.c ll_opt.c ${SRC_FILES}
	$(CC) $(CFLAGS) $(RES) $^ -o $@

linked_list_lazy: main.c ll_lazy.c ${SRC_FILES}
	$(CC) $(CFLAGS) $(RES) $^ -o $@

clean:
	rm -f linked_list_serial linked_list_fgl linked_list_opt linked_list_lazy
