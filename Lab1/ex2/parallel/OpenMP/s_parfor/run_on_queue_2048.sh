# Give the Job a descriptive name
#PBS -N run_fws_parfor

## Output and error files
#PBS -o n2048.out
#PBS -e n2048.err

##How long should the job run for?
#PBS -l walltime=00:20:00

## Start
## Run make in the src folder

cd $HOME/Lab1/ex2/FW-parallel/OpenMP

N=2048

# Run standard implementation
for thr in 1 2 4 8 16 32 64
do
	export OMP_NUM_THREADS=$thr
	./fws_parfor $N
done
