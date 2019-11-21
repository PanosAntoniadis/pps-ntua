# Give the Job a descriptive name
#PBS -N run_fwr_flowgraph

## Output and error files
#PBS -o n4096_b256_test3.out
#PBS -e n4096_b256_test3.err

##How long should the job run for?
#PBS -l walltime=00:15:00

#PBS -l nodes=1:ppn=8

## Start
## Run make in the src folder

cd $HOME/Lab1/ex2/FW-parallel/tbb/r_flowgraph

module load tbbz


./fwr_flowgraph 4096 256 8

