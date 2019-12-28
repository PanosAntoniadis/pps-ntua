#!/bin/bash

## Give the Job a descriptive name
#PBS -N test_array

## Output and error files
#PBS -o test_array.out
#PBS -e test_array.err

##How long should the job run for?
#PBS -l walltime=00:10:00

## Start 
## Run make in the src folder

cd $HOME/Lab3/ex2
./test_array 1
./test_array 2
./test_array 4
./test_array 8
./test_array 16
./test_array 32
./test_array 64
