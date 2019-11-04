#!/bin/bash

## Give the Job a descriptive name
#PBS -N make_GoL_s

## Output and error files
#PBS -o make_GoL_s.out
#PBS -e make_GoL_s.err

## How many machines should we get? 
#PBS -l nodes=1:ppn=1

##How long should the job run for?
#PBS -l walltime=00:10:00

## Start 
## Run make in the src folder

cd $HOME/Lab1/ex1/serial
make
