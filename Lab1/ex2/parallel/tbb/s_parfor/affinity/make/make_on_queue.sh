# Give the Job a descriptive name
#PBS -N make

## Output and error files
#PBS -o make.out
#PBS -e make.err

## How many machines should we get?

##How long should the job run for?
#PBS -l walltime=00:01:00

## Start
## Run make in the src folder

cd $HOME/Lab1/ex2/FW-parallel/tbb/s_parfor_panos/affinity
make

