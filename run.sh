#!/bin/bash

ROOT_DIR="/home/lingpenk/parsing_friendly_tagger/"

TURBO_DIR="/home/lingpenk/parsing_friendly_tagger/script/TBParser/"
WORKING_DIR="/home/lingpenk/parsing_friendly_tagger/script/run/"
DATA_DIR="/home/lingpenk/parsing_friendly_tagger/script/db_data/"

TURBO_ORIGINAL_DIR="/home/lingpenk/TBP/TurboParser/"

CURRENT_MODEL_DIR="/home/lingpenk/Data/models/current_models/"

FORCE="0.5"

FORCE_TEST="0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8"

# PARA="parallel --dryrun "
PARA="parallel "


PARA_END=" ::: "${FORCE_TEST}

cd ${TURBO_DIR}

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:`pwd;`/deps/local/lib:"

${PARA} ./TurboTagger --train --file_train=${DATA_DIR}train.tagging --file_model=${WORKING_DIR}/tagging_pft_model_force{} --tagger_usepft=true --tagger_pft_path=${ROOT_DIR}weights --pft_force={} --form_cutoff=1 --logtostderr ${PARA_END}

${PARA} ./TurboTagger --test --evaluate --file_model=${WORKING_DIR}tagging_pft_model_force{} --file_test=${DATA_DIR}dev.tagging --file_prediction=${WORKING_DIR}dev.pdf.{}.predicted --logtostderr ${PARA_END}

${PARA} ./TurboTagger --test --evaluate --file_model=${WORKING_DIR}tagging_pft_model_force{} --file_test=${DATA_DIR}test.tagging --file_prediction=${WORKING_DIR}test.pdf.{}.predicted --logtostderr ${PARA_END}

for f in ${FORCE_TEST}
do
python /home/lingpenk/research/scripts/TagConllUsingTBT.py ${DATA_DIR}dev ${WORKING_DIR}dev.pdf.${f}.predicted Y > ${WORKING_DIR}dev.pdf.${f}.tagged
python /home/lingpenk/research/scripts/TagConllUsingTBT.py ${DATA_DIR}test ${WORKING_DIR}test.pdf.${f}.predicted Y > ${WORKING_DIR}test.pdf.${f}.tagged
done

cd ${TURBO_ORIGINAL_DIR}

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:`pwd;`/deps/local/lib:"

${PARA} ./TurboParser --test --evaluate --file_model=${CURRENT_MODEL_DIR}210basic_sd330 --file_test=${WORKING_DIR}dev.pdf.{}.tagged --file_prediction=${WORKING_DIR}dev.pdf.{}.tagged.predicted --logtostderr ${PARA_END}
${PARA} ./TurboParser --test --evaluate --file_model=${CURRENT_MODEL_DIR}210basic_sd330 --file_test=${WORKING_DIR}test.pdf.{}.tagged --file_prediction=${WORKING_DIR}test.pdf.{}.tagged.predicted --logtostderr ${PARA_END}

for f in ${FORCE_TEST}
do
perl scripts/eval.pl -s ${WORKING_DIR}dev.pdf.${f}.tagged.predicted -g ${DATA_DIR}dev &> ${WORKING_DIR}dev.pdf.${f}.tagged.predicted.report
perl scripts/eval.pl -s ${WORKING_DIR}test.pdf.${f}.tagged.predicted -g ${DATA_DIR}test &> ${WORKING_DIR}test.pdf.${f}.tagged.predicted.report
done