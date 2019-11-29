# Give the Job a descriptive name
#PBS -N run_serial_1024

## Output and error files
#PBS -o run_serial_1024.out
#PBS -e run_serial_1024.err

## How many machines should we get?
#PBS -l nodes=1:ppn=1

##How long should the job run for?
#PBS -l walltime=00:20:00

## Start
## Run make in the src folder

cd $HOME/Lab2/serial

# Run
./jacobi 1024
./redblacksor 2014
./seidersor 1024
