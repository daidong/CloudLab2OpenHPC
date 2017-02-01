#!/bin/bash

bound=`expr $1 - 1`

for i in $(seq 0 $bound)
do
    echo RM Node-$i
    ssh node-$i "mkdir -p /proj/cloudincr-PG0/tools/graphmeta/dbs/edgecut/gdb/"
    ssh node-$i "cp -r ~/dbs/edgecut/gdb/* /proj/cloudincr-PG0/tools/graphmeta/dbs/edgecut/gdb/"
done
