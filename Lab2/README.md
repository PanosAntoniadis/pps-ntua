## Parallelization of the Heat Equation using MPI

### Algorithms
 - Jacobi
 - Gauss-Seidel SOR
 - Red-Black SOR

### Brief results

- Scalability test

 <p float="left">
  <img src="Lab2/plots/speedup_2048.png" width="280" />
  <img src="Lab2/plots/speedup_4096.png" width="280" /> 
  <img src="Lab2/plots/speedup_6144.png" width="280" />
</p>

- Speed test

 <p float="left">
  <img src="Lab2/plots/bar_conv_jac.png" width="280" />
  <img src="Lab2/plots/bar_conv_gau.png" width="280" /> 
  <img src="Lab2/plots/bar_rb_jac.png" width="280" />
</p>


### Project Structure

- Project description in Greek [here](Lab2/pps-exercise2-2019-20.pdf).
- Serial implementations in [serial](Lab2/serial).
- Parallel MPI implementations in [parallel](Lab2/parallel).
- Final report in Greek in [report](Lab2/report).
- Plots and scripts in [plots](Lab2/plots).


