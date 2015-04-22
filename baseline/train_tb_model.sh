#!/bin/bash

TURBO_ROOT="/home/lingpenk/TBP/TurboParser"
PTB_DIR="/home/lingpenk/Data/PTB/PTB_330/"
TRAIN_FILE="/home/lingpenk/Data/PTB/PTB_330/train.jack"
MODEL_DIR="/home/lingpenk/Data/parsing_friendly_tagger/model/baseline/"

WORKING_DIR="/home/lingpenk/Data/parsing_friendly_tagger/data/baseline/"

CURRENT_MODEL_DIR="/home/lingpenk/Data/models/current_models/"

cd ${TURBO_ROOT}

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:`pwd;`/deps/local/lib:"

## BASIC MODELS ##

./TurboParser --train --file_train=${TRAIN_FILE} --file_model=${MODEL_DIR}jack_basic --prune_basic=false --model_type=basic --logtostderr

./TurboParser --test --evaluate --file_model=${MODEL_DIR}jack_basic --file_test=${PTB_DIR}dev_tbttagged --file_prediction=${WORKING_DIR}dev_tbttagged_jack_basic_pred --logtostderr

./TurboParser --test --evaluate --file_model=${MODEL_DIR}jack_basic --file_test=${PTB_DIR}test_tbttagged --file_prediction=${WORKING_DIR}test_tbttagged_jack_basic_pred --logtostderr

./TurboParser --test --evaluate --file_model=${CURRENT_MODEL_DIR}210basic_sd330 --file_test=${PTB_DIR}dev_tbttagged --file_prediction=${WORKING_DIR}dev_tbttagged_basic_pred --logtostderr

./TurboParser --test --evaluate --file_model=${CURRENT_MODEL_DIR}210basic_sd330 --file_test=${PTB_DIR}test_tbttagged --file_prediction=${WORKING_DIR}test_tbttagged_basic_pred --logtostderr

./TurboParser --test --evaluate --file_model=${CURRENT_MODEL_DIR}210basic_sd330 --file_test=${PTB_DIR}dev --file_prediction=${WORKING_DIR}dev_basic_pred --logtostderr

./TurboParser --test --evaluate --file_model=${CURRENT_MODEL_DIR}210basic_sd330 --file_test=${PTB_DIR}test --file_prediction=${WORKING_DIR}test_basic_pred --logtostderr

perl scripts/eval.pl -s ${WORKING_DIR}dev_tbttagged_jack_basic_pred -g ${PTB_DIR}dev &> ${WORKING_DIR}dev_tbttagged_jack_basic_pred_report
perl scripts/eval.pl -s ${WORKING_DIR}test_tbttagged_jack_basic_pred -g ${PTB_DIR}test &> ${WORKING_DIR}test_tbttagged_jack_basic_pred_report
perl scripts/eval.pl -s ${WORKING_DIR}dev_tbttagged_basic_pred -g ${PTB_DIR}dev &> ${WORKING_DIR}dev_tbttagged_basic_pred_report
perl scripts/eval.pl -s ${WORKING_DIR}test_tbttagged_basic_pred -g ${PTB_DIR}test &> ${WORKING_DIR}test_tbttagged_basic_pred_report
perl scripts/eval.pl -s ${WORKING_DIR}dev_basic_pred -g ${PTB_DIR}dev &> ${WORKING_DIR}dev_basic_pred_report
perl scripts/eval.pl -s ${WORKING_DIR}test_basic_pred -g ${PTB_DIR}test &> ${WORKING_DIR}test_basic_pred_report


## STANDARD MODELS ##

./TurboParser --train --file_train=${TRAIN_FILE} --file_model=${MODEL_DIR}jack_standard --prune_basic=true --model_type=standard --logtostderr

./TurboParser --test --evaluate --file_model=${MODEL_DIR}jack_standard --file_test=${PTB_DIR}dev_tbttagged --file_prediction=${WORKING_DIR}dev_tbttagged_jack_standard_pred --logtostderr

./TurboParser --test --evaluate --file_model=${MODEL_DIR}jack_standard --file_test=${PTB_DIR}test_tbttagged --file_prediction=${WORKING_DIR}test_tbttagged_jack_standard_pred --logtostderr

./TurboParser --test --evaluate --file_model=${CURRENT_MODEL_DIR}210standard_sd330 --file_test=${PTB_DIR}dev_tbttagged --file_prediction=${WORKING_DIR}dev_tbttagged_standard_pred --logtostderr

