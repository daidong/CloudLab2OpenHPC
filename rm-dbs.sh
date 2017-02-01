#!/bin/bash

bound=`expr $1 - 1`

for i in $(seq 0 $bound)
do
    echo RM Node-$i
    ssh node-$i "rm -r ~/dbs/incrgiga/gdb/"
done
