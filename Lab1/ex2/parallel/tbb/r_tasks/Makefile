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

OBJS = fwr_tasks.o

all : $(OBJS)
	$(CXX) $(LDFLAGS) $(OBJS) -o fwr_tasks -L$(LIBRARY_DIR) $(LIBS)


%.o : %.cpp
	$(CXX) $(CXXFLAGS) -c $<

clean :
	rm -f fwr_tasks $(OBJS)

