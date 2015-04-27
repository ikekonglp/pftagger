#!/bin/bash

ROOT_DIR="/home/lingpenk/parsing_friendly_tagger/script/"

CREG_DIR="/home/lingpenk/creg"

ESTIMATION_FILE="/home/lingpenk/parsing_friendly_tagger/script/estimation/estimation"
ESTIMATION_FILE_DEV="/home/lingpenk/parsing_friendly_tagger/script/estimation/estimation_dev"

cd ${CREG_DIR}

# 15.4 is tuned !!!!!!
# for i in $(seq 0 0.1 40)
# do
./creg/creg -n -x ${ESTIMATION_FILE}.feat -y ${ESTIMATION_FILE}.resp --l2 15.4 --tx ${ESTIMATION_FILE_DEV}.feat --ty ${ESTIMATION_FILE_DEV}.resp > ${ESTIMATION_FILE}.weights
# done

cd ${ROOT_DIR}

python WeightsConverter.py ${ESTIMATION_FILE}.weights > ${ESTIMATION_FILE}.weights.pftformat