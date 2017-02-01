#!/bin/bash

bound=`expr $1 - 1`

for i in $(seq 0 $bound)
do
    ssh node-$i "source ~/.bashrc"
done
