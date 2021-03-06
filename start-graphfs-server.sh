#!/bin/bash

port=5555

while [[ $# > 1 ]]
do
    key="$1"

    case $key in
        -n | --number)
            server_number=$2
            shift
            ;;
        -t | --type)
            server_type="$2"
            shift
            ;;
        -d | --db)
            db_dir="$2"
            shift
            ;;
	-p | --port)
	    port=$2
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
seeds=""
line=0
for i in $(seq 0 $bound)
do
    if [ "$line" -eq 0 ]
    then
        seeds="node-$i:$port"
    else
        seeds="$seeds node-$i:$port"
    fi
    line=`expr 1 + $line`
done

localdir=${db_dir}
localdb=${localdir}/gfsdb

for i in $(seq 0 $bound)
do
    echo Start Graphfs on node-$i
    echo "mkdir -p $localdir"
    ssh node-$i "mkdir -p $localdir"
    ssh node-$i "~/graphfs/gmd_release/gmd-server-1.0.4-SNAPSHOT/bin/server.sh start -db $localdb -id $i -type ${server_type} -srvlist $seeds" &
done
