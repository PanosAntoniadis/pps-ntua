#!/bin/bash

## Give the Job a descriptive name
#PBS -N run_GoL_p

## Output and error files
#PBS -o run_GoL_p.out
#PBS -e run_GoL_p.err

## How many machines should we get?
#PBS -l nodes=1:ppn=8

##How long should the job run for?
#PBS -l walltime=00:30:00

## Start
## Run in the src folder

cd $HOME/Lab1/ex1/parallel

for thr in 1 2 4 6 8
do
  export OMP_NUM_THREADS=$thr
  ./GoL_p 64 1000
  ./GoL_p 1024 1000
  ./GoL_p 4096 1000
done
