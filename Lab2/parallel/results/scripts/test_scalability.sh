#!/bin/bash

## Give the Job a descriptive name
#PBS -N testjob

## Output and error files
#PBS -o test_scalability_mpi_2.out
#PBS -e test_scalability_mpi_2.err

## Limit memory, runtime etc.

## How many nodes:processors_per_node should we get?
## Run on parlab
#PBS -l nodes=8:ppn=8

## Start 
##echo "PBS_NODEFILE = $PBS_NODEFILE"
##cat $PBS_NODEFILE

## Run the job (use full paths to make sure we execute the correct thing) 
## NOTE: Fix the path to show to your executable! 

module load openmpi/1.8.3
cd $HOME/Lab2/parallel

## NOTE: Fix the names of your executables

for size in 2048 4096 6144
do
	for execfile in jacobi seidelsor redblacksor
	do
		mpirun  -np 1 --map-by node --mca btl self,tcp ${execfile} ${size} ${size} 1 1 >> ${execfile}_s${size}_c1_2
		mpirun  -np 2 --map-by node --mca btl self,tcp ${execfile} ${size} ${size} 2 1 >> ${execfile}_s${size}_c2_2
		mpirun  -np 4 --map-by node --mca btl self,tcp ${execfile} ${size} ${size} 2 2 >> ${execfile}_s${size}_c4_2
		mpirun  -np 8 --map-by node --mca btl self,tcp ${execfile} ${size} ${size} 4 2 >> ${execfile}_s${size}_c8_2
		mpirun  -np 16 --map-by node --mca btl self,tcp ${execfile} ${size} ${size} 4 4 >> ${execfile}_s${size}_c16_2
		mpirun  -np 32 --map-by node --mca btl self,tcp ${execfile} ${size} ${size} 8 4 >> ${execfile}_s${size}_c32_2
                mpirun  -np 64 --map-by node --mca btl self,tcp ${execfile} ${size} ${size} 8 8 >> ${execfile}_s${size}_c64_2
	done
done

## Make sure you disable convergence testing and printing
