#!/bin/bash

while [[ $# > 1 ]]
do
    key="$1"

    case $key in
        -n | --number)
            server_number=$2
            shift
            ;;
        --default)
            echo default
            ;;
        *)
            ;;
    esac
    shift
done

bound=`expr ${server_number} - 1`

for i in $(seq 0 $bound)
do
    echo Stop Graphfs on node-$i
    ssh node-$i "~/graphfs/gmd_release/gmd-server-1.0.4-SNAPSHOT/bin/server.sh stop" &
done
