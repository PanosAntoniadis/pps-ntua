.phony: all clean

all: fw fw_sr fw_tiled 

CC=gcc
CFLAGS= -Wall -O3 -Wno-unused-variable

HDEPS+=%.h

OBJS=util.o

fw: $(OBJS) fw.c 
	$(CC) $(OBJS) fw.c -o fw $(CFLAGS)
fw_sr: fw_sr.c 
	$(CC) $(OBJS) fw_sr.c -o fw_sr $(CFLAGS)
fw_tiled: fw_tiled.c 
	$(CC) $(OBJS) fw_tiled.c -o fw_tiled $(CFLAGS)

%.o: %.c $(HDEPS)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f *.o fw fw_sr fw_tiled 

