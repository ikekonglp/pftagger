#!/bin/bash

ROOT_DIR="/home/lingpenk/parsing_friendly_tagger/"

TURBO_DIR="/home/lingpenk/parsing_friendly_tagger/script/TBParser/"
WORKING_DIR="/home/lingpenk/parsing_friendly_tagger/script/debug/"
DATA_DIR="/home/lingpenk/parsing_friendly_tagger/script/db_data/"

TURBO_ORIGINAL_DIR="/home/lingpenk/TBP/TurboParser/"

cd ${TURBO_DIR}

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:`pwd;`/deps/local/lib:"

./TurboTagger --train --file_train=${DATA_DIR}train.tagging.small --file_model=${WORKING_DIR}/tagging_pft_model --tagger_usepft=true --tagger_pft_path=${ROOT_DIR}weights_plain --form_cutoff=1  --train_epochs=10 --logtostderr

./TurboTagger --test --evaluate --file_model=${WORKING_DIR}tagging_pft_model --file_test=${DATA_DIR}dev.tagging --file_prediction=${WORKING_DIR}dev.pdf.predicted --logtostderr

# ./TurboTagger --test --evaluate --file_model=${WORKING_DIR}tagging_pft_model --file_test=${DATA_DIR}dev.tagging --file_prediction=${WORKING_DIR}dev.pdf.predicted --logtostderr

cd ${TURBO_ORIGINAL_DIR}

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:`pwd;`/deps/local/lib:"

./TurboTagger --train --file_train=${DATA_DIR}train.tagging.small --file_model=${WORKING_DIR}/tagging_model --form_cutoff=1 --logtostderr

./TurboTagger --test --evaluate --file_model=${WORKING_DIR}tagging_model --file_test=${DATA_DIR}dev.tagging --file_prediction=${WORKING_DIR}dev.predicted --logtostderr


diff ${WORKING_DIR}dev.pdf.predicted ${WORKING_DIR}dev.predicted