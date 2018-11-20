#!/bin/bash
CURRENT_DIR=$(pwd -P)

export LD_LIBRARY_PATH=${CURRENT_DIR}

#./mjpg_streamer -i "./input_raspicam.so" -o "./output_http.so -w ./www"

#./mjpg_streamer -i "./input_uvc.so -d /dev/video0" -o "./output_http.so -w ./www"

#./mjpg_streamer -i "./input_uvc.so -d /dev/video0" -o "./output_http.so -w ./www"  -o "output_file.so -f pics -d 10000"

#./mjpg_streamer -i "./input_uvc.so" -o "./output_http.so -w ./www"  -o "output_file.so -f pics -d 10000"


./mjpg_streamer -i "./input_raspicam.so" -o "./output_http.so -w ./www"  -o "output_file.so -f pics -d 10000"

#./mjpg_streamer -i "./input_uvc.so -d /dev/video0" -o "./output_http.so -w ./www"  -o "output_file.so -f pics -d 5000"
