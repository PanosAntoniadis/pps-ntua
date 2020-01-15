CC = gcc
CFLAGS = -Wall -Wextra -pthread -O0

all: accounts accounts_opt

SRC_FILES= ../common/aff.c

accounts: accounts.c $(SRC_FILES) 
	$(CC) $(CFLAGS) $^ -o $@

accounts_opt: accounts_opt.c $(SRC_FILES)
	$(CC) $(CFLAGS) $^ -o $@

clean:
	rm -f accounts accounts_opt
