# Give the Job a descriptive name
#PBS -N run_fwt_flowgraph

## Output and error files
#PBS -o n4096_b256_x.out
#PBS -e n4096_b256_x.err

##How long should the job run for?
#PBS -l walltime=00:30:00

## Start
## Run make in the src folder

cd $HOME/Lab1/ex2/FW-parallel/tbb/t_flowgraph

module load tbbz

B=256
N=4096

for thr in 1 2 4 8 16 32 64
do
        ./fwt_flowgraph $N $B $thr
done

