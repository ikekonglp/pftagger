#!/bin/bash

WORKING_DIR="/home/lingpenk/Data/PTB/PTB_330/jacktagging/"
ESTIMATION_DIR="/home/lingpenk/parsing_friendly_tagger/script/estimation/"
PTB_DIR="/home/lingpenk/Data/PTB/PTB_330/"

BASELINE_DIR="/home/lingpenk/Data/parsing_friendly_tagger/data/baseline/"

# cat ${WORKING_DIR}train1 ${WORKING_DIR}train2 ${WORKING_DIR}train3 ${WORKING_DIR}train4 ${WORKING_DIR}train5 ${WORKING_DIR}train6 ${WORKING_DIR}train7 ${WORKING_DIR}train8 ${WORKING_DIR}train9 ${WORKING_DIR}train10 > ${WORKING_DIR}train_all
# cat ${WORKING_DIR}train1.pred ${WORKING_DIR}train2.pred ${WORKING_DIR}train3.pred ${WORKING_DIR}train4.pred ${WORKING_DIR}train5.pred ${WORKING_DIR}train6.pred ${WORKING_DIR}train7.pred ${WORKING_DIR}train8.pred ${WORKING_DIR}train9.pred ${WORKING_DIR}train10.pred > ${WORKING_DIR}train_all.pred
# cat ${WORKING_DIR}train1.tbtagged.pred ${WORKING_DIR}train2.tbtagged.pred ${WORKING_DIR}train3.tbtagged.pred ${WORKING_DIR}train4.tbtagged.pred ${WORKING_DIR}train5.tbtagged.pred ${WORKING_DIR}train6.tbtagged.pred ${WORKING_DIR}train7.tbtagged.pred ${WORKING_DIR}train8.tbtagged.pred ${WORKING_DIR}train9.tbtagged.pred ${WORKING_DIR}train10.tbtagged.pred > ${WORKING_DIR}train_all.tbtagged.pred

# python PickWrongSentence.py ${WORKING_DIR}train_all ${WORKING_DIR}train_all.pred ${WORKING_DIR}train_all.tbtagged.pred ${ESTIMATION_DIR}estimation
python PickWrongSentence.py ${PTB_DIR}dev ${BASELINE_DIR}dev_basic_pred ${BASELINE_DIR}dev_tbttagged_basic_pred ${ESTIMATION_DIR}estimation_dev