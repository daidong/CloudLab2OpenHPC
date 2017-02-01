#!/bin/bash

bound=`expr $1 - 1`

for i in $(seq 0 $bound)
do
    echo Install node-$i
    ssh -t node-$i "sudo sntp -s 24.56.178.140" &
done
