#define C 100
#define T 100000000

#define val 1.0
#define e 0.000001

double max ( double a, double b );
int converge ( double ** u_previous, double ** u_current, int X, int Y );
double ** allocate2d ( int dimX, int dimY );
void free2d( double ** array );
void init2d ( double ** array, int dimX, int dimY );
void zero2d ( double ** array, int dimX, int dimY );
void print2d ( double ** array, int dimX, int dimY );
void fprint2d ( char * s, double ** array, int dimX, int dimY );
