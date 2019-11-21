# Give the Job a descriptive name
#PBS -N run_fwt_parfor

## Output and error files
#PBS -o n4096_b64_bind_opt.out
#PBS -e n4096_b64_bind_opt.err

##How long should the job run for?
#PBS -l walltime=00:01:00

## Start
## Run make in the src folder

cd $HOME/Lab1/ex2/FW-parallel/OpenMP

N=4096
B=64

# Run tiled implementation
# export OMP_WAIT_POLICY=active
# export OMP_DYNAMIC=false
# export OMP_PROC_BIND=true

for thr in 1 2 4 8 16 32 64
do
	export OMP_NUM_THREADS=$thr
	./fwt_parfor $N $B
#done
