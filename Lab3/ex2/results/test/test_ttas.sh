#!/bin/bash

## Give the Job a descriptive name
#PBS -N test_ttas

## Output and error files
#PBS -o test_ttas.out
#PBS -e test_ttas.err

##How long should the job run for?
#PBS -l walltime=00:10:00

## Start 
## Run make in the src folder

cd $HOME/Lab3/ex2
./test_ttas 1
./test_ttas 2
./test_ttas 4
./test_ttas 8
./test_ttas 16
./test_ttas 32
./test_ttas 64
