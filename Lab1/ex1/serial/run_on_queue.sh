#!/bin/bash

## Give the Job a descriptive name
#PBS -N run_GoL_s

## Output and error files
#PBS -o run_GoL_s.out
#PBS -e run_GoL_s.err

## How many machines should we get? 
#PBS -l nodes=1:ppn=8

##How long should the job run for?
#PBS -l walltime=00:10:00

## Start 
## Run make in the src folder

cd $HOME/Lab1/ex1/serial
./GoL_s 64 1000
./GoL_s 1024 1000
./GoL_s 4096 1000
