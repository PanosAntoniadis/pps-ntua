# Give the Job a descriptive name
#PBS -N run_fwt_parfor

## Output and error files
#PBS -o n1024_b16.out
#PBS -e n1024_b16.err

##How long should the job run for?
#PBS -l walltime=00:10:00

## Start
## Run make in the src folder

cd $HOME/Lab1/ex2/FW-parallel/OpenMP

N=1024
B=16

# Run tiled implementation
for thr in 1 2 4 8 16 32 64
do
	export OMP_NUM_THREADS=$thr
	./fwt_parfor $N $B
done

