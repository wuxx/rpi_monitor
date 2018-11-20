#!/bin/bash

CURRENT_DIR=$(cd $(dirname $0); pwd)

cd ~/oss/tools/

./keep_dir_size.sh ${CURRENT_DIR} 102400 &

cd ${CURRENT_DIR}

while [ 1 ]; do
    ./run.sh
    echo "error exit, restart again."
    sleep 5
done
