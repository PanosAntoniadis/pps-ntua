#!/bin/bash

## Give the Job a descriptive name
#PBS -N test_pthread

## Output and error files
#PBS -o test_pthread.out
#PBS -e test_pthread.err

##How long should the job run for?
#PBS -l walltime=00:10:00

## Start 
## Run make in the src folder

cd $HOME/Lab3/ex2-lock
./test_pthread 1
./test_pthread 2
./test_pthread 4
./test_pthread 8
./test_pthread 16
./test_pthread 32
./test_pthread 64
