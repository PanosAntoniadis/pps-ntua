#!/bin/bash

## Give the Job a descriptive name
#PBS -N test_clh

## Output and error files
#PBS -o test_clh.out
#PBS -e test_clh.err

##How long should the job run for?
#PBS -l walltime=00:10:00

## Start 
## Run make in the src folder

cd $HOME/Lab3/ex2
./test_clh 1
./test_clh 2
./test_clh 4
./test_clh 8
./test_clh 16
./test_clh 32
./test_clh 64
