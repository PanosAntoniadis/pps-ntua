.phony: all clean

all: fwr_tasks fwt_tasks fws_parfor

CC=gcc
CFLAGS= -Wall -O3 -Wno-unused-variable -fopenmp

HDEPS+=%.h

OBJS=util.o

%.o: %.c $(HDEPS)
	$(CC) $(CFLAGS) -c $< -o $@

fwr_tasks: fwr_tasks.c 
	$(CC) $(OBJS) fwr_tasks.c -o fwr_tasks $(CFLAGS)

fwt_tasks: fwt_tasks.c
	$(CC) $(OBJS) fwt_tasks.c -o fwt_tasks $(CFLAGS)

fws_parfor: fws_parfor.c
	$(CC) $(OBJS) fws_parfor.c -o fws_parfor $(CFLAGS)

clean:
	rm -f *.o fwr_tasks fwt_tasks fws_parfor

