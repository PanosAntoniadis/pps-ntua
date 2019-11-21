# Give the Job a descriptive name
#PBS -N run_fwr_tasks

## Output and error files
#PBS -o n4096_b256_test.out
#PBS -e n4096_b256_test.err

##How long should the job run for?
#PBS -l walltime=00:10:00

#PBS -l nodes=1:ppn=8

## Start
## Run make in the src folder

cd $HOME/Lab1/ex2/FW-parallel/OpenMP

N=4096
B=256

# Run recursive implementation
export OMP_NUM_THREADS=8
./fwr_tasks 4096 256

