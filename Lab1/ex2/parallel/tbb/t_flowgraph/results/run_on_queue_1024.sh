# Give the Job a descriptive name
#PBS -N run_fwt_flowgraph

## Output and error files
#PBS -o n1024_b64.out
#PBS -e n1024_b64.err

##How long should the job run for?
#PBS -l walltime=00:10:00

## Start
## Run make in the src folder

cd $HOME/Lab1/ex2/FW-parallel/tbb/t_flowgraph

module load tbbz

B=64
N=1024

for thr in 1 2 4 8 16 32 64
do
        ./fwt_flowgraph $N $B $thr
done

