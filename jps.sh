#!/bin/bash

bound=`expr $1 - 1`

for i in $(seq 0 $bound)
do
    echo touch node-$i
    ssh node-$i "jps"
done
