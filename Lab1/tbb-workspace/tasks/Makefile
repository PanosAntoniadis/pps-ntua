include ../Makefile.include

INCLUDE_DIR = $(TBB_DIR)/include/
LIBRARY_DIR = $(TBB_DIR)/build/$(LIBRARY_VER)

# CXX = g++
# To compile in clones:
CXX = g++
CXXFLAGS = -O3 -Wall -std=c++11 -DUSE_LAMBDAS 
LDFLAGS =
LIBS = -ltbb -lrt

CXXFLAGS += -I$(INCLUDE_DIR)
 
OBJS = fib.o

all : $(OBJS)
	$(CXX) $(LDFLAGS) $(OBJS) -o fib -L$(LIBRARY_DIR) $(LIBS)


%.o : %.cpp
	$(CXX) $(CXXFLAGS) -c $<

clean :
	rm -f fib $(OBJS)
