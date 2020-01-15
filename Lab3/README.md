## Cache hierarchy and Scalability

Simple transaction system where scalability fails due to incorrect handling of cache hierarchy.

<p float="left">
  <img src="Lab3/ex1/plots/ex1_thoughput.png" width="420" />
  <img src="Lab3/ex1/plots/ex1_thoughput_opt.png" width="420" />
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
  <img src="Lab3/ex2/plots/ex2_thoughput_16_sync.png" width="280" />
  <img src="Lab3/ex2/plots/ex2_thoughput_1024_sync.png" width="280" />
  <img src="Lab3/ex2/plots/ex2_thoughput_8192_sync.png" width="280" />
</p>


## Synchronization techniques in Data Structures

### Types of synchronization
  - Fine-grain locking
  - Optimistic synchronization
  - Lazy synchronization


 ### Results
 
 - When searches > insertions-deletions
 
 
 <p float="left">
  <img src="Lab3/ex3/plots/ex3_thoughput_1024_1.png" width="420" />
  <img src="Lab3/ex3/plots/ex3_thoughput_8192_1.png" width="420" />
</p>



 - When searches < insertions-deletions
 
 <p float="left">
  <img src="Lab3/ex3/plots/ex3_thoughput_1024_2.png" width="420" />
  <img src="Lab3/ex3/plots/ex3_thoughput_8192_2.png" width="420" />
</p>



