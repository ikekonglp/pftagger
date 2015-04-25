#!/bin/bash

FORCE="0.5"

FORCE_TEST="0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 1.1 1.2 1.3 1.4 1.5 1.6"

# PARA="parallel --dryrun "
PARA="parallel "


PARA_END=" ::: "${FORCE_TEST}

myfun()
{
ROOT_DIR="/home/lingpenk/parsing_friendly_tagger/"
TURBO_DIR="/home/lingpenk/parsing_friendly_tagger/script/TBParser/"
WORKING_DIR="/home/lingpenk/parsing_friendly_tagger/script/run/"
DATA_DIR="/home/lingpenk/parsing_friendly_tagger/script/db_data/"

TURBO_ORIGINAL_DIR="/home/lingpenk/TBP/TurboParser/"

CURRENT_MODEL_DIR="/home/lingpenk/Data/models/current_models/"
cd ${TURBO_DIR}

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:`pwd;`/deps/local/lib:"

./TurboTagger --train --file_train=${DATA_DIR}train.tagging --file_model=${WORKING_DIR}/tagging_pft_model_force$1 --tagger_usepft=true --tagger_pft_path=${ROOT_DIR}weights --pft_force=$1 --form_cutoff=1 --logtostderr

./TurboTagger --test --evaluate --file_model=${WORKING_DIR}tagging_pft_model_force$1 --file_test=${DATA_DIR}dev.tagging --file_prediction=${WORKING_DIR}dev.pft.$1.predicted --logtostderr

./TurboTagger --test --evaluate --file_model=${WORKING_DIR}tagging_pft_model_force$1 --file_test=${DATA_DIR}test.tagging --file_prediction=${WORKING_DIR}test.pft.$1.predicted --logtostderr

python /home/lingpenk/research/scripts/TagConllUsingTBT.py ${DATA_DIR}dev ${WORKING_DIR}dev.pft.$1.predicted Y > ${WORKING_DIR}dev.pft.$1.tagged
python /home/lingpenk/research/scripts/TagConllUsingTBT.py ${DATA_DIR}test ${WORKING_DIR}test.pft.$1.predicted Y > ${WORKING_DIR}test.pft.$1.tagged

cd ${TURBO_ORIGINAL_DIR}

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:`pwd;`/deps/local/lib:"

./TurboParser --test --evaluate --file_model=${CURRENT_MODEL_DIR}210basic_sd330 --file_test=${WORKING_DIR}dev.pft.$1.tagged --file_prediction=${WORKING_DIR}dev.pft.$1.tagged.predicted --logtostderr
./TurboParser --test --evaluate --file_model=${CURRENT_MODEL_DIR}210basic_sd330 --file_test=${WORKING_DIR}test.pft.$1.tagged --file_prediction=${WORKING_DIR}test.pft.$1.tagged.predicted --logtostderr

perl scripts/eval.pl -s ${WORKING_DIR}dev.pft.$1.tagged.predicted -g ${DATA_DIR}dev &> ${WORKING_DIR}dev.pft.$1.tagged.predicted.report
perl scripts/eval.pl -s ${WORKING_DIR}test.pft.$1.tagged.predicted -g ${DATA_DIR}test &> ${WORKING_DIR}test.pft.$1.tagged.predicted.report
}

export -f myfun
parallel myfun {} ${PARA_END}