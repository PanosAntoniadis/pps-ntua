## Parallelization of the Heat Equation using MPI

### Algorithms
 - Jacobi
 - Gauss-Seidel SOR
 - Red-Black SOR

### Brief results

- Scalability test

 <p float="left">
  <img src="plots/speedup_2048.png" width="280" />
  <img src="plots/speedup_4096.png" width="280" /> 
  <img src="plots/speedup_6144.png" width="280" />
</p>

- Speed test

 <p float="left">
  <img src="plots/bar_conv_jac.png" width="280" />
  <img src="plots/bar_conv_gau.png" width="280" /> 
  <img src="plots/bar_rb_jac.png" width="280" />
</p>


### Project Structure

- Project description in Greek [here](pps-exercise2-2019-20.pdf).
- Serial implementations in [serial](serial).
- Parallel MPI implementations in [parallel](parallel).
- Final report in Greek in [report](report).
- Plots and scripts in [plots](plots).


