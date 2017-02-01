#!/bin/bash

bound=`expr $1 - 1`

for i in $(seq 0 $bound)
do
    echo RM Node-$i
    #ssh node-$i "mv /tmp/gmdsrv.pid /tmp/gmdsrv.pid.back"
    ssh node-$i "mv /tmp/gmdsrv.pid.back /tmp/gmdsrv.pid"
done
