# Give the Job a descriptive name
#PBS -N run_fwt_serial

## Output and error files
#PBS -o b32.out
#PBS -e b32.err

## How many machines should we get?
#PBS -l nodes=1:ppn=1

##How long should the job run for?
#PBS -l walltime=00:20:00

## Start
## Run make in the src folder

cd $HOME/Lab1/ex2/serial

# Run tiled implementation
./fw_tiled 1024 32
./fw_tiled 2048 32
./fw_tiled 4096 32

