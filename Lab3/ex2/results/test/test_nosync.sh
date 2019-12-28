#!/bin/bash

## Give the Job a descriptive name
#PBS -N test_nosync

## Output and error files
#PBS -o test_nosync.out
#PBS -e test_nosync.err

##How long should the job run for?
#PBS -l walltime=00:10:00

## Start 
## Run make in the src folder

cd $HOME/Lab3/ex2/
./test_nosync 1
./test_nosync 2
./test_nosync 4
./test_nosync 8
./test_nosync 16
./test_nosync 32
./test_nosync 64
