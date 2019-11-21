# Give the Job a descriptive name
#PBS -N run_fwt_flowgraph

## Output and error files
#PBS -o n4096_b256_test.out
#PBS -e n4096_b256_test.err

##How long should the job run for?
#PBS -l walltime=00:15:00

#PBS -l nodes=1:ppn=8

## Start
## Run make in the src folder

cd $HOME/Lab1/ex2/FW-parallel/tbb/t_flowgraph

module load tbbz

B=256
N=4096

./fwt_flowgraph 4096 256 8

