#!/bin/bash

## Give the Job a descriptive name
#PBS -N test_tas

## Output and error files
#PBS -o test_tas.out
#PBS -e test_tas.err

##How long should the job run for?
#PBS -l walltime=00:10:00

## Start 
## Run make in the src folder

cd $HOME/Lab3/ex2
./test_tas 1
./test_tas 2
./test_tas 4
./test_tas 8
./test_tas 16
./test_tas 32
./test_tas 64
