# Give the Job a descriptive name
#PBS -N run_fws_parfor_2d_G

## Output and error files
#PBS -o n4096.out
#PBS -e n4096.err

##How long should the job run for?
#PBS -l walltime=00:20:00

## Start
## Run make in the src folder

cd $HOME/Lab1/ex2/FW-parallel/tbb/s_parfor_panos/2d_G

module load tbbz

N=4096

for thr in 1 2 4 8 16 32 64
do
        ./fws_parfor_2d_G $N $thr
done
~                                                                                                      
~         
