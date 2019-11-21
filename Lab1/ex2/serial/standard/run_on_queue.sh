# Give the Job a descriptive name
#PBS -N run_fws_serial

## Output and error files
#PBS -o fws_serial.out
#PBS -e fws_serial.err

## How many machines should we get?
#PBS -l nodes=1:ppn=1

##How long should the job run for?
#PBS -l walltime=00:05:00

## Start
## Run make in the src folder

cd $HOME/Lab1/ex2/serial

# Run standard implementation
./fw 1024
./fw 2048
./fw 4096 
