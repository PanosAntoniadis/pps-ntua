# Give the Job a descriptive name
#PBS -N run_fwr_tasks

## Output and error files
#PBS -o n4096_b128_test.out
#PBS -e n4096_b128_test.err

##How long should the job run for?
#PBS -l walltime=00:10:00

#PBS -l nodes=1:ppn=8

cd $HOME/Lab1/ex2/FW-parallel/tbb/r_tasks

module load tbbz

B=128
N=4096

./fwr_tasks 4096 128 8

