#!/bin/bash

bound=`expr $1 - 1`
type=giga

for i in $(seq 0 $bound)
do
    echo RM Node-$i
    ssh node-$i "mkdir -p ~/dbs/$type/gdb/"
    ssh node-$i "cp -r /proj/cloudincr-PG0/tools/graphmeta/dbs/$type/gdb/gfsdb$i ~/dbs/$type/gdb/"
done
