#!/bin/bash

## Give the Job a descriptive name
#PBS -N make

## Output and error files
#PBS -o make.out
#PBS -e make.err

## How many machines should we get? 

##How long should the job run for?

## Start 
## Run make in the src folder

cd $HOME/Lab1/ex2/FW-parallel/OpenMP
make
