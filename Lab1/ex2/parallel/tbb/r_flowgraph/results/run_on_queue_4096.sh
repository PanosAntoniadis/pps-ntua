# Give the Job a descriptive name
#PBS -N run_fwr_flowgraph

## Output and error files
#PBS -o n4096_b64.out
#PBS -e n4096_b64.err

##How long should the job run for?
#PBS -l walltime=00:30:00

## Start
## Run make in the src folder

cd $HOME/Lab1/ex2/FW-parallel/tbb/r_flowgraph

module load tbbz

B=64
N=4096

for thr in 1 2 4 8 16 32 64
do
        ./fwr_flowgraph $N $B $thr
done

