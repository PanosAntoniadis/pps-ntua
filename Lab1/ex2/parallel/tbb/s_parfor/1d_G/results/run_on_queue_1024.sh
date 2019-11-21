# Give the Job a descriptive name
#PBS -N run_fws_parfor_1d_G

## Output and error files
#PBS -o n1024.out
#PBS -e n1024.err

##How long should the job run for?
#PBS -l walltime=00:10:00

## Start
## Run make in the src folder

cd $HOME/Lab1/ex2/FW-parallel/tbb/s_parfor_panos/1d_G

module load tbbz

N=1024

for thr in 1 2 4 8 16 32 64
do
        ./fws_parfor_1d_G $N $thr
done

