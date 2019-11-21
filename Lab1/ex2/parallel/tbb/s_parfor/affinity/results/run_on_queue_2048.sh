# Give the Job a descriptive name
#PBS -N run_fws_parfor_aff

## Output and error files
#PBS -o n2048.out
#PBS -e n2048.err

##How long should the job run for?
#PBS -l walltime=00:15:00

## Start
## Run make in the src folder

cd $HOME/Lab1/ex2/FW-parallel/tbb/s_parfor_panos/affinity

module load tbbz

N=2048

for thr in 1 2 4 8 16 32 64
do
        ./fws_parfor_aff $N $thr
done