./TurboParser --test --evaluate --file_model=${CURRENT_MODEL_DIR}210standard_sd330 --file_test=${PTB_DIR}test_tbttagged --file_prediction=${WORKING_DIR}test_tbttagged_standard_pred --logtostderr

./TurboParser --test --evaluate --file_model=${CURRENT_MODEL_DIR}210standard_sd330 --file_test=${PTB_DIR}dev --file_prediction=${WORKING_DIR}dev_standard_pred --logtostderr

./TurboParser --test --evaluate --file_model=${CURRENT_MODEL_DIR}210standard_sd330 --file_test=${PTB_DIR}test --file_prediction=${WORKING_DIR}test_standard_pred --logtostderr

perl scripts/eval.pl -s ${WORKING_DIR}dev_tbttagged_jack_standard_pred -g ${PTB_DIR}dev &> ${WORKING_DIR}dev_tbttagged_jack_standard_pred_report
perl scripts/eval.pl -s ${WORKING_DIR}test_tbttagged_jack_standard_pred -g ${PTB_DIR}test &> ${WORKING_DIR}test_tbttagged_jack_standard_pred_report
perl scripts/eval.pl -s ${WORKING_DIR}dev_tbttagged_standard_pred -g ${PTB_DIR}dev &> ${WORKING_DIR}dev_tbttagged_standard_pred_report
perl scripts/eval.pl -s ${WORKING_DIR}test_tbttagged_standard_pred -g ${PTB_DIR}test &> ${WORKING_DIR}test_tbttagged_standard_pred_report
perl scripts/eval.pl -s ${WORKING_DIR}dev_standard_pred -g ${PTB_DIR}dev &> ${WORKING_DIR}dev_standard_pred_report
perl scripts/eval.pl -s ${WORKING_DIR}test_standard_pred -g ${PTB_DIR}test &> ${WORKING_DIR}test_standard_pred_report

## FULL MODELS ##

./TurboParser --train --file_train=${TRAIN_FILE} --file_model=${MODEL_DIR}jack_full --prune_basic=true --model_type=full --logtostderr

./TurboParser --test --evaluate --file_model=${MODEL_DIR}jack_full --file_test=${PTB_DIR}dev_tbttagged --file_prediction=${WORKING_DIR}dev_tbttagged_jack_full_pred --logtostderr

./TurboParser --test --evaluate --file_model=${MODEL_DIR}jack_full --file_test=${PTB_DIR}test_tbttagged --file_prediction=${WORKING_DIR}test_tbttagged_jack_full_pred --logtostderr

./TurboParser --test --evaluate --file_model=${CURRENT_MODEL_DIR}210full_sd330 --file_test=${PTB_DIR}dev_tbttagged --file_prediction=${WORKING_DIR}dev_tbttagged_full_pred --logtostderr

./TurboParser --test --evaluate --file_model=${CURRENT_MODEL_DIR}210full_sd330 --file_test=${PTB_DIR}test_tbttagged --file_prediction=${WORKING_DIR}test_tbttagged_full_pred --logtostderr

./TurboParser --test --evaluate --file_model=${CURRENT_MODEL_DIR}210full_sd330 --file_test=${PTB_DIR}dev --file_prediction=${WORKING_DIR}dev_full_pred --logtostderr

./TurboParser --test --evaluate --file_model=${CURRENT_MODEL_DIR}210full_sd330 --file_test=${PTB_DIR}test --file_prediction=${WORKING_DIR}test_full_pred --logtostderr

perl scripts/eval.pl -s ${WORKING_DIR}dev_tbttagged_jack_full_pred -g ${PTB_DIR}dev &> ${WORKING_DIR}dev_tbttagged_jack_full_pred_report
perl scripts/eval.pl -s ${WORKING_DIR}test_tbttagged_jack_full_pred -g ${PTB_DIR}test &> ${WORKING_DIR}test_tbttagged_jack_full_pred_report
perl scripts/eval.pl -s ${WORKING_DIR}dev_tbttagged_full_pred -g ${PTB_DIR}dev &> ${WORKING_DIR}dev_tbttagged_full_pred_report
perl scripts/eval.pl -s ${WORKING_DIR}test_tbttagged_full_pred -g ${PTB_DIR}test &> ${WORKING_DIR}test_tbttagged_full_pred_report
perl scripts/eval.pl -s ${WORKING_DIR}dev_full_pred -g ${PTB_DIR}dev &> ${WORKING_DIR}dev_full_pred_report
perl scripts/eval.pl -s ${WORKING_DIR}test_full_pred -g ${PTB_DIR}test &> ${WORKING_DIR}test_full_pred_report



