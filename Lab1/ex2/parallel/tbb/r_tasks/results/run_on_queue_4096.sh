# Give the Job a descriptive name
#PBS -N run_fwr_tasks

## Output and error files
#PBS -o n4096_b256.out
#PBS -e n4096_b256.err

##How long should the job run for?
#PBS -l walltime=00:40:00

## Start
## Run make in the src folder

cd $HOME/Lab1/ex2/FW-parallel/tbb/r_tasks

module load tbbz

B=256
N=4096

for thr in 1 2 4 8 16 32 64
do
	./fwr_tasks $N $B $thr
done
