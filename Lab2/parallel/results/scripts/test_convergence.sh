#!/bin/bash

## Give the Job a descriptive name
#PBS -N testjob

## Output and error files
#PBS -o s1024_16_4_2.out
#PBS -e s1024_16_4_2.err

## How many machines should we get? 
#PBS -l nodes=8:ppn=8

## Start 
##echo "PBS_NODEFILE = $PBS_NODEFILE"
##cat $PBS_NODEFILE

module load openmpi/1.8.3
cd $HOME/Lab2/parallel

for execfile in jacobi seidelsor redblacksor 
do
	mpirun -np 64 --map-by node --mca btl self,tcp ${execfile} 1024 1024 16 4
done

