## Cache hierarchy and Scalability

Simple transaction system where scalability fails due to incorrect handling of cache hierarchy.

<p float="left">
  <img src="./ex1-cache/plots/ex1_thoughput.png" width="410" />
  <img src="./ex1-cache/plots/ex1_thoughput_opt.png" width="410" />
</p>


## Mutual Exclusion - Locks

### Type of locks
 - pthread_lock
 - tas_lock
 - ttas_lock
 - array_lock
 - clh_lock
 
 ### Results
 
 <p float="left">
  <img src="./ex2-lock/plots/ex2_thoughput_16_sync.png" width="270" />
  <img src="./ex2-lock/plots/ex2_thoughput_1024_sync.png" width="270" />
  <img src="./ex2-lock/plots/ex2_thoughput_8192_sync.png" width="270" />
</p>


## Synchronization techniques in Data Structures

### Types of synchronization
  - Fine-grain locking
  - Optimistic synchronization
  - Lazy synchronization


 ### Results
 
 - When searches > insertions-deletions
 
 
 <p float="left">
  <img src="./ex3-ds/plots/ex3_thoughput_1024_1.png" width="410" />
  <img src="./ex3-ds/plots/ex3_thoughput_8192_1.png" width="410" />
</p>



 - When searches < insertions-deletions
 
 <p float="left">
  <img src="./ex3-ds/plots/ex3_thoughput_1024_2.png" width="410" />
  <img src="./ex3-ds/plots/ex3_thoughput_8192_2.png" width="410" />
</p>

## Project Structure
- Project description in Greek [here](pps-exercise3-2019-20.pdf).
- Cache hierarchy and Scalability in [ex1-cache](ex1-cache).
- Mutual Exclusion - Locks in [ex2-lock](ex2-lock).
- Synchronization techniques in Data Structures in [ex3-ds](ex3-ds).
- Final report in Greek in [report](report).


