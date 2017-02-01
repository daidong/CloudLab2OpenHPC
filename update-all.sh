#!/bin/bash

bound=`expr $1 - 1`

for i in $(seq 0 $bound)
do
    echo Install node-$i
    ssh -t node-$i "/proj/cloudincr-PG0/tools/graphmeta/update.sh" &
done
