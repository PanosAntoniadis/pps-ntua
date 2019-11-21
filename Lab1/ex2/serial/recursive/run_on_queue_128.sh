# Give the Job a descriptive name
#PBS -N run_fwr_serial

## Output and error files
#PBS -o b128.out
#PBS -e b128.err

## How many machines should we get?
#PBS -l nodes=1:ppn=1

##How long should the job run for?
#PBS -l walltime=00:20:00

## Start
## Run make in the src folder

cd $HOME/Lab1/ex2/serial

# Run recursive implementation
./fw_sr 1024 128
./fw_sr 2048 128
./fw_sr 4096 128
